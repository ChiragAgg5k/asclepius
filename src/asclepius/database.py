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

    def add_medicine(
        self, Mid: int, name: str, description: str, dosage: int, availability: str
    ) -> None:
        """Add a medicine to the database.

        Args:
            Mid (int): Medicine ID
            name (str): Name of the medicine
            description (str): Short description of the medicine
            dosage (int): recommended dosage of the medicine
            availability (bool): Is the medicine available?

        Returns:
            None
        """

        self.cursor.execute(
            "INSERT INTO medicines VALUES (?, ?, ?, ?, ?)",
            (Mid, name, description, dosage, availability),
        )
        self.connection.commit()

    def get_medicine(self, Mid: int) -> tuple:
        """Get a medicine from the database.

        Args:
            Mid (int): Medicine ID

        Returns:
            tuple: Medicine details
        """
        self.cursor.execute("SELECT * FROM medicines WHERE Mid = ?", (Mid,))
        return self.cursor.fetchone()
