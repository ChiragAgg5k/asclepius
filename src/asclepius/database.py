"""Database module for Asclepius."""
import sqlite3


class Database:
    """Database class for Asclepius."""

    def __init__(self, module_name: str = "Not Provided") -> None:
        """Initialize the database connection and cursor."""
        try:
            self.connection = sqlite3.connect("src/data/asclepius.db")
            self.cursor = self.connection.cursor()
            print("Database connection successful -", module_name)

        except sqlite3.OperationalError as error:
            print("Error: ", error)

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

    def signup(self, credentials: tuple) -> bool:
        """Add a new user to the database.

        Args:
            credentials (tuple): User credentials

        Returns:
            bool: True if signup successful, False otherwise
        """

        username = credentials[0]
        enrollid = credentials[1]
        contact = credentials[2]
        roomno = credentials[3]
        hosteller = credentials[4]
        password = credentials[5]

        try:
            self.cursor.execute(
                "INSERT INTO credentials VALUES (?, ?, ?, ?, ?,?)",
                (enrollid, username, hosteller, roomno, contact, password),
            )
            self.connection.commit()

            print("Signup successful")
            return True

        except sqlite3.IntegrityError:

            print("Error: Enrollment ID already exists")
            return False

    def get_signupdetails(self, enrollment_id: str) -> list:
        """Get the signup details of the user.

        Args:
            enrollment_id (str): Enrollment ID of the user

        Returns:
            list: Signup details
        """
        self.cursor.execute(
            "SELECT * FROM credentials WHERE enrollid = (?)",
            (enrollment_id.upper(),),
        )
        return self.cursor.fetchone()

    def login(self, credentials: tuple) -> bool:
        """Verify the login credentials of the user.

        Args:
            credentials (tuple): [Enrollment ID, Password]

        Returns:
            bool: True if credentials are correct, False otherwise
        """
        self.cursor.execute(
            "SELECT * FROM credentials WHERE enrollid = (?)",
            (credentials[0].upper(),),
        )

        fetched = self.cursor.fetchone()

        if fetched:

            if fetched[5] == credentials[1]:
                print("Login Credentials verified")
                return True

            print("Wrong password entered")

        print("Wrong enrollment ID entered")
        return False

    def get_medicine_record(self, enrollment_id) -> list:
        """Get the medicine record from the database.

        Returns:
            list: Medicine record
        """
        self.cursor.execute(
            "SELECT * FROM MRECORD WHERE enrollid = (?)", (enrollment_id,)
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
        """Add orders to the database.

        Args:
            mid_list (list): List of medicine IDs
            enrollment_id (str): Enrollment ID of the user
        """

        for mid in mid_list:
            self.cursor.execute(
                "INSERT INTO MRECORD (enrollid ,MID) VALUES (?, ?)",
                (
                    enrollment_id,
                    mid,
                ),
            )

        print(f"{len(mid_list)} orders added to the database")
        self.connection.commit()
