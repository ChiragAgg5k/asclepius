import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")


class Signup:
    # constructor
    def __init__(self, parent):
        self.widgets(parent)  # passing parent in order to bind the elements

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
        app.geometry("500x600")

        # background image
        self.bgimage = ctk.CTkImage(
            Image.open("assets/images/login_bg.png"), size=(500, 600)
        )
        self.bgLabel = ctk.CTkLabel(root, image=self.bgimage)
        self.bgLabel.place(x=0, y=0)

        # window title
        self.title = ctk.CTkLabel(
            app, text="SignUp to Asclepius!", font=("Arial", 14, "bold")
        ).pack(pady=10, padx=50)

        # creating name label and entry
        self.name_label = ctk.CTkLabel(
            app, text="Name", font=("Times New Roman", 14, "bold")
        ).place(relx=0.1, rely=0.1, anchor=ctk.NW)
        
        self.name_entry = ctk.CTkEntry(
            app, 
            textvariable=self.name,
            font=("Times New Roman", 12, "normal")
        ).place(relx=0.1, rely=0.15, width=300, height=30, anchor=ctk.NW)

        # creating username/enrollment label and entry
        self.username_label = ctk.CTkLabel(
            app, 
            text="UserName/Enrollment No.", 
            font=("Times New Roman", 14, "bold")
        ).place(relx=0.1, rely=0.22, anchor=ctk.NW)
        
        self.username_entry = ctk.CTkEntry(
            app, 
            textvariable=self.username, 
            font=("Times New Roman", 12, "normal")
        ).place(relx=0.1, rely=0.27, width=300, height=30, anchor=ctk.NW)

        # creating room no. label and entry
        # creating radio button enaled function

        self.room_no_label = ctk.CTkLabel(
            app, 
            text="Hostel Room No", 
            font=("Times New Roman", 14, "bold")
        ).place(relx=0.55, rely=0.35)
        self.room_entry = ctk.CTkEntry(
            app,
            textvariable=self.room_no,
            font=("Times New Roman", 12, "normal"),
            width=30,
        )
        self.room_entry.place(relx=0.55, rely=0.40, width=300, height=30)
        self.room_entry.configure(state="disabled")
        # radio buttons
        self.hostel_label =ctk.CTkLabel(
            app, 
            text="Dayscholar/Hosteler*", 
            font=("Times New Roman", 14, "bold")
        ).place(relx=0.1, rely=0.35)
        self.disableEntryRadioButton = ctk.CTkRadioButton(
            root,
            text="Dayscholar",
            font=("Times New Roman", 12, "normal"),
            variable=(self.var),
            value="0",
            command=self.disableEntry,
        )
        self.disableEntryRadioButton.place(relx=0.1, rely=0.40, anchor=ctk.NW)
        
        self.enableEntryRadioButton = ctk.CTkRadioButton(
            root,
            text="Hosteler",
            font=("Times New Roman", 12, "normal"),
            variable=(self.var),
            value="1",
            command=self.enableEntry,
        )
        self.enableEntryRadioButton.place(relx=0.1, rely=0.45, anchor=ctk.NW)

        # creating contact no. label and entry
        self.phone_label = ctk.CTkLabel(
            app, 
            text="Contact No.", 
            font=("Times New Roman", 14, "bold")
        ).place(relx=0.1, rely=0.52, anchor=ctk.NW)
        
        self.phone_entry = ctk.CTkEntry(
            app, 
            textvariable=self.phone, 
            font=("Times New Roman", 12, "normal")
        ).place(relx=0.1, rely=0.57, width=300, height=30, anchor=ctk.NW)

        # creating 'Register' button
        self.register = ctk.CTkButton(
            app,
            text="Register",
            font=("Times New Roman", 14, "bold"),
            
            command=self.submit,
        ).place(relx=0.5, rely=0.9, width=150, height=30, anchor=ctk.CENTER)

        self.password_label= ctk.CTkLabel(
            app, 
            text="Password", 
            font=("Times New Roman", 14, "bold")
        ).place(relx=0.1, rely=0.64, anchor=ctk.NW)

        self.password_entry = ctk.CTkEntry(
            app, 
            textvariable=self.phone, 
            font=("Times New Roman", 12, "normal")
        ).place(relx=0.1, rely=0.69, width=300, height=30, anchor=ctk.NW)

        self.confirm_password_label= ctk.CTkLabel(
            app, 
            text="Confirm Password", 
            font=("Times New Roman", 14, "bold")
        ).place(relx=0.1, rely=0.76, anchor=ctk.NW)

        self.confirm_password_entry = ctk.CTkEntry(
            app, 
            textvariable=self.phone, 
            font=("Times New Roman", 12, "normal")
        ).place(relx=0.1, rely=0.81, width=300, height=30, anchor=ctk.NW)



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
        room_no = self.room_no.get()
        name.set("")
        username.set("")
        room_no.set("")
        phone.set("")

        self.root.mainloop()

# creating tkinter object to pass into class object
root = ctk.CTk()

# class object
obj = Signup(root)


