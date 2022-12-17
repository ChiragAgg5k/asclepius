import customtkinter as ctk
from PIL import Image

from asclepius.centerwin import CenterWindow
from asclepius.database import Database
from asclepius.login_screen import Login
from asclepius.signup import Signup


class HomeScreen:
    def __init__(
        self,
        width: int = 500,
        height: int = 500,
    ) -> None:

        self.width = width
        self.height = height

        self.root = ctk.CTk()
        self.root.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        # exits the program when the window is closed
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

        self.root.title("Ascelpius - Home")
        self.selected_tab = ""

        self.db = Database()

    def homescreen(self):
        """Display the homescreen."""

        CenterWindow.center_window(self.root, self.width, self.height)

        self.tabview = ctk.CTkTabview(self.root, width=200, corner_radius=10)
        self.tabview.add("Login")
        self.tabview.add("Signup")
        self.tabview.pack(fill="both", expand=True, anchor=ctk.CENTER)

        login_object = Login(
            color_theme="green",
            root=self.tabview.tab("Login"),
            width=self.width,
            height=self.height,
        )
        login_tab_frame = login_object.return_login_frame()
        login_tab_frame.pack(fill="both", expand=True, anchor=ctk.CENTER)

        signup_object = Signup(root=self.tabview.tab("Signup"))
        signup_tab_frame = signup_object.return_signup_frame()
        signup_tab_frame.pack(fill="both", expand=True, anchor=ctk.CENTER)

        login_object.display()

        while True:

            self.root.update()

            if login_object.login_completed or signup_object.signup_completed:
                self.root.destroy()
                break

    def show_homescreen(self) -> None:
        """Show the homescreenwindow"""
        CenterWindow.center_window(self.root, self.width, self.height)
        self.homescreen()
