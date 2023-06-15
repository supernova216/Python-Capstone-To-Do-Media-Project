import os, model, server

os.system("dropdb fun")
os.system("createdb fun")

model.connect_to_db(server.app)

with server.app.app_context():
    model.db.create_all()

    new_user = model.User(email = "nathanharris91@gmail.com", password = "something")
    new_movie = model.Movie(movie_title = "Guardians of the Galaxy 3", user_id = "1")
    new_book = model.Book(book_title = "Gunmetal Gods", user_id = "1")
    new_game = model.Game(game_title = "Metroid Prime Remastered", user_id = "1")

    model.db.session.add(new_user)
    model.db.session.add(new_movie)
    model.db.session.add(new_book)
    model.db.session.add(new_game)
    model.db.session.commit()
