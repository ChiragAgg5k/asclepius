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
        appearance_mode: str = "light",
        color_theme: str = "green",
    ) -> None:

        self.width = width
        self.height = height

        self.root = ctk.CTk()
        self.root.resizable(False, False)
        CenterWindow.center_window(self.root, self.width, self.height)

        ctk.set_appearance_mode(appearance_mode)
        ctk.set_default_color_theme(color_theme)

        # exits the program when the window is closed by the user
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

        self.root.title("Ascelpius - Home")

        self.selected_tab = ""
        self.__user_enrollment_id = ""

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

            if login_object.login_completed:
                print("User logged in successfully.")
                self.__user_enrollment_id = login_object.get_credentials()[0]
                self.root.destroy()
                break

            elif signup_object.signup_completed:
                print("User signed up successfully.")
                self.__user_enrollment_id = signup_object.get_credentials()[1]
                self.root.destroy()
                break

        self.root.mainloop()

    def get_user_enrollment_id(self) -> str:
        """Return the enrollment id of the user."""
        return self.__user_enrollment_id.upper()

    def show_homescreen(self) -> None:
        """Show the homescreenwindow"""
        self.homescreen()
