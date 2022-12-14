import re

import customtkinter as ctk
from PIL import Image


class Login:
    # constructor
    def __init__(
        self,
        appearance_mode: str = "dark",
        color_theme: str = "green",
        width: int = 450,
        height: int = 350,
    ) -> None:

        self.width = width
        self.height = height
        self.appearance_mode = appearance_mode
        self.color_theme = color_theme

    def center_window(self) -> None:
        """Centers the window."""

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coord = (screen_width / 2) - (self.width / 2)
        y_coord = (screen_height / 2) - (self.height / 2)
        self.root.geometry(f"{self.width}x{self.height}+{int(x_coord)}+{int(y_coord)}")

    def display(self):
        """Display the login screen."""

        ctk.set_appearance_mode(self.appearance_mode)
        ctk.set_default_color_theme(self.color_theme)

        self.root = ctk.CTk()
        self.root.resizable(False, False)

        self.enrollment_id = ctk.StringVar()
        self.password = ctk.StringVar()

        self.root.title("Ascelpius - Login")
        self.center_window()

        self.bgimage = ctk.CTkImage(
            Image.open("assets/images/login_bg.png"), size=(450, 350)
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
            self.root, textvariable=self.enrollment_id, width=220
        )

        self.pswrd_CTkLabel = ctk.CTkLabel(
            self.root,
            text="Password:",
            font=("Arial", 15, "bold"),
            corner_radius=10,
        )
        self.pswrd_entry = ctk.CTkEntry(
            self.root, textvariable=self.password, width=220, show="*"
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

        if self.enrollment_id.get() == "" or self.password.get() == "":
            ctk.CTkLabel(
                self.root,
                text="Please enter all the details!",
                corner_radius=10,
                font=("Arial", 15, "bold"),
            ).place(relx=0.51, rely=0.9, anchor=ctk.CENTER)

        elif not re.match(r"^e[1-2][0-9][a-z]{4}[0-9]{4}", self.enrollment_id.get()):
            ctk.CTkLabel(
                self.root,
                text="Please enter a valid enrollment ID!",
                corner_radius=10,
                font=("Arial", 15, "bold"),
            ).place(relx=0.51, rely=0.9, anchor=ctk.CENTER)

        else:
            self.root.destroy()
            return True
