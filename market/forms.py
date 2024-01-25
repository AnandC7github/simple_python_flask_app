'''Flask form for user registration'''
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField


class Form(FlaskForm):
    '''User Registration | Sign-in and Sign-up'''
    username = StringField(label='Username', description="Username")
    email = StringField(label='Email', description="Email address")
    password = StringField(label='Password', description="Password")
    confirm_password = StringField(
        label='Confirm password', description="Confirm password")
    submit = SubmitField(label='Submit')
