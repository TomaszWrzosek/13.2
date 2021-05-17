from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    description = StringField('Opis', validators=[DataRequired()])
    done = BooleanField('Wykonane?')
    new_task = StringField('Nowe zadanie', validators=[DataRequired()])
   