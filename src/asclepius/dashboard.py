import sqlite3

import customtkinter as ctk


class Dashboard:
    def __init__(
        self, width: int, height: int, appearance: str, theme_color: str, data: list
    ) -> None:
        """Constructor for Dashboard class for Asclepius.

        Args:
            width (int): witdh of the window
            height (int): height of the window
            appearance (str): ['light', 'Dark','System']
            theme_color (str): ['blue','green','dark-blue']
        """

        self.root = ctk.CTk()
        self.root.title("Asclepius")
        self.root.resizable(False, False)
        self.height = height
        self.width = width

        ctk.set_appearance_mode(appearance)
        ctk.set_default_color_theme(theme_color)

        self.op_font = ctk.CTkFont(
            family="Franklin Gothic", size=30, weight="bold", underline=True
        )
        self.title_font = ctk.CTkFont(family="Rockwell", size=60, weight="bold")
        self.button_font = ctk.CTkFont(family="Rockwell", size=20, weight="bold")
        self.text_font = ctk.CTkFont(family="Rockwell", size=20, weight="normal")
        self.small_text_font = ctk.CTkFont(family="Arial", size=17, weight="normal")

        # User Dashboard
        self.dashboard_frame = ctk.CTkFrame(self.root)
        ctk.CTkLabel(
            self.dashboard_frame, text="Welcome to Asclepius", font=self.op_font
        ).pack(padx=20, pady=20)
        ctk.CTkLabel(
            self.dashboard_frame,
            text="Hello, User Name. Welcome to Asclepius, Your Wellness Partner.",
            font=self.text_font,
            anchor=ctk.W,
        ).pack(anchor=ctk.W, padx=20, pady=20)
        ctk.CTkLabel(
            self.dashboard_frame, text="User Name - Username", font=self.small_text_font
        ).pack(anchor=ctk.W, padx=20, pady=20)
        ctk.CTkLabel(
            self.dashboard_frame,
            text="Enroll ID - EnrollmentID",
            font=self.small_text_font,
        ).pack(anchor=ctk.W, padx=20, pady=20)
        ctk.CTkLabel(
            self.dashboard_frame,
            text="User Phone No. - +91 XXXXX XXXXX",
            font=self.small_text_font,
        ).pack(anchor=ctk.W, padx=20, pady=20)
        ctk.CTkLabel(
            self.dashboard_frame, text="Registered Since - ", font=self.small_text_font
        ).pack(anchor=ctk.W, padx=20, pady=20)

        # Medicines Dashboard
        self.meds_frame = ctk.CTkFrame(self.root)
        ctk.CTkLabel(self.meds_frame, text="Meds List", font=self.op_font).grid(
            row=0, column=0, columnspan=7, padx=20, pady=20
        )
        row = 1
        for i in data:
            for j in range(len(i)):
                e = ctk.CTkEntry(
                    self.meds_frame,
                    width=140,
                    font=self.small_text_font,
                )
                e.grid(row=row, column=(j + 1))
                e.insert(ctk.END, i[j])
            ctk.CTkButton(
                self.meds_frame,
                text="Order",
                font=self.button_font,
                width=130,
                border_width=1,
            ).grid(row=row, column=6)
            row += 1

        # Med Help Dashboard
        self.mhelp_frame = ctk.CTkFrame(self.root)

        wellness_description = """
To ensure students’s well-being, Bennett provides a well-equipped wellness centre with four beds and 
round-the-clock, with a small nursing staff on standby. A well-qualified general physician is available 
on campus 24*7.For prolonged medical illness, or for case of infection, recovery rooms are available. 
The centre organises health check-up camps, blood donation drives, and physiotherapy sessions 
for students and staff.

Asclepius is a platform for students to access the wellness centre from anywhere. It provides
all the necessary services and information about the wellness centre.
"""

        ctk.CTkLabel(
            self.mhelp_frame,
            text="About Asclepius",
            font=self.op_font,
            anchor=ctk.CENTER,
        ).pack(padx=20, pady=20)
        ctk.CTkLabel(
            self.mhelp_frame, text=wellness_description, font=self.small_text_font
        ).pack(anchor=ctk.W, padx=20)
        ctk.CTkLabel(self.mhelp_frame, text="Contact Us", font=self.op_font).pack(
            anchor=ctk.W, padx=20, pady=20
        )
        ctk.CTkLabel(
            self.mhelp_frame,
            text="For general queries- 0120-7199300",
            font=self.small_text_font,
        ).pack(anchor=ctk.W, padx=20, pady=10)
        ctk.CTkLabel(
            self.mhelp_frame,
            text="WhatsApp- +91 8860309257",
            font=self.small_text_font,
        ).pack(anchor=ctk.W, padx=20, pady=10)

        # Medical Records Dashboard
        self.mrec_frame = ctk.CTkFrame(self.root)
        ctk.CTkLabel(self.mrec_frame, text="Medical Records", font=self.op_font).pack(
            padx=20, pady=20
        )

    def center_window(self) -> None:
        """Center the window."""

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coord = (screen_width / 2) - (self.width / 2)
        y_coord = (screen_height / 2) - (self.height / 2)
        self.root.geometry(f"{self.width}x{self.height}+{int(x_coord)}+{int(y_coord)}")

    def navigation_frame(self) -> None:
        """Create the navigation frame."""

        navigation_frame = ctk.CTkFrame(
            self.root, width=100, height=self.height, corner_radius=15
        )

        self.dashboard_button = ctk.CTkButton(
            navigation_frame,
            text=" DashBoard ",
            font=self.button_font,
            command=lambda: self.reset_frame("home"),
            corner_radius=10,
            height=40,
        )

        self.meds_button = ctk.CTkButton(
            navigation_frame,
            text=" Medicines ",
            font=self.button_font,
            command=lambda: self.reset_frame("meds"),
            corner_radius=10,
            height=40,
        )

        self.mhelp_button = ctk.CTkButton(
            navigation_frame,
            text=" About ",
            font=self.button_font,
            command=lambda: self.reset_frame("mhelp"),
            corner_radius=10,
            height=40,
        )

        self.mrecord_button = ctk.CTkButton(
            navigation_frame,
            text=" Med Records ",
            font=self.button_font,
            command=lambda: self.reset_frame("mrecord"),
            corner_radius=10,
            height=40,
        )

        navigation_frame.pack(fill="y", side="left", padx=20, pady=(0, 20))
        self.dashboard_button.pack(fill="x", padx=10, pady=20)
        self.meds_button.pack(fill="x", padx=10, pady=20)
        self.mrecord_button.pack(fill="x", padx=10, pady=20)
        self.mhelp_button.pack(fill="x", padx=10, pady=20)

    def reset_frame(self, frame_name) -> None:
        self.dashboard_frame.pack_forget()
        self.meds_frame.pack_forget()
        self.mhelp_frame.pack_forget()
        self.mrec_frame.pack_forget()

        if frame_name == "home":
            self.dashboard_frame.pack(
                fill="both", expand=True, padx=(0, 20), pady=(0, 20)
            )
        elif frame_name == "meds":
            self.meds_frame.pack(fill="both", expand=True, padx=(0, 20), pady=(0, 20))

        elif frame_name == "mhelp":
            self.mhelp_frame.pack(fill="both", expand=True, padx=(0, 20), pady=(0, 20))

        elif frame_name == "mrecord":
            self.mrec_frame.pack(fill="both", expand=True, padx=(0, 20), pady=(0, 20))

    def options_frame(self) -> None:
        """Create the options frame."""

        options_frame = ctk.CTkFrame(
            self.root, width=200, height=self.height, corner_radius=15
        )

        options_frame.pack(side="left", fill="y", padx=(20, 0), pady=20)

        options_title = ctk.CTkLabel(
            options_frame, text="Options", font=self.op_font, corner_radius=10
        )

        appearance_mode_optionemenu = ctk.CTkOptionMenu(
            options_frame,
            values=["System", "Dark", "Light"],
            command=self.change_appearance_mode_event,
            font=self.button_font,
            height=50,
        )

        quit_button = ctk.CTkButton(
            options_frame,
            text="Quit",
            font=self.button_font,
            command=self.root.destroy,
            corner_radius=10,
            height=50,
        )

        change_user_button = ctk.CTkButton(
            options_frame,
            text="Change User",
            font=self.button_font,
            command=self.change_user,
            corner_radius=10,
            height=50,
        )

        options_title.pack(side="top", fill="x", padx=10, pady=20)
        change_user_button.pack(side="top", fill="x", padx=10, pady=20)
        quit_button.pack(side="bottom", fill="x", padx=10, pady=(0, 20))
        appearance_mode_optionemenu.pack(side="bottom", fill="x", padx=10, pady=20)

    def title_frame(self, title):
        """Create the title frame."""

        title_frame = ctk.CTkFrame(
            self.root, width=self.width - 200, height=50, corner_radius=10
        )
        title_frame.pack(side="top", fill="x", padx=20, pady=20, anchor=ctk.NE)
        title_label = ctk.CTkLabel(title_frame, text=title, font=self.title_font)
        title_label.grid(row=0, column=0, padx=20, pady=20)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Change the appearance mode.

        Args:
            new_appearance_mode (str): The new appearance mode.
        """

        ctk.set_appearance_mode(new_appearance_mode)

    def change_user(self):
        pass

    def show_dashboard(self) -> None:
        """Show the dashboard."""

        # frames
        self.options_frame()
        self.title_frame("Asclepius")
        self.navigation_frame()

        self.dashboard_frame.pack(fill="both", expand=True, padx=(0, 20), pady=(0, 20))

        self.center_window()
        self.root.mainloop()
