from model import db, User, Movie, Game, Book, connect_to_db

def create_user(email, password):  
    new_user = User(email=email, password=password)

    return new_user

def get_movies(user_id):
    return Movie.query.filter_by(user_id = user_id).all()

def get_books(user_id):
    return Book.query.filter_by(user_id = user_id).all()

def get_games(user_id):
    return Game.query.filter_by(user_id = user_id).all()

def get_user_by_email(email):
    return User.query.filter(User.email == email).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)