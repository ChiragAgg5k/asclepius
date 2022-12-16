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
            appearance (str): ['light', 'Dark']
            theme_color (str): ['blue','green','dark-blue']
            dataset (list): list of lists containing the data
            col_headers (list): list of strings containing the column headers
        """
        self.width = width
        self.height = height
        self.dataset = dataset
        self.col_headers = col_headers

        ctk.set_appearance_mode(appearance)
        ctk.set_default_color_theme(theme_color)

        self.root = ctk.CTk()
        self.root.title("Asclepius")
        self.root.resizable(False, False)

        self.order_list = []

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

        title_label = ctk.CTkLabel(title_frame, text=title, font=self.title_font)

        tagline_label = ctk.CTkLabel(
            title_frame, text="- Your Wellness Partner", font=self.tagline_font
        )

        title_label.grid(row=0, column=0, padx=20, pady=20)
        tagline_label.grid(row=0, column=1, pady=20)

        title_frame.pack(side=ctk.TOP, fill=ctk.X, padx=(0, 20), pady=20)

    def navigation_frame(self) -> None:
        """Create the navigation frame."""

        navigation_frame = ctk.CTkFrame(
            self.root, width=100, height=self.height, corner_radius=15
        )

        navigation_title = ctk.CTkLabel(
            navigation_frame, text="Navigation", font=self.op_font
        )

        dashboard_button = ctk.CTkButton(
            navigation_frame,
            text=" DashBoard ",
            font=self.button_font,
            command=lambda: self.reset_frame("home"),
            corner_radius=10,
            height=40,
        )

        meds_button = ctk.CTkButton(
            navigation_frame,
            text=" Medicines ",
            font=self.button_font,
            command=lambda: self.reset_frame("meds"),
            corner_radius=10,
            height=40,
        )

        mhelp_button = ctk.CTkButton(
            navigation_frame,
            text=" About ",
            font=self.button_font,
            command=lambda: self.reset_frame("mhelp"),
            corner_radius=10,
            height=40,
        )

        mrecord_button = ctk.CTkButton(
            navigation_frame,
            text=" Med Records ",
            font=self.button_font,
            command=lambda: self.reset_frame("mrecord"),
            corner_radius=10,
            height=40,
        )

        appearance_mode_optionemenu = ctk.CTkOptionMenu(
            navigation_frame,
            values=["Dark", "Light"],
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

        navigation_frame.pack(side=ctk.LEFT, fill=ctk.Y, padx=20, pady=20)

        navigation_title.pack(pady=20)

        dashboard_button.pack(pady=15)
        meds_button.pack(pady=15)
        mrecord_button.pack(pady=15)
        mhelp_button.pack(pady=15)

        quit_button.pack(pady=15, side=ctk.BOTTOM)
        appearance_mode_optionemenu.pack(pady=15, side=ctk.BOTTOM)

    def reset_frame(self, frame_name) -> None:

        if frame_name == "home":
            self.dashboard_frame.pack(
                fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20)
            )
        else:
            self.dashboard_frame.pack_forget()

        if frame_name == "meds":
            self.meds_frame.pack(fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20))
        else:
            self.meds_frame.pack_forget()

        if frame_name == "mhelp":
            self.mhelp_frame.pack(
                fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20)
            )
        else:
            self.mhelp_frame.pack_forget()

        if frame_name == "mrecord":
            self.mrec_frame.pack(fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20))
        else:
            self.mrec_frame.pack_forget()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Change the appearance mode.

        Args:
            new_appearance_mode (str): The new appearance mode.
        """

        ctk.set_appearance_mode(new_appearance_mode)

    def order_check_button(self, mid: str):
        if mid == "0":
            try:
                self.order_list.pop()
            except IndexError:
                print("No order removed, list is empty.")
        else:
            self.order_list.append(mid)

    def place_order(self):
        if len(self.order_list) == 0:
            print("No order placed, list is empty.")
        else:
            print("Order placed.")
            self.order_list = []
            self.reset_frame("meds")

    def display_table(self) -> None:
        """Display the table of medicines."""

        column_widths = [80, 150, 450, 80, 100]
        check_box_var = ctk.StringVar()

        for i in range(0, len(self.col_headers)):

            col_cell = ctk.CTkLabel(
                self.scrollbar_frame,
                text=self.col_headers[i].capitalize(),
                font=self.text_font,
                width=column_widths[i],
                height=50,
            )
            col_cell.grid(row=1, column=(i + 1), pady=(10, 20), ipady=1, padx=5)

            col = ctk.CTkEntry(
                self.scrollbar_frame,
                width=column_widths[i],
                height=50,
                font=self.text_font,
            )

            col.insert(ctk.END, self.col_headers[i].capitalize())
            col.configure(state=ctk.DISABLED)

            col.grid(row=1, column=(i + 1), pady=(10, 20), ipady=1, padx=5)

        order_entry = ctk.CTkEntry(
            self.scrollbar_frame, height=50, font=self.text_font, width=80
        )
        order_entry.insert(ctk.END, "Order")
        order_entry.grid(row=1, column=6, pady=(10, 20), ipady=1, padx=5)

        row = 2
        for i in self.dataset:

            for j in range(0, len(i)):
                e = ctk.CTkEntry(
                    self.scrollbar_frame,
                    width=column_widths[j],
                    font=self.small_text_font,
                )
                e.grid(row=row, column=(j + 1), padx=5)

                try:
                    e.insert(ctk.END, i[j].capitalize())
                except AttributeError:
                    e.insert(ctk.END, i[j])

                e.configure(state=ctk.DISABLED)

            order_checkbox = ctk.CTkCheckBox(
                self.scrollbar_frame,
                text="",
                variable=check_box_var,
                onvalue=i[0],
                command=lambda: self.order_check_button(check_box_var.get()),
                width=70,
            )

            order_checkbox.grid(row=row, column=6, padx=5)

            row += 1

    def dashboard_frame(self):

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

        user_details = [
            "Name",
            "Enrollment Number",
            "Email",
            "Phone Number",
            "Hostel Room Number",
        ]

        for i in user_details:
            ctk.CTkLabel(
                self.dashboard_frame, text=i, font=self.text_font, anchor=ctk.W
            ).pack(anchor=ctk.W, padx=20, pady=20)

        # ------------------------ User Dashboard ------------------------#

        # ----------------------- Medicines Dashboard -----------------------#
        self.meds_frame = ctk.CTkFrame(self.root)

        self.meds_canvas = ctk.CTkCanvas(
            self.meds_frame,
            width=1000,
            height=500,
        )
        self.scrollbar = ctk.CTkScrollbar(
            self.meds_frame,
            orientation=ctk.VERTICAL,
            command=self.meds_canvas.yview,
            width=30,
        )
        self.scrollbar_frame = ctk.CTkFrame(self.meds_canvas)

        self.scrollbar_frame.bind(
            "<Configure>",
            lambda e: self.meds_canvas.configure(
                scrollregion=self.meds_canvas.bbox("all")
            ),
        )

        self.meds_canvas.create_window(
            (0, 0), window=self.scrollbar_frame, anchor=ctk.N
        )
        self.meds_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.meds_canvas.grid(row=0, column=0, sticky=ctk.NSEW)
        self.scrollbar.grid(row=0, column=1, sticky=ctk.NS)

        self.display_table()

        place_order_button = ctk.CTkButton(
            self.meds_frame, text="Place Order", command=self.place_order
        )
        place_order_button.grid(row=1, column=0, sticky=ctk.E, pady=5)

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
        ctk.CTkLabel(self.mrec_frame, text="Medical Records", font=self.op_font).grid(
            row=0, column=0, padx=20, pady=20
        )

        #! placeholder
        ctk.CTkLabel(
            self.mrec_frame, text="You have no records for now...", font=self.text_font
        ).grid(row=1, column=0, padx=20, pady=20)
        # -------------------- Medical Records Dashboard --------------------#

        self.dashboard_frame.pack(
            fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20)
        )

    def show_dashboard(self) -> None:
        """Show the dashboard."""

        self.navigation_frame()
        self.title_frame("Asclepius")
        self.dashboard_frame()

        self.center_window()
        self.root.mainloop()
