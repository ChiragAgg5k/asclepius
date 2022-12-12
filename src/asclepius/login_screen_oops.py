from tkinter import *
import customtkinter as ctk
from captcha.image import ImageCaptcha


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

class Login:
    #constructor
    def __init__(self, parent):
        self.widgets(parent) #passing parent in order to bind the elements
        self.app = ctk

     #function for labels and entries
    def widgets(self, app):
        #declaring textvariables to store the input from user
        self.username= StringVar()
        self.password= StringVar()
        
        #app title and geometry
        app.title("Login Here!")
        app.geometry("450x350")

         # Create an image instance of the given size
        self.image = ImageCaptcha(width = 200, height = 30)
 
        # Image captcha text
        self.captcha_text = '564532' 
 
        # generate the image of the given text
        self.data = self.image.generate(self.captcha_text) 
 
        # write the image on the given file and save it
        self.image.write(self.captcha_text, 'CAPTCHA.png')

        self.captcha_label = Label(app, text= 'Enter Captcha:', font=('Times New Roman', 14, 'bold')).place(relx = 0.1, rely =0.52, anchor= NW)
        self.captcha_entry= Entry(app, textvariable=self.captcha_text).place(relx = 0.1,  rely = 0.60,width=300,height=30, anchor= NW)



        #background image
        self.bgimage = PhotoImage(file = "lgnbg.png")
        self.bgLabel = Label(root, image=self.bgimage)
        self.bgLabel.place(x = 0, y=0)

        #window title
        self.title = Label(app, text= 'Login Here!', font=('Arial', 14, 'bold')).pack(pady = 40, padx =50)

         #creating username label and entry
        self.username_label = Label(app, text = 'Name:', font= ('Times New Roman', 14, 'bold')).place(relx = 0.1, rely =0.20, anchor= NW)
        self.username_entry= Entry(app, textvariable=self.username).place(relx = 0.1,  rely = 0.27,width=300,height=30, anchor= NW)

         #creating password label and entry
        self.pswrd_label = Label(app, text = 'Password:', font= ('Times New Roman', 14, 'bold')).place(relx = 0.1, rely =0.40, anchor= NW)
        self.pswrd_entry= Entry(app, textvariable=self.password, width = 20).place(relx = 0.1,  rely = 0.47,width=300,height=30, anchor= NW)

        #creating 'submit' button
        self.submit= Button(app, text= 'Submit',font= ('Times New Roman', 14,'bold'), bg='light blue', command= self.submit).place(relx = 0.5, rely =0.70, width=150,height=40,anchor= CENTER)

    #function to get signup credentials
    # from textvariables declared earlier
    def submit(self):
        username= self.username.get()
        password= self.password.get()
        username.set("")
        password.set("")

   
# creating tkinter object to pass into class object
root = ctk.CTk()

#class object
obj= Login(root)

root.mainloop()