'''Flask form for user registration'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import Length, EqualTo, DataRequired


class Form(FlaskForm):
    '''User Registration | Sign-in and Sign-up'''
    username = StringField(label='Username', description="Username", validators=[Length(min=2,max=30),DataRequired()])
    email = StringField(label='Email', description="Email address", validators= [Email(), DataRequired()])
    password = PasswordField(label='Password', description="Password", validators=[Length(min=6),DataRequired()])
    confirm_password = PasswordField(
        label='Confirm password', description="Confirm password", validators= [EqualTo('password'),DataRequired()])
    submit = SubmitField(label='Create Account')
