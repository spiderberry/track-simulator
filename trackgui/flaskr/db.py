import sqlite3
import random
from faker import Faker

import click
from flask import current_app, g

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types = sqlite3.PARSE_DECLTYPES
        )

        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e = None):
    db = g.pop("db", None)

    if db is not None:
        db.close()

def init_db():

    db = get_db()

    with current_app.open_resource("schema2.sql") as f:
        db.executescript(f.read().decode("utf8"))

def populate_db():
    fake = Faker()
    db = get_db()
    cursor = db.cursor()
    insert_stmt = (
            "INSERT INTO Athletes(first_name, last_name, age, acceleration, endurance, form, mental, speed, start)"
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        )

    for i in range(99):
        data = (fake.unique.first_name_male(), fake.unique.last_name(), random.randint(16,30), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
        cursor.execute(insert_stmt, data)
        db.commit()

@click.command("init-db")
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")

@click.command("populate-db")
def populate_db_command():
    """Populate the database with 99 random athletes."""
    populate_db()
    click.echo("Populated the database with 99 random athletes.")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(populate_db_command)