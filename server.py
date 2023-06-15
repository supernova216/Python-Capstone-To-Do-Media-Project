from flask import Flask, render_template, request, flash, session, redirect, url_for
from model import connect_to_db, db, Movie, Game, Book
from forms import MovieForm, BookForm, GameForm
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def login():
    return render_template('homepage.html')

@app.route("/users", methods=["POST"])
def register_user():
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created. Please log in.")

    return redirect("/")

@app.route("/login", methods = ["POST"])
def check_login():
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("Email or password is incorrect")
    else:
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return redirect("/")

@app.route("/movies")
def show_movies():
    if not "user_email" in session:
        flash(f"Please log in!")
        return redirect(url_for("login"))
    
    movie_form = MovieForm()
    user = crud.get_user_by_email(session["user_email"])
    movies = crud.get_movies(user.user_id)
    return render_template("movies.html", movies = movies, movie_form = movie_form)

@app.route("/add_movie", methods = ["POST"])
def add_movie():
    movie_form = MovieForm()
    movie_title = movie_form.movie_title.data
    user = crud.get_user_by_email(session["user_email"])
    user_id = user.user_id
    new_movie = Movie(movie_title = movie_title, user_id = user_id)
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("show_movies"))
    
@app.route("/update_movie/<movie_id>", methods=["GET","POST"])
def update_movie(movie_id):
    form = MovieForm()
    movie = Movie.query.get(movie_id)
    if request.method == "POST":
        movie.movie_title = form.movie_title.data
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for("show_movies"))
    else:
        return render_template("update_movie.html", movie = movie, form = form)

@app.route("/delete_movie/<movie_id>",methods = ["GET", "DELETE"]) 
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("show_movies"))

@app.route("/books")
def show_books():
    if not "user_email" in session:
        flash(f"Please log in!")
        return redirect(url_for("login"))
    book_form = BookForm()
    user = crud.get_user_by_email(session["user_email"])
    books = crud.get_books(user.user_id)
    return render_template("books.html", books = books, book_form = book_form)

@app.route("/add_book", methods = ["POST"])
def add_book():
    book_form = BookForm()
    book_title = book_form.book_title.data
    user = crud.get_user_by_email(session["user_email"])
    user_id = user.user_id
    new_book = Book(book_title = book_title, user_id = user_id)
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for("show_books"))

@app.route("/update_book/<book_id>", methods=["GET","POST"])
def update_book(book_id):
    form = BookForm()
    book = Book.query.get(book_id)
    if request.method == "POST":
        book.book_title = form.book_title.data
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("show_books"))
    else:
        return render_template("update_book.html", book = book, form = form)

@app.route("/delete_book/<book_id>",methods = ["GET", "DELETE"]) 
def delete_book(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("show_books"))

@app.route("/games")
def show_games():
    if not "user_email" in session:
        flash(f"Please log in!")
        return redirect(url_for("login"))
    game_form = GameForm()
    user = crud.get_user_by_email(session["user_email"])
    games = crud.get_games(user.user_id)
    return render_template("games.html", games = games, game_form = game_form)

@app.route("/add_game", methods = ["POST"])
def add_game():
    game_form = GameForm()
    game_title = game_form.game_title.data
    user = crud.get_user_by_email(session["user_email"])
    user_id = user.user_id
    new_game = Game(game_title = game_title, user_id = user_id)
    db.session.add(new_game)
    db.session.commit()
    return redirect(url_for("show_games"))

@app.route("/update_game/<game_id>", methods=["GET","POST"])
def update_game(game_id):
    form = GameForm()
    game = Game.query.get(game_id)
    if request.method == "POST":
        game.game_title = form.game_title.data
        db.session.add(game)
        db.session.commit()
        return redirect(url_for("show_games"))
    else:
        return render_template("update_game.html", game = game, form = form)
        
@app.route("/delete_game/<game_id>",methods = ["GET", "DELETE"]) 
def delete_game(game_id):
    game = Game.query.get(game_id)
    db.session.delete(game)
    db.session.commit()
    return redirect(url_for("show_games"))

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host = "0.0.0.0", debug = True)

