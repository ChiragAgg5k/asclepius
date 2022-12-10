import sqlite3


class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)"
        )
        self.connection.commit()
