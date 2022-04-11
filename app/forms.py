from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired, InputRequired
from flask_wtf.file import FileAllowed
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired()])
    photo=FileField(validators=[FileRequired(), FileAllowed(['png', 'jpg', 'jpeg','PNG', 'JPEG', 'JPG', 'jng', 'JNG', 'gif', 'GIF'])])