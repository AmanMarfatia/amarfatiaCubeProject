import sqlite3
from typing import Tuple


class Users:
    pass


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect('/Users/amanmarfatia/PycharmProjects/amarfatiaCubeProject/database.sqlite3')  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def create_entries_table(cursor: sqlite3.Cursor):
    create_statement = """Insert INTO 'database'(
    entryID INTEGER PRIMARY KEY,
    prefix TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    logo TEXT,
    team_name TEXT,
    email TEXT,
    jersey_color TEXT,
    phone_number TEXT,
    coach TEXT,
    head_coach TEXT,
    waterboys TEXT,
    doctor TEXT,
    eighteen_thru_twentyfive TEXT,
    twentyfive_thru_thirty TEXT,
    thirty_thru_forty TEXT,
    forty_thru_fifty TEXT,
    created_date TEXT,
    created_by TEXT);"""
    cursor.execute(create_statement)


def add_entries_to_db(cursor: sqlite3.Cursor, entries_data: list[dict]):
    # the insert or ignore syntax will insert if the primary key isn't in use or ignore if the primary key is in the DB
    insertStatement = """INSERT OR IGNORE INTO WuFooData (entryID, prefix, first_name, last_name, logo, team_name, email, jersey_color,
    phone_number, coach, head_coach, waterboys, doctor, eighteen_thru_twentyfive, twentyfive_thru_thirty, thirty_thru_forty, forty_thru_fifty,
     created_date, created_by) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
    for entry in entries_data:
        entry_values = list(
            entry.values()
        )  # get the list of values from the dictionary
        entry_values[0] = int(
            entry_values[0]
        )  # the EntryID is a string, but I want it to be a number
        entry_values = entry_values[:-2]
        cursor.execute(insertStatement, entry_values)
