import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)

    movie = db.relationship("Movie", backref = "users")
    game = db.relationship("Game", backref = "users")
    book = db.relationship("Book", backref = "users")
    
    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"

class Movie(db.Model):

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    movie_title = db.Column(db.String, unique = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable = False)

    def __repr__(self):
        return f"<Movie movie_id={self.movie_id} movie_title={self.movie_title}>"
    
class Book(db.Model):

    __tablename__ = "books"

    book_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    book_title = db.Column(db.String, unique = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable = False)

    def __repr__(self):
        return f"<Book book_id={self.book_id} book_title={self.book_title}"

class Game(db.Model):

    __tablename__ = "games"

    game_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    game_title = db.Column(db.String, unique = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable = False)

    def __repr__(self):
        return f"<Game game_id={self.game_id} game_title={self.game_title}"

def connect_to_db(flask_app, db_uri=os.environ["POSTGRES_URI"], echo = False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db")

if __name__ == "__main__":
    from server import app

    connect_to_db(app)
