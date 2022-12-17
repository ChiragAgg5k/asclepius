from login_screen import Login
from signup import Signup
import customtkinter as ctk
from PIL import Image


class Open_window:

    # constructor
    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        self.root = ctk.CTk()
        self.root.resizable(False, False)
        self.center_window()
        self.display()

        self.width = 500
        self.height = 500
        



    def center_window(self,) -> None:
        """Center the window."""

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coord = (screen_width / 2) - (self.width / 2)
        y_coord = (screen_height / 2) - (self.height / 2)
        self.root.geometry(f"{self.width}x{self.height}+{int(x_coord)}+{int(y_coord)}")

    def display(self) -> None:
        
        # self.root title and geometry
        self.root.title("Welcome")
        self.center_window()

        # background image
        self.bgimage = ctk.CTkImage(
            Image.open("assets/images/login_bg.png"), size=(450, 350)
        )
        self.bgCTkLabel = ctk.CTkLabel(self.root, image=self.bgimage, text="")

        self.login_button = ctk.CTkButton(
                self.root,
                text="Login",
                font=("Arial", 20, "bold"),
                width=150,
                height=40,
                corner_radius=10,
                
            ).pack(padx= 50, pady= 30)

        self.signup_button = ctk.CTkButton(
                self.root,
                text="Signup",
                font=("Arial", 20, "bold"),
                width=150,
                height=40,
                corner_radius=10,
                command=lambda: self.signup(),
            ).pack(padx= 50, pady= 60)

        self.root.mainloop()
