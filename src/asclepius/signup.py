import re

import customtkinter as ctk
from PIL import Image

from asclepius.database import Database


class Signup:
    """Class to create the signup screen."""

    def __init__(
        self, root, width=500, height=500, appearance_mode="light", color_theme="green"
    ) -> None:
        """Constructor for the Signup class.

        Args:
            root (ctk window/frame): where the widgets will be placed.
            width (int, optional): width of the window. Defaults to 500.
            height (int, optional): height of the window. Defaults to 500.
        """
        ctk.set_appearance_mode(appearance_mode)
        ctk.set_default_color_theme(color_theme)

        self.signup_frame = ctk.CTkFrame(root, width=width, height=height)
        self.signup_completed = False

        self.width = width
        self.height = height

        self.__name = ctk.StringVar()
        self.__enrollid = ctk.StringVar()
        self.__phoneno = ctk.StringVar()
        self.__room_no = ctk.StringVar()
        self.__is_hosteller = ctk.StringVar()
        self.__password = ctk.StringVar()

        self.text_font = ctk.CTkFont(family="Rockwell", size=20, weight="bold")
        self.small_text_font = ctk.CTkFont(family="Rockwell", size=14, weight="normal")

        self.database = Database("Signup Screen")

    def widgets(self):
        """Function to create widgets for the login screen.

        Args:
            app (ctk.Ctk()): The root window.
        """

        self.bgimage = ctk.CTkImage(
            Image.open("assets/images/login_bg.png"),
            size=(self.width, self.height + 100),
        )
        self.bgLabel = ctk.CTkLabel(self.signup_frame, image=self.bgimage, text="")
        self.bgLabel.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        self.title = ctk.CTkLabel(
            self.signup_frame, text="SignUp to Asclepius!", font=self.text_font
        ).place(relx=0.5, rely=0.05, anchor=ctk.CENTER)

        ctk.CTkLabel(
            self.signup_frame, text="Full Name*", font=self.small_text_font
        ).place(relx=0.1, rely=0.1, anchor=ctk.NW)

        self.name_entry = ctk.CTkEntry(
            self.signup_frame, textvariable=self.__name, font=self.small_text_font
        )
        self.name_entry.place(relx=0.1, rely=0.15, width=300, height=30, anchor=ctk.NW)

        ctk.CTkLabel(
            self.signup_frame,
            text="Bennett Enrollment no.*",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.25, anchor=ctk.NW)

        ctk.CTkEntry(
            self.signup_frame, textvariable=self.__enrollid, font=self.small_text_font
        ).place(relx=0.1, rely=0.3, width=300, height=30, anchor=ctk.NW)

        ctk.CTkLabel(
            self.signup_frame, text="Room Number", font=self.small_text_font
        ).place(relx=0.55, rely=0.4)
        self.room_entry = ctk.CTkEntry(
            self.signup_frame,
            textvariable=self.__room_no,
            font=self.small_text_font,
            width=30,
            fg_color="lightgrey",
        )
        self.room_entry.place(relx=0.55, rely=0.45, width=200, height=30)
        self.room_entry.configure(state=ctk.DISABLED)

        self.hostel_label = ctk.CTkLabel(
            self.signup_frame, text="Choose an Option*\n", font=self.small_text_font
        ).place(relx=0.1, rely=0.4)

        self.disableEntryRadioButton = ctk.CTkRadioButton(
            self.signup_frame,
            text="Day Scholar",
            font=self.small_text_font,
            variable=(self.__is_hosteller),
            value="0",
            command=self.disableEntry,
        )

        self.disableEntryRadioButton.place(relx=0.1, rely=0.45, anchor=ctk.NW)
        self.enableEntryRadioButton = ctk.CTkRadioButton(
            self.signup_frame,
            text="Hosteller",
            font=self.small_text_font,
            variable=(self.__is_hosteller),
            value="1",
            command=self.enableEntry,
        )
        self.enableEntryRadioButton.place(relx=0.1, rely=0.5, anchor=ctk.NW)

        ctk.CTkLabel(
            self.signup_frame,
            text="Contact Number*",
            font=self.small_text_font,
        ).place(relx=0.1, rely=0.57, anchor=ctk.NW)

        ctk.CTkEntry(
            self.signup_frame, textvariable=self.__phoneno, font=self.small_text_font
        ).place(relx=0.1, rely=0.62, width=300, height=30, anchor=ctk.NW)

        ctk.CTkLabel(
            self.signup_frame, text="Password*", font=self.small_text_font
        ).place(relx=0.1, rely=0.69, anchor=ctk.NW)
        ctk.CTkEntry(
            self.signup_frame,
            show="*",
            font=self.small_text_font,
            textvariable=self.__password,
        ).place(relx=0.1, rely=0.74, width=300, height=30, anchor=ctk.NW)

        self.register = ctk.CTkButton(
            self.signup_frame,
            text="Register",
            font=self.text_font,
            command=self.submit,
            corner_radius=10,
        ).place(relx=0.5, rely=0.87, width=150, height=40, anchor=ctk.CENTER)

    def enableEntry(self):
        self.room_entry.configure(state="normal", fg_color="white")
        self.room_entry.focus()
        self.room_entry.update()

    def disableEntry(self):
        self.room_entry.configure(state="disabled")
        self.room_entry.configure(fg_color="lightgrey")
        self.room_entry.update()

    def submit(self):
        """Function to check meet the requirements and submit the data to the database."""

        if (
            (self.__name.get() == "")
            or (self.__enrollid.get() == "")
            or (self.__phoneno.get() == "")
            or (self.__password.get() == "")
            or (self.__is_hosteller.get() == "")
        ):
            ctk.CTkLabel(
                self.signup_frame,
                text="Please fill all the fields",
                font=self.small_text_font,
            ).place(relx=0.5, rely=0.95, anchor=ctk.CENTER)

        elif not re.match(
            r"^e[1-2][0-9][a-z]{4}[0-9]{4}", self.__enrollid.get().lower()
        ):
            ctk.CTkLabel(
                self.signup_frame,
                text="Please enter a valid enrollment ID!",
                corner_radius=10,
                font=self.small_text_font,
            ).place(relx=0.5, rely=0.95, anchor=ctk.CENTER)

        elif not self.database.signup(self.get_credentials()):
            ctk.CTkLabel(
                self.signup_frame, text="User already exists", font=self.small_text_font
            ).place(relx=0.5, rely=0.95, anchor=ctk.CENTER)

        else:
            self.signup_frame.after(1000, self.signin_delay)

            ctk.set_appearance_mode("dark")

            for widget in self.signup_frame.winfo_children():
                widget.destroy()

            ctk.CTkLabel(
                self.signup_frame, text="Signing In...", font=self.text_font
            ).pack(pady=40, padx=50, fill=ctk.BOTH, expand=True)

    def signin_delay(self):
        """Loading screen for 1 second before redirecting to the dashboard page."""
        self.signup_completed = True

    def get_credentials(self) -> tuple:
        """Returns the signup information"""

        return (
            self.__name.get(),
            self.__enrollid.get().upper(),
            self.__phoneno.get(),
            self.__room_no.get(),
            self.__is_hosteller.get(),
            self.__password.get(),
        )

    def return_signup_frame(self) -> ctk.CTkFrame:
        """Show the signupwindow"""
        self.widgets()

        return self.signup_frame
