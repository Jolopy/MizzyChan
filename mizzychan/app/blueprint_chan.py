from app import app, socketio
from flask import Blueprint, render_template, flash, redirect, request, url_for, session, abort, jsonify
from flask_socketio import emit, join_room, leave_room
import mailing
import forms
import userDAO
from decorators import requireLoginLevel
from functions import get_db
import logging
import string, random
import requests
logr = logging.getLogger('SonicPlatform.blueprint_chan')
chan_B = Blueprint('chan', __name__)

@chan_B.route('/chat', methods = ['GET'])
def helpchatclient():
    room=request.args['room'] if 'room' in request.args else None
    return render_template('chattest.html', room=room)

@chan_B.route('/changeUserName', methods = ['POST'])
def changeUserName():
    return jsonify({'ok': 1})
    if all(x in request.form for x in ('g-recaptcha-response', 'userNameChange')):

        dictToSend = {'secret': '6Ldw_wkUAAAAAJFyh_Pmg1KKyM_1ta4Rwg3smpEY',
                      'response': request.form['g-recaptcha-response']}
        res = requests.get('https://www.google.com/recaptcha/api/siteverify',
                           params=dictToSend,
                           verify=True)
        if res.json()['success']:

            return jsonify({'ok': 1})
        else:
            return jsonify({'ok': 0})
    else:
        return jsonify({'ok': 0})


@chan_B.route('/categories/<category>', methods = ['GET'])
def categories(category):
    print category

    labels={'Top_Rated':'Top Rated',
            'US_News': 'US News',
            'World_News':'World News',
            'Politics':'Politics',
            'Science':'Science',
            'Technology':'Technology',
            'Entertainment':'Entertainment',
            'Business':'Business',
            'Gaming':'Gaming',
            'Sports':'Sports',
            'Health':'Health',
            'Memes':'Memes'}
    name = labels[category]


    return render_template('categories.html', categoryName=name)


@socketio.on('connect', namespace='/chat')
def connect2():
    # join_room(session['user'])
    # room = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))

    emit('connectConfirm')

# 'disconnected' is a special event
@socketio.on('disconnect')
def disconnected():
    pass

@socketio.on('userDisconnect', namespace='/chat')
def userDisconnect(user, room):
    #db = get_db()
    #db.msgs.insert({'room':room, 'user':user, 'left':True, 'time':tStamp})

    leave_room(room)
    emit('userDisconnect', {'ok': 1, 'user':user, 'room':room}, room=room)


@socketio.on('joined', namespace='/chat')
def joined(user, room):
    join_room(room)
    #at some point, twisted will be implemented instead of this
    #loggedIn.addUser(user)
    #print loggedIn.getUsers()
    #db = get_db()
    #db.msgs.insert({'room':room, 'user':user, 'joined':True, 'time':tStamp})

    print 'user joined'
    emit('joined', {'ok': 1, 'user': user}, room=room)


# @socketio.on('checkUsersOnlineInit', namespace='/chat')
# def checkUsersOnlineInit():
#     emit('checkUsersOnlineInit', {}, broadcast=True)
#
# @socketio.on('checkUsersOnlineConfirm', namespace='/chat')
# def checkUsersOnlineConfirm(user, status):
#     db = get_db()
#     #cur = [msg for msg in db.msgs.find({'room':status, 'msg':{'$exists':True}},{'_id':0}).sort([('$natural',-1)]).limit(20)]
#     cur = []
#     emit('checkUsersOnlineConfirm', {'msgs':cur, 'user':user, 'room':status}, room=room)

@socketio.on('chatMsg', namespace='/chat')
def chatMsg(user, room, data):


    # #msgs.insert({'post':message})
    # if message != 'connected':
    #
    #     msgsCol.insert({'user':message['user'], 'msg':message['post']})
    #
    #     emit('update', message, broadcast=True)
    #db = get_db()
    #db.msgs.insert({'room':room, 'user':user, 'msg':data})
    emit('chatMsg', {'user':user, 'data':data, 'room':room}, room=room)
