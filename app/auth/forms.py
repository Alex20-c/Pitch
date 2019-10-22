from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    email =  SubmitField('Your Email Address',Validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
	password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
	password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
	submit = SubmitField('Sign Up')
 
def validate_email(self,data_field):
    if User.query.filter_by(email =data_field.data).first():
        raise ValidationError('There is an account with that email')
    
def validator_username(self,data_field):
    if User.query.filter_by(username = data_field.data).first():
        raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    username = StringField('username',validators=[Required()])
    password = PasswordField('password',validators=[Required()])
    remember = BooleanField("Remember me")
    submit = SubmitField("submit")
