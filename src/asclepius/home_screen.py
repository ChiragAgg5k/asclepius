import login_screen, signup
import customtkinter as ctk
from PIL import Image
from centerwin import CenterWindow

class HomeScreen:

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

        self.root.title("Ascelpius - Home")

    def homescreen(self):
        """Display the homescreen."""

        CenterWindow.center_window(self.root, self.width, self.height)

        self.bgimage = ctk.CTkImage(
            Image.open("assets/images/login_bg.png"), size=(self.width, self.height)
        )
        self.bgCTkLabel = ctk.CTkLabel(self.root, image=self.bgimage, text="")

        self.title = ctk.CTkLabel(
            self.root,
            text="Welcome!!!",
            font=("Arial", 20, "bold"),
            corner_radius=10,
        )

        self.login_button = ctk.CTkButton(
                self.root,
                text="Login",
                font=("Arial", 20, "bold"),
                width=150,
                height=40,
                corner_radius=10,
                command= self.login
            ).pack(padx= 50, pady= 30)

        self.signup_button = ctk.CTkButton(
                self.root,
                text="Signup",
                font=("Arial", 20, "bold"),
                width=150,
                height=40,
                corner_radius=10,
                command=self.signup,
            ).pack(padx= 50, pady= 60)

    def login(self):
        displayLogin= login_screen.Login()
        displayLogin.display()

    def signup(self):
        signup_screen= signup.Signup()
        signup_screen.widgets()

    def show_homescreen(self) -> None:
        """Show the homescreenwindow"""
        self.homescreen()

        CenterWindow.center_window(self.root, self.width, self.height)
        self.root.mainloop()
