from tkinter import *

import customtkinter as ctk

from asclepius.centerwin import CenterWindow

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")


class Signup:
    # constructor
    def __init__(self):
        parent = ctk.CTk()
        self.widgets(parent)  # passing parent in order to bind the elements

    # function for labels and entries
    def widgets(self, app):
        # declaring textvariables to store the input from user
        self.name = StringVar()
        self.username = StringVar()
        self.phone = StringVar()
        self.room_no = StringVar()
        # self.room_no.set(None)
        self.var = StringVar()
        self.var.set(None)

        # app title and geometry
        app.title("Signup Here!")
        app.geometry("500x500")

        # background image
        self.bgimage = PhotoImage(file="assets/images/login_bg.png")
        self.bgLabel = Label(app, image=self.bgimage)
        self.bgLabel.place(x=0, y=0)

        # window title
        self.title = Label(
            app, text="SignUp to Asclepius!", font=("Arial", 14, "bold")
        ).pack(pady=40, padx=50)

        # creating name label and entry
        self.name_label = Label(
            app, text="Name", font=("Times New Roman", 14, "bold")
        ).place(relx=0.1, rely=0.15, anchor=NW)
        self.name_entry = Entry(
            app, textvariable=self.name, font=("Times New Roman", 12, "normal")
        ).place(relx=0.1, rely=0.22, width=300, height=30, anchor=NW)

        # creating username/enrollment label and entry
        self.username_label = Label(
            app, text="UserName/Enrollment No.", font=("Times New Roman", 14, "bold")
        ).place(relx=0.1, rely=0.30, anchor=NW)
        self.username_entry = Entry(
            app, textvariable=self.username, font=("Times New Roman", 12, "normal")
        ).place(relx=0.1, rely=0.37, width=300, height=30, anchor=NW)

        # creating room no. label and entry
        # creating radio button enaled function

        self.room_no_label = Label(
            app, text="Hostel Room No", font=("Times New Roman", 14, "bold")
        ).place(relx=0.55, rely=0.45)
        self.room_entry = Entry(
            app,
            textvariable=self.room_no,
            font=("Times New Roman", 12, "normal"),
            width=30,
        )
        self.room_entry.place(relx=0.55, rely=0.50, width=300, height=30)
        self.room_entry.config(state="disabled")
        # radio buttons
        self.hostel_label = Label(
            app, text="Dayscholar/Hosteler*", font=("Times New Roman", 14, "bold")
        ).place(relx=0.1, rely=0.45)
        self.disableEntryRadioButton = Radiobutton(
            app,
            text="Dayscholar",
            font=("Times New Roman", 12, "normal"),
            variable=(self.var),
            value="0",
            command=self.disableEntry,
        )
        self.disableEntryRadioButton.place(relx=0.1, rely=0.50, anchor=NW)
        self.enableEntryRadioButton = Radiobutton(
            app,
            text="Hosteler",
            font=("Times New Roman", 12, "normal"),
            variable=(self.var),
            value="1",
            command=self.enableEntry,
        )
        self.enableEntryRadioButton.place(relx=0.1, rely=0.55, anchor=NW)

        # creating contact no. label and entry
        self.phone_label = Label(
            app, text="Contact No.", font=("Times New Roman", 14, "bold")
        ).place(relx=0.1, rely=0.63, anchor=NW)
        self.phone_entry = Entry(
            app, textvariable=self.phone, font=("Times New Roman", 12, "normal")
        ).place(relx=0.1, rely=0.70, width=300, height=30, anchor=NW)

        # creating 'Register' button
        self.register = Button(
            app,
            text="Register",
            font=("Times New Roman", 14, "bold"),
            bg="sky blue",
            command=self.submit,
        ).place(relx=0.5, rely=0.85, width=150, height=30, anchor=CENTER)

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
        root = ctk.CTk()
        self.widgets(root)

        CenterWindow.center_window(self.root, self.width, self.height)
        self.root.mainloop()
