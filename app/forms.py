from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class HousehelpRegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    county = StringField('County', validators=[DataRequired()])
    next_of_kin = StringField('Next of Kin')
    experience = StringField('Experience')
    salary_expectation = IntegerField('Salary Expectation')
    preferred_location = StringField('Preferred Location')
    age = IntegerField('Age')
    submit = SubmitField('Register')

class FeedbackForm(FlaskForm):
    content = TextAreaField('Feedback', validators=[DataRequired()])
    submit = SubmitField('Submit Feedback')

class ComplaintForm(FlaskForm):
    content = TextAreaField('Complaint', validators=[DataRequired()])
    submit = SubmitField('Submit Complaint')

