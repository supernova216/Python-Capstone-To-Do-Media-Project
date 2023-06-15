from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class MovieForm(FlaskForm):
    movie_title = StringField('movie title', validators = [DataRequired(), Length(min = 1, max = 255)])
    submit = SubmitField("submit")

class BookForm(FlaskForm):
    book_title = StringField('book title', validators = [DataRequired(), Length(min = 1, max = 255)])
    submit = SubmitField("submit")

class GameForm(FlaskForm):
    game_title = StringField('game title', validators = [DataRequired(), Length(min = 1, max = 255)])
    submit= SubmitField("submit")