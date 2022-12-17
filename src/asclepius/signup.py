import customtkinter as ctk
from PIL import Image

from asclepius.centerwin import CenterWindow


class Signup:
    # constructor
    def __init__(self):
        self.root = ctk.CTk()

    # function for labels and entries
    def widgets(self, app):
        # declaring textvariables to store the input from user
        self.name = ctk.StringVar()
        self.username = ctk.StringVar()
        self.phone = ctk.StringVar()
        self.room_no = ctk.StringVar()
        # self.room_no.set(None)
        self.var = ctk.StringVar()
        self.var.set(None)

        # app title and geometry
        app.title("Signup Here!")
        app.geometry("500x500")

        # background image
        self.bgimage = ctk.CTkImage(
            Image.open("assets/images/login_bg.png"), size=(500, 500)
        )
        self.bgLabel = ctk.CTkLabel(app, image=self.bgimage, text="")
        self.bgLabel.place(x=0, y=0)

        # window title
        self.title = ctk.CTkLabel(
            app, text="SignUp to Asclepius!", font=("Arial", 14, "bold")
        ).pack(pady=40, padx=50)

        # creating name label and entry
        self.name_label = ctk.CTkLabel(
            app, text="Name", font=("Times New Roman", 14, "bold")
        ).place(relx=0.1, rely=0.15, anchor=ctk.NW)
        self.name_entry = ctk.CTkEntry(
            app, textvariable=self.name, font=("Times New Roman", 12, "normal")
        ).place(relx=0.1, rely=0.22, width=300, height=30, anchor=ctk.NW)

        # creating username/enrollment label and entry
        self.username_label = ctk.CTkLabel(
            app, text="UserName/Enrollment No.", font=("Times New Roman", 14, "bold")
        ).place(relx=0.1, rely=0.30, anchor=ctk.NW)
        self.username_entry = ctk.CTkEntry(
            app, textvariable=self.username, font=("Times New Roman", 12, "normal")
        ).place(relx=0.1, rely=0.37, width=300, height=30, anchor=ctk.NW)

        # creating room no. label and entry
        # creating radio button enaled function

        self.room_no_label = ctk.CTkLabel(
            app, text="Hostel Room No", font=("Times New Roman", 14, "bold")
        ).place(relx=0.55, rely=0.45)
        self.room_entry = ctk.CTkEntry(
            app,
            textvariable=self.room_no,
            font=("Times New Roman", 12, "normal"),
            width=30,
        )
        self.room_entry.place(relx=0.55, rely=0.50, width=200, height=30)
        self.room_entry.configure(state=ctk.DISABLED)
        # radio buttons
        self.hostel_label = ctk.CTkLabel(
            app, text="Dayscholar/Hosteler*", font=("Times New Roman", 14, "bold")
        ).place(relx=0.1, rely=0.45)
        self.disableEntryRadioButton = ctk.CTkRadioButton(
            app,
            text="Dayscholar",
            font=("Times New Roman", 12, "normal"),
            variable=(self.var),
            value="0",
            command=self.disableEntry,
        )
        self.disableEntryRadioButton.place(relx=0.1, rely=0.50, anchor=ctk.NW)
        self.enableEntryRadioButton = ctk.CTkRadioButton(
            app,
            text="Hosteler",
            font=("Times New Roman", 12, "normal"),
            variable=(self.var),
            value="1",
            command=self.enableEntry,
        )
        self.enableEntryRadioButton.place(relx=0.1, rely=0.55, anchor=ctk.NW)

        # creating contact no. label and entry
        self.phone_label = ctk.CTkLabel(
            app, text="Contact No.", font=("Times New Roman", 14, "bold")
        ).place(relx=0.1, rely=0.63, anchor=ctk.NW)
        self.phone_entry = ctk.CTkEntry(
            app, textvariable=self.phone, font=("Times New Roman", 12, "normal")
        ).place(relx=0.1, rely=0.70, width=300, height=30, anchor=ctk.NW)

        # creating 'Register' button
        self.register = ctk.CTkButton(
            app,
            text="Register",
            font=("Times New Roman", 14, "bold"),
            bg_color="sky blue",
            command=self.submit,
        ).place(relx=0.5, rely=0.85, width=150, height=30, anchor=ctk.CENTER)

    # callbacks
    def enableEntry(self):
        self.room_entry.configure(state="normal")
        self.room_entry.update()

    def disableEntry(self):
        self.room_entry.configure(state="disabled")
        self.room_entry.update()

    # function to get signup credentials
    # from textvariables declared earlier
    def submit(self):
        name = self.name.get()
        username = self.username.get()
        phone = self.phone.get()
        room_no = self.room.get()
        name.set("")
        username.set("")
        room_no.set("")
        phone.set("")

    def show_signup(self) -> None:
        """Show the signupwindow"""
        self.widgets(self.root)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

        CenterWindow.center_window(self.root, 500, 500)
        self.root.mainloop()
