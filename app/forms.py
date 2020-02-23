from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from app.models import Note

class NoteForm(FlaskForm):
    content = TextAreaField('Note:', validators=[DataRequired(),
                            Length(min=1, max=100)])
    submit = SubmitField('Submit')