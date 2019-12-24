 from flask_wtf import FlaskForm
 from wtforms import StringField,PasswordField,SubmitField
 from wtforms.validators import DataRequired,Email,EqualTo
 from wtforms import ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField("Log In")


class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',"passwords are not matching plese try again !")])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email id has been already taken ')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your Email Id has already been taken !')

        