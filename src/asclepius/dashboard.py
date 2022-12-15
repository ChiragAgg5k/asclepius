import customtkinter as ctk
from PIL import Image


class Dashboard:
    """
    This class is used to create the dashboard for the user.
    This is where most of the program will be run from.
    """

    def __init__(
        self,
        width: int,
        height: int,
        appearance: str,
        theme_color: str,
        dataset: list,
        col_headers: list,
    ) -> None:
        """Constructor for Dashboard class for Asclepius.

        Args:
            width (int): witdh of the window
            height (int): height of the window
            appearance (str): ['light', 'Dark','System']
            theme_color (str): ['blue','green','dark-blue']
            dataset (list): list of lists containing the data
            col_headers (list): list of strings containing the column headers
        """
        self.width = width
        self.height = height
        self.appearance = appearance
        self.theme_color = theme_color
        self.dataset = dataset
        self.col_headers = col_headers

    def center_window(self) -> None:
        """Center the window."""

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coord = (screen_width / 2) - (self.width / 2)
        y_coord = (screen_height / 2) - (self.height / 2)
        self.root.geometry(f"{self.width}x{self.height}+{int(x_coord)}+{int(y_coord)}")

    def title_frame(self, title: str) -> None:
        """Create the title frame.

        Args:
            title (str): title of the frame
        """

        title_frame = ctk.CTkFrame(
            self.root, width=self.width - 200, height=50, corner_radius=10
        )
        title_frame.pack(side="top", fill="x", padx=20, pady=20, anchor=ctk.NE)

        title_label = ctk.CTkLabel(title_frame, text=title, font=self.title_font)
        title_label.grid(row=0, column=0, padx=20, pady=20)

        tagline_label = ctk.CTkLabel(
            title_frame, text="- Your Wellness Partner", font=self.tagline_font
        )
        tagline_label.grid(row=0, column=1, pady=20)

    def navigation_frame(self) -> None:
        """Create the navigation frame."""

        navigation_frame = ctk.CTkFrame(
            self.root, width=100, height=self.height, corner_radius=15
        )

        navigation_title = ctk.CTkLabel(
            navigation_frame, text="Navigation", font=self.op_font
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

        appearance_mode_optionemenu = ctk.CTkOptionMenu(
            navigation_frame,
            values=["System", "Dark", "Light"],
            command=self.change_appearance_mode_event,
            font=self.button_font,
            height=50,
        )

        quit_button = ctk.CTkButton(
            navigation_frame,
            text=" Quit ",
            font=self.button_font,
            command=self.root.destroy,
            corner_radius=10,
            height=40,
        )

        navigation_frame.pack(fill="y", side="left", padx=(20, 0), pady=(20, 20))

        navigation_title.pack(fill="x", padx=10, pady=20)

        self.dashboard_button.pack(fill="x", padx=10, pady=15)
        self.meds_button.pack(fill="x", padx=10, pady=15)
        self.mrecord_button.pack(fill="x", padx=10, pady=15)
        self.mhelp_button.pack(fill="x", padx=10, pady=15)

        quit_button.pack(fill="x", padx=10, pady=20, side="bottom")
        appearance_mode_optionemenu.pack(fill="x", padx=10, pady=20, side="bottom")

    def reset_frame(self, frame_name) -> None:

        self.dashboard_frame.pack_forget()
        self.meds_frame.pack_forget()
        self.mhelp_frame.pack_forget()
        self.mrec_frame.pack_forget()

        if frame_name == "home":
            self.dashboard_frame.pack(
                fill="both", expand=True, padx=(20, 20), pady=(0, 20)
            )

        elif frame_name == "meds":
            self.meds_frame.pack(fill="both", expand=True, padx=(20, 20), pady=(0, 20))

        elif frame_name == "mhelp":
            self.mhelp_frame.pack(fill="both", expand=True, padx=(20, 20), pady=(0, 20))

        elif frame_name == "mrecord":
            self.mrec_frame.pack(fill="both", expand=True, padx=(20, 20), pady=(0, 20))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Change the appearance mode.

        Args:
            new_appearance_mode (str): The new appearance mode.
        """

        ctk.set_appearance_mode(new_appearance_mode)

    def show_dashboard(self) -> None:
        """Show the dashboard."""

        ctk.set_appearance_mode(self.appearance)
        ctk.set_default_color_theme(self.theme_color)

        self.root = ctk.CTk()
        self.root.title("Asclepius")
        self.root.resizable(False, False)

        # ------------------------ Fonts ------------------------#
        self.op_font = ctk.CTkFont(
            family="Franklin Gothic", size=30, weight="bold", underline=True
        )
        self.title_font = ctk.CTkFont(family="Rockwell", size=60, weight="bold")
        self.button_font = ctk.CTkFont(family="Rockwell", size=20, weight="bold")
        self.text_font = ctk.CTkFont(family="Rockwell", size=20, weight="normal")
        self.small_text_font = ctk.CTkFont(family="Arial", size=18, weight="normal")
        self.tagline_font = ctk.CTkFont(family="Rockwell", size=30, weight="normal")
        # ------------------------ Fonts ------------------------#

        # ------------------------ User Dashboard ------------------------#
        self.dashboard_frame = ctk.CTkFrame(self.root)

        ctk.CTkLabel(
            self.dashboard_frame, text="Welcome to Asclepius", font=self.op_font
        ).pack(padx=20, pady=20)
        ctk.CTkLabel(
            self.dashboard_frame,
            text="""Hello, User Name. Welcome to Asclepius, Your Wellness Partner. The following are the your 
            details saved in our database.""",
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
        # ------------------------ User Dashboard ------------------------#

        # ----------------------- Medicines Dashboard -----------------------#
        self.meds_frame = ctk.CTkFrame(self.root)
        meds_scroll_bar = ctk.CTkScrollbar(self.meds_frame, orientation="vertical")
        meds_scroll_bar.place(relx=0.98, rely=0.05, relheight=0.9, anchor="ne")
        ctk.CTkLabel(self.meds_frame, text="Meds List", font=self.op_font).grid(
            row=0, column=0, columnspan=7, padx=20, pady=20
        )

        col1 = ctk.CTkEntry(self.meds_frame, width=160, height=50, font=self.text_font)
        col1.insert(ctk.END, self.col_headers[0].capitalize())
        col1.configure(state=ctk.DISABLED)
        col1.grid(row=1, column=1, padx=(20, 0), pady=(10, 20), ipady=1)

        for i in range(1, len(self.col_headers)):
            col = ctk.CTkEntry(
                self.meds_frame, width=160, height=50, font=self.text_font
            )
            col.insert(ctk.END, self.col_headers[i].capitalize())
            col.configure(state=ctk.DISABLED)

            col.grid(row=1, column=(i + 1), pady=(10, 20), ipady=1)

        order_entry = ctk.CTkEntry(
            self.meds_frame, height=50, font=self.text_font, width=130
        )
        order_entry.insert(ctk.END, "Order")
        order_entry.grid(row=1, column=6, pady=(10, 20), ipady=1)

        row = 2
        for i in self.dataset:
            for j in range(len(i)):
                e = ctk.CTkEntry(
                    self.meds_frame,
                    width=140,
                    font=self.small_text_font,
                )
                e.grid(row=row, column=(j + 1))
                e.insert(ctk.END, i[j])
                e.configure(state=ctk.DISABLED)

            ctk.CTkButton(
                self.meds_frame,
                text="Order",
                font=self.button_font,
                width=130,
                border_width=1,
            ).grid(row=row, column=6)

            row += 1
        # ----------------------- Medicines Dashboard -----------------------#

        # ----------------------- Med Help Dashboard -----------------------#
        self.mhelp_frame = ctk.CTkFrame(self.root)

        wellness_description = """
To ensure students’s well-being, Bennett provides a well-equipped wellness centre with four beds and round-the-clock,
with a small nursing staff on standby. A well-qualified general physician is available on campus 24*7.For prolonged 
medical illness, orfor case of infection, recovery rooms are available. The centre organises health check-up camps, 
blood donation drives, and physiotherapy sessions for students and staff.

Asclepius is a platform for students to access the wellness centre from anywhere. It provides all the necessary 
services and information about the wellness centre.
"""

        ctk.CTkLabel(
            self.mhelp_frame,
            text="About Asclepius",
            font=self.op_font,
            anchor=ctk.CENTER,
        ).pack(padx=(20, 20), pady=20)
        ctk.CTkLabel(
            self.mhelp_frame, text=wellness_description, font=self.small_text_font
        ).pack(anchor=ctk.CENTER, padx=20)
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
        # ----------------------- Med Help Dashboard -----------------------#

        # -------------------- Medical Records Dashboard --------------------#
        self.mrec_frame = ctk.CTkFrame(self.root)
        ctk.CTkLabel(self.mrec_frame, text="Medical Records", font=self.op_font).pack(
            padx=20, pady=20
        )
        # -------------------- Medical Records Dashboard --------------------#

        self.navigation_frame()
        self.title_frame("Asclepius")

        self.dashboard_frame.pack(fill="both", expand=True, padx=(20, 20), pady=(0, 20))

        self.center_window()
        self.root.mainloop()
