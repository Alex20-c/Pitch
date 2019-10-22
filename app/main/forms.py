from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField,SubmitField
from wtforms.validators import Required


class CategoryForm(FlaskForm):
    """
    class to create a form to create category
    """
    name =  SubmitField('Pitch category',validators=[Required()])
    sybmit = SubmitField('Create')

class PitchForm(FlaskForm):
    """
    class to create form to write pitch
    """
    pitch = SubmitField('Pitch Content', validators=[Required()])
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    """
    class to create form to comment on a pitch
    """
    comment = StringField('Comment Content', validators=[Required()])
    submit =  SubmitField('Submit')