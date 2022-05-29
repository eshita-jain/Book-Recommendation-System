from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length,Email,EqualTo, ValidationError
from Main.models import User


class RegistrationForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	confirm_pswd=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('Sign Up')

	def validate_username(self,username):
		user=User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please Choose a different one.')

	def validate_email(self,email):
		user=User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please Choose a different one.')



class LoginForm(FlaskForm):
	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	remember=BooleanField('Remember Me')
	submit=SubmitField('Login')

class BookForm(FlaskForm):
	bookname=StringField('Enter Book Name',validators=[DataRequired()])
	submit=SubmitField('Get Recommendations !')

class UploadBook(FlaskForm):
	ISBN=StringField('ISBN',validators=[DataRequired(),Length(min=2,max=15)])
	Title=StringField('Title',validators=[DataRequired()])
	Author=StringField('Author',validators=[DataRequired()])
	Publisher=StringField('Publisher',validators=[DataRequired()])
	ImageURL=StringField('Image URL',validators=[DataRequired()])
	submit=SubmitField('Upload Details')


class Contact(FlaskForm):
	subject=StringField('Subject',validators=[DataRequired(),Length(min=5,max=12)])
	query=StringField('Query',validators=[DataRequired()])
	submit=SubmitField('Submit')


class DeleteBook(FlaskForm):
	ISBN=StringField('Enter ISBN :',validators=[DataRequired(),Length(min=2,max=15)])
	submit=SubmitField('Delete Book ;)')


class UpdateAccount(FlaskForm):
	username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	email=StringField('Email',validators=[DataRequired(),Email()])
	picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
	submit=SubmitField('Update')

	def validate_username(self,username):
		if username.data != current_user.username:
			user=User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('That username is taken. Please Choose a different one.')

	def validate_email(self,email):
		if email.data != current_user.email:
			user=User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('That email is taken. Please Choose a different one.')

