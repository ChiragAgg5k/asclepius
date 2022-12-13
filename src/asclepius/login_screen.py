import customtkinter as ctk


class Login:
    # constructor
    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()

    # function for CTkLabels and entries
    def display(self):
        # declaring textvariables to store the input from user
        self.username = ctk.StringVar()
        self.password = ctk.StringVar()

        # self.root title and geometry
        self.root.title("Login Here!")
        self.root.geometry("450x350")

        # background image
        # self.bgimage = ctk.PhotoImage(file="assets/images/login_bg.png")
        # self.bgCTkLabel = ctk.CTkLabel(self.root, image=self.bgimage)
        # self.bgCTkLabel.place(x=0, y=0)

        # window title
        self.title = ctk.CTkLabel(
            self.root, text="Login Here!", font=("Arial", 14, "bold")
        ).pack(pady=40, padx=50)

        # creating username CTkLabel and entry
        self.username_CTkLabel = ctk.CTkLabel(
            self.root, text="Name:", font=("Times New Roman", 14, "bold")
        ).place(relx=0.1, rely=0.20, anchor=ctk.NW)
        self.username_entry = ctk.CTkEntry(self.root, textvariable=self.username).place(
            relx=0.1, rely=0.27, width=300, height=30, anchor=ctk.NW
        )

        # creating password CTkLabel and entry
        self.pswrd_CTkLabel = ctk.CTkLabel(
            self.root, text="Password:", font=("Times New Roman", 14, "bold")
        ).place(relx=0.1, rely=0.40, anchor=ctk.NW)
        self.pswrd_entry = ctk.CTkEntry(
            self.root, textvariable=self.password, width=20
        ).place(relx=0.1, rely=0.47, width=300, height=30, anchor=ctk.NW)

        self.root.mainloop()
