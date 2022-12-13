import customtkinter as ctk
from PIL import Image


class Login:
    # constructor
    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        self.root = ctk.CTk()
        self.root.resizable(False, False)

        self.width = 450
        self.height = 350

    def center_window(self) -> None:
        """Center the window."""

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coord = (screen_width / 2) - (self.width / 2)
        y_coord = (screen_height / 2) - (self.height / 2)
        self.root.geometry(f"{self.width}x{self.height}+{int(x_coord)}+{int(y_coord)}")

    # function for CTkLabels and entries
    def display(self):
        # declaring textvariables to store the input from user
        self.username = ctk.StringVar()
        self.password = ctk.StringVar()

        # self.root title and geometry
        self.root.title("Ascelpius - Login")
        self.center_window()

        # background image
        self.bgimage = ctk.CTkImage(
            Image.open("assets/images/login_bg.png"), size=(450, 350)
        )
        self.bgCTkLabel = ctk.CTkLabel(self.root, image=self.bgimage, text="")

        # window title
        self.title = ctk.CTkLabel(
            self.root, text="Login Here!", font=("Arial", 20, "bold"), corner_radius=10
        )

        # creating username CTkLabel and entry
        self.username_CTkLabel = ctk.CTkLabel(
            self.root, text="Name:", font=("Arial", 15, "bold"), corner_radius=10
        )
        self.username_entry = ctk.CTkEntry(
            self.root, textvariable=self.username, width=200
        )

        # creating password CTkLabel and entry
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

        self.submit_button.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)

        self.root.mainloop()

    def submit(self) -> list:
        self.root.destroy()
        return 1
