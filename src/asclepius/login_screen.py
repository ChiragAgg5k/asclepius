from tkinter import *

import customtkinter as ctk
from PIL import Image


class LoginScreen:
    def __init__(self, appearance: str, color_theme: str) -> None:

        ctk.set_appearance_mode(appearance)
        ctk.set_default_color_theme(color_theme)

        self.login_root = ctk.CTk()
        self.login_root.title("Asclepius - Log in")
        self.login_root.geometry("800x600")
        self.login_root.resizable(False, False)

        self.login_bg = ctk.CTkImage(Image.open("assets/images/background.png"))

        self.__id = ctk.StringVar()
        self.__password = ctk.StringVar()

    def submit(self) -> None:
        print(self.__id.get())
        print(self.__password.get())

    def display_login_screen(self) -> None:

        background_label = ctk.CTkLabel(self.login_root, image=self.login_bg)
        title_label = ctk.CTkLabel(
            self.login_root, text="Welcome to Asclepius!", font=("Elephant", 25)
        )

        submit_button = ctk.CTkButton(
            self.login_root, text="Submit", command=self.submit
        )

        title_label.pack(side="top", fill="both", expand="yes")
        submit_button.pack(side="bottom", pady=100)

        self.login_root.mainloop()
