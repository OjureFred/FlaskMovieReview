from typing_extensions import Required
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ReviewForm(FlaskForm):
    title = StringField('Review Title', validators=[Required])
    review = TextAreaField('MovieReview', validators=[Required])
    submit = SubmitField('Submit')
