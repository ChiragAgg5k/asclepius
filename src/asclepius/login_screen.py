import customtkinter as ctk
from PIL import Image


class Login:
    # constructor
    def __init__(
        self,
        appearance_mode: str = "light",
        color_theme: str = "green",
        width: int = 450,
        height: int = 350,
    ) -> None:

        ctk.set_appearance_mode(appearance_mode)
        ctk.set_default_color_theme(color_theme)

        self.root = ctk.CTk()
        self.root.resizable(False, False)

        self.width = width
        self.height = height

        self.username = ctk.StringVar()
        self.password = ctk.StringVar()

    def center_window(self) -> None:
        """Center the window."""

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coord = (screen_width / 2) - (self.width / 2)
        y_coord = (screen_height / 2) - (self.height / 2)
        self.root.geometry(f"{self.width}x{self.height}+{int(x_coord)}+{int(y_coord)}")

    def display(self):
        """Display the login screen."""

        self.root.title("Ascelpius - Login")
        self.center_window()

        self.bgimage = ctk.CTkImage(
            Image.open("assets/images/login_bg.png"), size=(450, 350)
        )
        self.bgCTkLabel = ctk.CTkLabel(self.root, image=self.bgimage, text="")

        self.title = ctk.CTkLabel(
            self.root, text="Login Here!", font=("Arial", 20, "bold"), corner_radius=10
        )

        self.username_CTkLabel = ctk.CTkLabel(
            self.root, text="Name:", font=("Arial", 15, "bold"), corner_radius=10
        )
        self.username_entry = ctk.CTkEntry(
            self.root, textvariable=self.username, width=200
        )

        self.pswrd_CTkLabel = ctk.CTkLabel(
            self.root,
            text="Password:",
            font=("Arial", 15, "bold"),
            corner_radius=10,
        )
        self.pswrd_entry = ctk.CTkEntry(
            self.root, textvariable=self.password, width=200, show="*"
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

        self.bgCTkLabel.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.title.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

        self.username_entry.place(relx=0.6, rely=0.4, anchor=ctk.CENTER)
        self.username_CTkLabel.place(relx=0.2, rely=0.4, anchor=ctk.CENTER)

        self.pswrd_entry.place(relx=0.6, rely=0.55, anchor=ctk.CENTER)
        self.pswrd_CTkLabel.place(relx=0.2, rely=0.55, anchor=ctk.CENTER)

        self.submit_button.place(relx=0.5, rely=0.75, anchor=ctk.CENTER)

        self.root.mainloop()

    def submit(self) -> list:
        """Submit the login details.

        Returns:
            list[str,str]: A list containing the username and password.
        """

        if self.username.get() == "" or self.password.get() == "":
            ctk.CTkLabel(
                self.root,
                text="Please enter all the details!",
                corner_radius=10,
                font=("Arial", 15, "bold"),
            ).place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

        else:
            self.root.destroy()
            return True
