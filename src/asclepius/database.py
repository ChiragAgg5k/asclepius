import sqlite3


class Database:
    """Database class for Asclepius."""

    def __init__(self) -> None:
        try:
            self.connection = sqlite3.connect("src/data/asclepius.db")
            self.cursor = self.connection.cursor()

            print("Database connected successfully")
        except sqlite3.OperationalError as e:

            print("Database not found, Error: ", e)
            print("check if the database exists in the data folder")

    def get_medicines(self) -> list:
        """Get a medicine from the database.

        Returns:
            list: All Medicine details
        """
        self.cursor.execute("SELECT * FROM medicines")
        return self.cursor.fetchall()

    def get_col_headings(self, table_name: str) -> list:
        """Get the column headings of the medicines table.

        Args:
            table_name: Name of the table

        Returns:
            list: Column headings
        """

        self.cursor.execute(f"SELECT * FROM {table_name}")
        return [description[0] for description in self.cursor.description]

    def signup(
        self,
        Enrollid: str,
        username: str,
        Hosteller: int,
        roomno: str,
        contact: int,
    ) -> None:

        self.cursor.execute(
            "INSERT INTO credentials VALUES (?, ?, ?, ?, ?)",
            (Enrollid, username, Hosteller, roomno, contact),
        )
        self.connection.commit()

        def get_signupdetails(self) -> list:
            self.cursor.execute("SELECT * FROM signup")
            return self.cursor.fetchall()

    def login(self):
        statement = "SELECT username, password FROM credentials"
        self.cursor.execute(statement)
        username = ""
        password = ""
        statement1 = f"SELECT username from credentials WHERE username='{username}' AND Password = '{password}';"
        self.cursor.execute(statement1)
        if not self.cursor.fetchone():
            print("Login failed")
        else:
            print("Welcome")

    def get_medicine_record(self) -> list:
        """Get the medicine record from the database.

        Returns:
            list: Medicine record
        """
        self.cursor.execute("SELECT * FROM MRECORD")
        return self.cursor.fetchall()

    def add_orders(self, mid_list: list) -> None:

        all_medicines = self.get_medicines()
        for i in mid_list:
            for j in all_medicines:
                if i == j[0]:
                    self.cursor.execute(
                        "INSERT INTO MRECORD(ENROLLID,MID,NAME,PRICE) VALUES (' ',?, ?, ?)",
                        (j[0], j[1], j[4]),
                    )
                    self.connection.commit()
        self.connection.commit()
