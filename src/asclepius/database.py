import sqlite3


class Database:
    """Database class for Asclepius."""

    def __init__(self) -> None:
        """Initialize the database connection and cursor."""
        try:
            self.connection = sqlite3.connect("src/data/asclepius.db")
            self.cursor = self.connection.cursor()
            print("Database connection successful")

        except sqlite3.OperationalError as e:
            print("Error: ", e)

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

        username = credentials[0]
        Enrollid = credentials[1]
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

            print("Signup successful")
            return True

        except sqlite3.IntegrityError:

            print("Error: Enrollment ID already exists")
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

        fetched = self.cursor.fetchone()

        if fetched:

            if fetched[5] == credentials[1]:
                print("Credentials verified")
                return True

            else:
                print("Wrong password entered")

        print("Wrong enrollment ID entered")
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

    def get_medicine_details(self, mid: str) -> list:
        """Get the medicine details from the database.

        Returns:
            list: Medicine details
        """
        self.cursor.execute("SELECT * FROM medicines WHERE MID = (?)", (mid,))
        return self.cursor.fetchone()

    def add_orders(self, mid_list: list, enrollment_id: str) -> None:

        for mid in mid_list:
            self.cursor.execute(
                "INSERT INTO MRECORD (ENROLLID ,MID) VALUES (?, ?)",
                (
                    enrollment_id,
                    mid,
                ),
            )

        print(f"{len(mid_list)} orders added to the database)")
        self.connection.commit()
