from app import app, socketio
from flask import Blueprint, render_template, flash, redirect, request, url_for, session, abort, jsonify
from flask.ext.socketio import emit, join_room
import mailing
import forms
import userDAO
from decorators import requireLoginLevel
from functions import get_db
import logging
import string, random

logr = logging.getLogger('SonicPlatform.blueprint_chan')
chan_B = Blueprint('users', __name__)

@chan_B.route('/chat', methods = ['POST'])
def chat():

    return render_template('chattest.html')

@socketio.on('connect', namespace='/MISChat')
def connect2():
    # join_room(session['user'])
    room = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
    emit('connectConfirm', {'ok': 1, 'room':room})

# 'disconnected' is a special event
@socketio.on('disconnect')
def disconnected():
    pass

@socketio.on('userDisconnect', namespace='/MISChat')
def userDisconnect(user, room, fname, lname, tStamp):
    db = get_db()
    db.msgs.insert({'room':room, 'user':user, 'left':True, 'time':tStamp})
    emit('userDisconnect', {'ok': 1, 'user':user, 'room':room, 'time':tStamp}, broadcast=True)


@socketio.on('joined', namespace='/MISChat')
def joined(user, mode, room, fname, lname, tStamp):
    #at some point, twisted will be implemented instead of this
    #loggedIn.addUser(user)
    #print loggedIn.getUsers()
    db = get_db()
    db.msgs.insert({'room':room, 'user':user, 'joined':True, 'time':tStamp})
    emit('joined', {'user':user,'mode':mode, 'room':room, 'time':tStamp}, broadcast=True)

@socketio.on('checkUsersOnlineInit', namespace='/MISChat')
def checkUsersOnlineInit():
    emit('checkUsersOnlineInit', {}, broadcast=True)

@socketio.on('checkUsersOnlineConfirm', namespace='/MISChat')
def checkUsersOnlineConfirm(user, status, tStamp):
    db = get_db()
    cur = [msg for msg in db.msgs.find({'room':status, 'msg':{'$exists':True}},{'_id':0}).sort([('$natural',-1)]).limit(20)]
    emit('checkUsersOnlineConfirm', {'msgs':cur, 'user':user, 'room':status, 'time':tStamp}, broadcast=True)

@socketio.on('chatMsg', namespace='/MISChat')
def chatMsg(user, fname, lname, data, room, tStamp):
    #
    # #msgs.insert({'post':message})
    # if message != 'connected':
    #
    #     msgsCol.insert({'user':message['user'], 'msg':message['post']})
    #
    #     emit('update', message, broadcast=True)
    db = get_db()
    db.msgs.insert({'room':room, 'user':user, 'fname':fname, 'lname':lname, 'msg':data, 'time':tStamp})
    emit('chatMsg', {'user':user,  'fname':fname, 'lname':lname, 'data':data, 'room':room, 'time':tStamp}, broadcast=True)
