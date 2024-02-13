'''Flask form for user registration'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Length, EqualTo, Email, DataRequired
from market.model import User


class Form(FlaskForm):

  def validate_username(self, username_to_check):
    user = User.query.filter_by(username=username_to_check.data).first()
    if user:
      raise ValidationError('Username already exists! Please try a different name')

    def vaildate_email(self, email_to_check):
      email = User.query.filter_by(email = email_to_check.data).first()
      if email:
        raise ValidationError('Email already exists! Please try a different email')
    
    '''User Registration | Sign-in and Sign-up'''
    username = StringField(label='Username', description="Username", validators=[Length(min=2,max=30),DataRequired()])
    email = StringField(label='Email', description="Email address", validators= [Email(), DataRequired()])
    password = PasswordField(label='Password', description="Password", validators=[Length(min=6),DataRequired()])
    confirm_password = PasswordField(
        label='Confirm password', description="Confirm password", validators= [EqualTo('password'),DataRequired()])
    submit = SubmitField(label='Create Account')
