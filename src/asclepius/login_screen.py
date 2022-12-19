import re

import customtkinter as ctk
from PIL import Image

from asclepius.database import Database


class Login:
    """Class to handle the login screen."""

    def __init__(
        self,
        appearance_mode: str = "light",
        color_theme: str = "green",
        width: int = 500,
        height: int = 500,
        root=None,
    ) -> None:
        """Initialize the login screen.

        Args:
            appearance_mode (str, optional): Determines appearance. Defaults to "light".
            color_theme (str, optional): Determines accent color. Defaults to "green".
            width (int, optional): Sets width of the window. Defaults to 500.
            height (int, optional): Sets height of the window. Defaults to 500.
            root (_type_, optional): Tkinter window where the widgets need to be placed. Defaults to None.
        """

        self.width = width
        self.height = height

        ctk.set_appearance_mode(appearance_mode)
        ctk.set_default_color_theme(color_theme)
        self.login_frame = ctk.CTkFrame(root, width=self.width, height=self.height)

        self.__enrollment_id = ctk.StringVar()
        self.__password = ctk.StringVar()

        self.login_completed = False

        self.db = Database("Login Screen")

    def display(self):
        """Display the login screen."""

        self.bgimage = ctk.CTkImage(
            Image.open("assets/images/login_bg.png"), size=(self.width, self.height)
        )
        self.bgCTkLabel = ctk.CTkLabel(self.login_frame, image=self.bgimage, text="")

        self.title = ctk.CTkLabel(
            self.login_frame,
            text="Login Here!",
            font=("Arial", 20, "bold"),
            corner_radius=10,
        )

        self.enrollmentid = ctk.CTkLabel(
            self.login_frame,
            text="Enrollment ID:",
            font=("Arial", 15, "bold"),
            corner_radius=10,
        )
        self.enrollmentid_entry = ctk.CTkEntry(
            self.login_frame, textvariable=self.__enrollment_id, width=220
        )

        self.pswrd_CTkLabel = ctk.CTkLabel(
            self.login_frame,
            text="Password:",
            font=("Arial", 15, "bold"),
            corner_radius=10,
        )
        self.pswrd_entry = ctk.CTkEntry(
            self.login_frame, textvariable=self.__password, width=220, show="*"
        )

        self.submit_button = ctk.CTkButton(
            self.login_frame,
            text="Submit",
            font=("Arial", 20, "bold"),
            width=150,
            height=40,
            corner_radius=10,
            command=self.submit,
        )

        self.enrollmentid_entry.bind("<Return>", lambda event: self.submit())
        self.pswrd_entry.bind("<Return>", lambda event: self.submit())

        self.bgCTkLabel.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.title.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

        self.enrollmentid_entry.place(relx=0.6, rely=0.4, anchor=ctk.CENTER)
        self.enrollmentid.place(relx=0.2, rely=0.4, anchor=ctk.CENTER)

        self.pswrd_entry.place(relx=0.6, rely=0.55, anchor=ctk.CENTER)
        self.pswrd_CTkLabel.place(relx=0.2, rely=0.55, anchor=ctk.CENTER)

        self.submit_button.place(relx=0.5, rely=0.75, anchor=ctk.CENTER)

    def submit(self) -> bool:
        """Submit the login details.

        Returns:
            True if the details are entered, else False.
        """

        if self.__enrollment_id.get() == "" or self.__password.get() == "":
            ctk.CTkLabel(
                self.login_frame,
                text="Please enter all the details!",
                corner_radius=10,
                font=("Arial", 15, "bold"),
            ).place(relx=0.51, rely=0.9, anchor=ctk.CENTER)

        elif not re.match(
            r"^e[1-2][0-9][a-z]{4}[0-9]{4}", self.__enrollment_id.get().lower()
        ):
            ctk.CTkLabel(
                self.login_frame,
                text="Please enter a valid enrollment ID!",
                corner_radius=10,
                font=("Arial", 15, "bold"),
            ).place(relx=0.51, rely=0.9, anchor=ctk.CENTER)

        elif not (self.db.login(self.get_credentials())):
            ctk.CTkLabel(
                self.login_frame,
                text="Invalid credentials!",
                corner_radius=10,
                font=("Arial", 15, "bold"),
            ).place(relx=0.51, rely=0.9, anchor=ctk.CENTER)

        else:
            self.login_frame.after(1000, self.login_delay)

            for widget in self.login_frame.winfo_children():
                widget.destroy()

            ctk.set_appearance_mode("dark")

            ctk.CTkLabel(
                self.login_frame, text="Logging in...", font=("Arial", 20, "bold")
            ).place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    def login_delay(self):
        """Delay the login screen."""
        self.login_completed = True

    def get_credentials(self) -> tuple:
        """Get the credentials entered by the user.

        Returns:
            tuple: The enrollment ID and password entered by the user.
        """
        return (self.__enrollment_id.get(), self.__password.get())

    def return_login_frame(self) -> ctk.CTkFrame:
        """Return the login frame."""
        return self.login_frame
