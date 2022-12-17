import re

import customtkinter as ctk
from PIL import Image

from asclepius.centerwin import CenterWindow


class Login:
    """Class to handle the login screen."""

    def __init__(
        self,
        appearance_mode: str = "dark",
        color_theme: str = "green",
        width: int = 450,
        height: int = 350,
    ) -> None:

        self.width = width
        self.height = height

        ctk.set_appearance_mode(appearance_mode)
        ctk.set_default_color_theme(color_theme)

        self.root = ctk.CTk()
        self.root.resizable(False, False)

        # exits the program when the window is closed
        self.root.protocol("WM_DELETE_WINDOW", exit)

        # Encapsulated credentials
        self.__enrollment_id = ctk.StringVar()
        self.__password = ctk.StringVar()

        self.root.title("Ascelpius - Login")

    def display(self):
        """Display the login screen."""

        CenterWindow.center_window(self.root, self.width, self.height)

        self.bgimage = ctk.CTkImage(
            Image.open("assets/images/login_bg.png"), size=(self.width, self.height)
        )
        self.bgCTkLabel = ctk.CTkLabel(self.root, image=self.bgimage, text="")

        self.title = ctk.CTkLabel(
            self.root,
            text="Login Here!",
            font=("Arial", 20, "bold"),
            corner_radius=10,
        )

        self.enrollmentid = ctk.CTkLabel(
            self.root,
            text="Enrollment ID:",
            font=("Arial", 15, "bold"),
            corner_radius=10,
        )
        self.enrollmentid_entry = ctk.CTkEntry(
            self.root, textvariable=self.__enrollment_id, width=220
        )

        self.pswrd_CTkLabel = ctk.CTkLabel(
            self.root,
            text="Password:",
            font=("Arial", 15, "bold"),
            corner_radius=10,
        )
        self.pswrd_entry = ctk.CTkEntry(
            self.root, textvariable=self.__password, width=220, show="*"
        )

        self.submit_button = ctk.CTkButton(
            self.root,
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

        self.root.mainloop()

    def submit(self) -> bool:
        """Submit the login details.

        Returns:
            True if the details are entered, else False.
        """

        if self.__enrollment_id.get() == "" or self.__password.get() == "":
            ctk.CTkLabel(
                self.root,
                text="Please enter all the details!",
                corner_radius=10,
                font=("Arial", 15, "bold"),
            ).place(relx=0.51, rely=0.9, anchor=ctk.CENTER)

        elif not re.match(
            r"^e[1-2][0-9][a-z]{4}[0-9]{4}", self.__enrollment_id.get().lower()
        ):
            ctk.CTkLabel(
                self.root,
                text="Please enter a valid enrollment ID!",
                corner_radius=10,
                font=("Arial", 15, "bold"),
            ).place(relx=0.51, rely=0.9, anchor=ctk.CENTER)

        # !change this to check password from database
        elif len(self.__password.get()) < 8:
            ctk.CTkLabel(
                self.root,
                text="Invalid password!",
                corner_radius=10,
                font=("Arial", 15, "bold"),
            ).place(relx=0.51, rely=0.9, anchor=ctk.CENTER)

        else:
            self.root.after(1000, self.root.destroy)

            for widget in self.root.winfo_children():
                widget.destroy()

            ctk.set_appearance_mode("dark")

            ctk.CTkLabel(
                self.root,
                text="Logging in...",
                font=("Arial", 20, "bold"),
            ).place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

            return True

    def get_credentials(self) -> tuple:
        return (self.__enrollment_id.get(), self.__password.get())
