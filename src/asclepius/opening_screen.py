from login_screen import Login
from signup import Signup
import customtkinter as ctk
 
class Opening_screen:
    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        self.root = ctk.CTk()
        self.root.resizable(False, False)

        self.width = 450
        self.height = 350

    def openNewWindow(self):
     
        # Toplevel object which will
        # be treated as a new window
        self.newWindow = ctk.CTkToplevel()
 
        # sets the title of the
        # Toplevel widget
        self.newWindow.title("Welcome")
 
        # sets the geometry of toplevel
        self.newWindow.geometry("450x350")
 
        # A Label widget to show in toplevel
        self.top_Label= ctk.CTkLabel(newWindow, text ="Welcome to Asclepius", font= ("Elephant", 20, "bold")).pack(pady= 10, padx= 50)

        self.login_button = ctk.CTkButton(
                self.root,
                text="Login",
                font=("Arial", 20, "bold"),
                width=150,
                height=40,
                corner_radius=10,
                command=self.login,
            ).pack(padx= 50, pady= 30)
        
        
        def login(self):
            self.obj = Login()
            self.obj.display()
            

        self.signup_button = ctk.CTkButton(
                self.root,
                text="Signup",
                font=("Arial", 20, "bold"),
                width=150,
                height=40,
                corner_radius=10,
                command=self.obj.signup,
            ).pack(padx= 50, pady= 60)


        def signup(self):
            self.obj = Signup()
            self.obj.display_signup()
            

obj= Opening_screen()
obj.openNewWindow()
root.mainloop()
        