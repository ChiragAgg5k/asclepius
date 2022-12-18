import sqlite3


class Database:
    """Database class for Asclepius."""

    def __init__(self) -> None:
        try:
            self.connection = sqlite3.connect("src/data/asclepius.db")
            self.cursor = self.connection.cursor()

        except sqlite3.OperationalError as e:
            pass

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

    def signup(self, credentials: tuple) -> None:

        Enrollid = credentials[0]
        username = credentials[1]
        contact = credentials[2]
        roomno = credentials[3]
        Hosteller = credentials[4]
        password = credentials[5]

        try:
            self.cursor.execute(
                "INSERT INTO credentials VALUES (?, ?, ?, ?, ?,?)",
                (Enrollid, username, Hosteller, roomno, contact, password),
            )
            self.connection.commit()
            return True

        except sqlite3.IntegrityError:
            return False

    def get_signupdetails(self, enrollment_id) -> list:
        self.cursor.execute(
            "SELECT * FROM credentials WHERE ENROLLID = (?)", (enrollment_id,)
        )
        return self.cursor.fetchone()

    def login(self, credentials: tuple) -> bool:
        self.cursor.execute(
            "SELECT * FROM credentials WHERE ENROLLID = (?)", (credentials[0],)
        )
        if self.cursor.fetchone():
            return True
        return False

    def get_medicine_record(self, enrollment_id) -> list:
        """Get the medicine record from the database.

        Returns:
            list: Medicine record
        """
        self.cursor.execute(
            "SELECT * FROM MRECORD WHERE ENROLLID = (?)", (enrollment_id,)
        )
        return self.cursor.fetchall()

    def add_orders(self, mid_list: list, enrollment_id: str) -> None:

        all_medicines = self.get_medicines()
        for i in mid_list:
            for j in all_medicines:
                if i == j[0]:
                    self.cursor.execute(
                        "INSERT INTO MRECORD(ENROLLID,MID,NAME,PRICE) VALUES (? , ?, ?, ?)",
                        (
                            enrollment_id,
                            j[0],
                            j[1],
                            j[4],
                        ),
                    )
                    self.connection.commit()

        self.connection.commit()
