from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Log In Here!")
root.geometry("450x350")

bgimage = PhotoImage(file = "lgnbg.png")

bgLabel = Label(root, image=bgimage)
bgLabel.place(x = 0, y=0)

label2 = Label(root, text = "Welcome to Asclepius!", font = ("Elephant", 25))
label2.pack(pady = 50, padx =50)

id_var= ctk.StringVar()
pw_var= ctk.StringVar()

def submit():
    id= id_var.get()
    password = pw_var.get()

    id_var.set("")
    pw_var.set("")

label3 = Label(root, text= "User ID:", font = ("Times New Roman", 18, 'bold'))
label3.place(relx = 0.1, rely =0.25, anchor= NW)

entry1 = ctk.CTkEntry(root, textvariable= id_var, font=('Arial', 18, 'normal'))
entry1.place(relx =0.1, rely = 0.35, anchor= NW )

label4 = Label(root, text = "Password:", font = ("Times New Roman", 18, 'bold'))
label4.place(relx = 0.1, rely = 0.48, anchor = NW)

entry2 = ctk.CTkEntry(root, textvariable= pw_var, show = "*" )
entry2.place(relx =0.1, rely = 0.58, anchor= NW )

sub_btn = ctk.CTkButton(root, text = "Submit", command = submit)
sub_btn.place(relx = 0.35, rely = 0.80)

root.mainloop()
