__author__ = 'paul'

import pymongo
import operator
import xlwt
import datetime

# connections to the sonic web and local audit databases
MONGO_LOCAL_HOST = 'localhost'
MONGO_LOCAL_PORT = 27017
MONGO_LOCAL_DATABASE = 'sonic'
MONGO_LOCAL_AUTHENTICATION_DATABASE = None
MONGO_LOCAL_USER = None
MONGO_LOCAL_PASS = None

# connections to the remote "command log" storage database
MONGO_REMOTE_HOST = '52.1.50.7'
MONGO_REMOTE_PORT = 27017
MONGO_REMOTE_DATABASE = 'audit'
MONGO_REMOTE_AUTHENTICATION_DATABASE = 'admin'
MONGO_REMOTE_USER = 'admin'
MONGO_REMOTE_PASS = 'Peace@75!'

class FormatAudit(object):

    def __init__(self):
        self.lc = self._connect_local()
        self.rc = self._connect_remote()

    def _connect_local(self):
        connection = pymongo.MongoClient(MONGO_LOCAL_HOST, MONGO_LOCAL_PORT)
        if MONGO_LOCAL_USER:
            if MONGO_LOCAL_AUTHENTICATION_DATABASE == None:
                getattr(connection, MONGO_LOCAL_DATABASE).authenticate(MONGO_LOCAL_USER, MONGO_LOCAL_PASS)
            else:
                getattr(connection, MONGO_LOCAL_AUTHENTICATION_DATABASE).authenticate(MONGO_LOCAL_USER, MONGO_LOCAL_PASS)
        return connection

    def _connect_remote(self):
        connection = pymongo.MongoClient(MONGO_REMOTE_HOST, MONGO_REMOTE_PORT)
        if MONGO_REMOTE_USER:
            if MONGO_REMOTE_AUTHENTICATION_DATABASE == None:
                getattr(connection, MONGO_REMOTE_DATABASE).authenticate(MONGO_REMOTE_USER, MONGO_REMOTE_PASS)
            else:
                getattr(connection, MONGO_REMOTE_AUTHENTICATION_DATABASE).authenticate(MONGO_REMOTE_USER, MONGO_REMOTE_PASS)
        return connection

    def _get_user(self, db, user):
        userObj = db.users.find_one({'_id':user}, {'_id':0, 'clusters':1})
        if not userObj:
            raise LookupError("User %s not found in database!" % user)
        else:
            return userObj
        
    def _datesort_absolute(self, arr):
        """
        Sort the given array of mongo objects by dates in an absolute fashion. This can be an option.        
        :param arr: the array of objects which should all have the 'dte' key somewhere to be sorted on
        :return: the same array, but sorted
        """
        try:
            cmp = operator.itemgetter("dte")
            arr.sort(key=cmp, reverse=True)
        except:
            print "Datesort_Absolute has failed!, defaulting..."
        return arr
        
    def get_all_audits(self, user):
        '''
        Use the three other instance methods to obtain every piece of audit data related to this specific user
        :param user: the username of the user
        :return: the array of audit objects, date descending sorted
        '''
        print "Retrieving All Required data..."
        audits = []
        audits += self.get_site_actions(user)
        audits += self.get_commands_audit_local(user)
        audits += self.get_commands_audit_remote(user)
        return self._datesort_absolute(audits)

    def get_all_user_clusters(self, user):
        """
        Get all of the cluster ids which belong to a specific user
        :return: the list of ids or None if user does not exist
        """

        db = self.lc[MONGO_LOCAL_DATABASE]
        userObj = self._get_user(db, user)
        userClusters = []
        userClusters += userObj['clusters']
        userTermCur = db.terminated.find({'user':user}, {'_id':1})
        for termObj in userTermCur:
            userClusters.append(termObj['_id'])
        return userClusters

    def get_site_actions(self, user):
        """
        Get all of the site audit messages
        :param user: the username of the user
        :return: list of site action objects, descending date
        """
        print "Downloading user site actions..."
        db = self.lc[MONGO_LOCAL_DATABASE]
        userObj = self._get_user(db, user)
        siteActions = []
        siteActionsCur = db.siteAudit.find({'user':user}, {'_id':0}).sort([('dte',-1)])
        for ActionObj in siteActionsCur:
            siteActions.append(ActionObj)
        return siteActions

    def get_commands_audit_local(self, user):
        """
        Get all the rest of the audit besides the web part, from the local database
        :param user: the username of the user
        :return: list of site action objects, descending data
        """
        print "Downloading user local environment commands..."
        db = self.lc[MONGO_LOCAL_DATABASE]
        userObj = self._get_user(db, user)
        audits = []
        commandAuditsCurLocal = db.audits.find({'user':user}, {'_id':0}).sort([('dte',-1)])
        for auditObj in commandAuditsCurLocal:
            audits.append(auditObj)
        return audits

    def get_commands_audit_remote(self, user):
        """
        Get all the rest of the audit besides the web part, from the remote database
        :param user: the username of the user
        :return: list of site action objects, descending data
        """
        print "Downloading user remote environment commands..."
        db = self.lc[MONGO_LOCAL_DATABASE]
        userObj = self._get_user(db, user)
        db = self.rc[MONGO_REMOTE_DATABASE]
        userClusters = self.get_all_user_clusters(user)
        audits = []
        for cluster in userClusters:
            commandAuditsCurRemote = db[str(cluster)].find({}, {'_id':0}).sort([('dte',-1)])
            for auditObj in commandAuditsCurRemote:
                auditObj['user'] = user
                audits.append(auditObj)
        return audits


class FitSheetWrapper(object):
    """Try to fit columns to max size of any entry.
    To use, wrap this around a worksheet returned from the
    workbook's add_sheet method, like follows:

        sheet = FitSheetWrapper(book.add_sheet(sheet_name))

    The worksheet interface remains the same: this is a drop-in wrapper
    for auto-sizing columns.
    """
    def __init__(self, sheet):
        self.sheet = sheet
        self.widths = dict()

    def write(self, r, c, label='', *args, **kwargs):
        self.sheet.write(r, c, label, *args, **kwargs)
        width = len(label)*367 #arial10.fitwidth(label)
        if width > self.widths.get(c, 0):
            try:
                self.widths[c] = width
                self.sheet.col(c).width = width
            except:
                print "setting width failed!"

    def __getattr__(self, attr):
        return getattr(self.sheet, attr)

user = 'admin'
reader = FormatAudit()

colFormat = {'user':0, 'dte':1, 'action':2, 'details':3}
detailFormat = ['type', 'a0', 'a1', 'a2', 'a3', 'a4']

data = reader.get_all_audits(user)

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
style2 = xlwt.easyxf("align: wrap on, vert centre, horiz center")


wb = xlwt.Workbook()
#datetime.datetime.strftime(datetime.datetime.now(), '%c')
ws = FitSheetWrapper(wb.add_sheet('Audit Report for %s' % user))

for i, audit in enumerate(data):

    ws.write(i, colFormat['user'], audit['user'], style2)
    dte = datetime.datetime.strftime(audit['dte'], '%c')
    ws.write(i, colFormat['dte'], dte, style2)
    ws.write(i, colFormat['action'], audit['action'], style2)
    details = audit.get('details', {})
    offset = 3
    for extra in detailFormat:
        if extra in details:
            wstr = "%s = %s" % (extra, details[extra])
            ws.write(i, offset, wstr, style2)
            offset += 1
            del details[extra]
    for j, extra in enumerate(details):
        wstr = "%s = %s" % (extra, details[extra])
        ws.write(i, j+offset, wstr, style2)

wb.save('auditlog-%s.xls' % user)



