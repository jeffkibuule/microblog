from flask_mail import Message
from flask import render_template
from flask_babel import _
from app import mail, current_app
from threading import Thread

def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body,
               attachments=None, sync=False):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    if attachments:
           for attachment in attachments:
                  msg.attach(*attachment)
    if sync:
           mail.send(msg)
    else:
    	Thread(target=send_async_mail, 
           		args=(current_app._get_current_object(), msg)).start()

def send_password_reset_email(user):
		token = user.get_reset_password_token()
		send_email(_('[Microblog] Reset Your Password'),
			 		sender=current_app.config['ADMINS'][0],
					recipients=[user.email],
					text_body=render_template('email/reset_password.txt',
							   user=user, token=token),
					html_body=render_template('email/reset_password.html',
							   user=user, token=token))