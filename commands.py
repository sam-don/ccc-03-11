from main import db
from flask import Blueprint

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables Deleted")

@db_commands.cli.command("seed")
def seed_db():
    from models.Book import Book
    from faker import Faker

    faker = Faker()

    for i in range(10):
        book = Book()
        book.title = faker.catch_phrase()
        db.session.add(book)
        print(f"{i+1} book record(s) created")

    db.session.commit()
    print("Tables seeded")
