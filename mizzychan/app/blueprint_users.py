from app import app, socketio
from flask import Blueprint, render_template, flash, redirect, request, url_for, session, abort, jsonify
import mailing
import forms
import userDAO
from decorators import requireLoginLevel
from functions import get_db
import logging

logr = logging.getLogger('SonicPlatform.blueprint_users')
users_B = Blueprint('users', __name__)





@users_B.route('/verifylogin', methods = ['POST'])
def verifylogin():


    loginForm = forms.loginForm()    
    
    if loginForm.validate_on_submit():
        db = get_db()


        userSecurity = userDAO.userDAO(db)
        user = userSecurity.validate_login(loginForm.userName.data.lower(),loginForm.password.data)

        if user not in [None, False]:
            session['level'] = user['level']
            session['user'] = user['_id']
            session['fname'] = user['firstName']
            session['lname'] = user['lastName']
            session['linuxUser'] = userSecurity.check_user_linux(user['_id'])


            if user['aws_can_create_cluster']:
                session['aws'] = True
            else:
                session['aws'] = False


            if 'wantsurl' in request.form:
                return redirect(request.form['wantsurl'])
            else:
                return redirect('/')

        if user == False:
            body = """<p>Sorry, this username is currently locked out. You must contact the system administrator to unlock it</p>"""
            header = "Login Error"
            return render_template("completepage.html", header = header, body = body, loginForm = loginForm)

    body = """<p>Sorry, this username / password combination was not found in the database</p>"""
    if app.config.get('LDAP_ENABLED', False) == False:
        body += '<div class="loginInfo"><a href="%s">Forgot username / password?</a></div>' % (url_for('users.forgotlogininfo'))

    header = "Login Error"

    return render_template("completepage.html", header = header, body = body, loginForm = loginForm)


@users_B.route('/logout', methods = ['GET'])
def logout():
    session.clear()
    flash("Logged out successfully", 'success')
    return redirect('/')




               
        
