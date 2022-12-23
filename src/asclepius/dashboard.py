import customtkinter as ctk
from PIL import Image

from asclepius.centerwin import CenterWindow
from asclepius.database import Database


class Dashboard:
    """
    This class is used to create the dashboard for the user.
    This is where most of the program will be run from.
    """

    def __init__(
        self,
        width: int = 1280,
        height: int = 720,
        appearance: str = "dark",
        theme_color: str = "green",
        enrollment_id: str = "",
    ) -> None:
        """Constructor for Dashboard class for Asclepius.

        Args:
            width (int): width of the window
            height (int): height of the window
            appearance (str): ['light', 'Dark']
            theme_color (str): ['blue','green','dark-blue']
            dataset (list): list of lists containing the data
            col_headers (list): list of strings containing the column headers
        """

        self.width = width
        self.height = height
        self.user_id = enrollment_id

        self.db_object = Database("Dashboard")

        self.dataset = self.db_object.get_medicines()
        self.col_headers = self.db_object.get_col_headings("medicines")

        ctk.set_appearance_mode(appearance)
        ctk.set_default_color_theme(theme_color)

        self.root = ctk.CTk()
        self.root.title("Asclepius - Your Wellness Partner")
        # self.root.resizable(False, False)

        self.title_logo = ctk.CTkImage(
            Image.open("assets/images/logo-no-background.png"), size=(125, 100)
        )

        self.order_list = []
        self.column_widths = [80, 150, 450, 80, 100]

        # ------------------------ Fonts ------------------------#
        self.op_font = ctk.CTkFont(
            family="Franklin Gothic", size=30, weight="bold", underline=True
        )
        self.title_font = ctk.CTkFont(family="Rockwell", size=60, weight="bold")
        self.text_font = ctk.CTkFont(family="Rockwell", size=20, weight="normal")
        self.text_font_bold = ctk.CTkFont(family="Rockwell", size=20, weight="bold")
        self.small_text_font = ctk.CTkFont(family="Arial", size=18, weight="normal")
        self.tagline_font = ctk.CTkFont(family="Rockwell", size=30, weight="normal")
        # ------------------------ Fonts ------------------------#

        self.dashboard_frame = ctk.CTkFrame(self.root)
        self.mrec_frame = ctk.CTkFrame(self.root)
        self.mhelp_frame = ctk.CTkFrame(self.root)

        self.meds_frame = ctk.CTkFrame(self.root)
        self.meds_canvas = ctk.CTkCanvas(self.meds_frame)
        self.scrollable_frame = ctk.CTkFrame(self.meds_canvas)
        self.scrollbar = ctk.CTkScrollbar(
            self.meds_frame,
            orientation=ctk.VERTICAL,
            command=self.meds_canvas.yview,
            width=30,
        )

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

        title_logo_label = ctk.CTkLabel(title_frame, image=self.title_logo, text="")

        title_label.pack(side=ctk.LEFT, padx=(20, 0))
        tagline_label.pack(side=ctk.LEFT, padx=(0, 20))
        title_logo_label.pack(side=ctk.RIGHT, padx=(0, 20), pady=5)

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
            font=self.text_font_bold,
            command=lambda: self.reset_frame("home"),
            corner_radius=10,
            height=40,
        )

        meds_button = ctk.CTkButton(
            navigation_frame,
            text=" Medicines ",
            font=self.text_font_bold,
            command=lambda: self.reset_frame("meds"),
            corner_radius=10,
            height=40,
        )

        mhelp_button = ctk.CTkButton(
            navigation_frame,
            text=" About ",
            font=self.text_font_bold,
            command=lambda: self.reset_frame("mhelp"),
            corner_radius=10,
            height=40,
        )

        mrecord_button = ctk.CTkButton(
            navigation_frame,
            text=" Med Records ",
            font=self.text_font_bold,
            command=lambda: self.reset_frame("mrecord"),
            corner_radius=10,
            height=40,
        )

        light_mode = ctk.CTkButton(
            navigation_frame,
            text=" Light Mode ",
            font=self.text_font_bold,
            height=30,
            command=lambda: self.change_appearance_mode_event("Light"),
        )

        dark_mode = ctk.CTkButton(
            navigation_frame,
            text=" Dark Mode ",
            font=self.text_font_bold,
            height=30,
            command=lambda: self.change_appearance_mode_event("Dark"),
        )

        quit_button = ctk.CTkButton(
            navigation_frame,
            text=" Quit ",
            font=self.text_font_bold,
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
        light_mode.pack(pady=15, side=ctk.BOTTOM)
        dark_mode.pack(pady=15, side=ctk.BOTTOM)

    def reset_frame(self, frame_name) -> None:
        """Changes the frame to the given frame. Forgets the other frames.

        Args:
            frame_name (str): name of the frame to be displayed
        """

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
            self.display_mrec()
        else:
            self.mrec_frame.pack_forget()

        print("Frame reset to", frame_name)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Change the appearance mode.

        Args:
            new_appearance_mode (str): The new appearance mode.
        """

        ctk.set_appearance_mode(new_appearance_mode)
        print("Appearance mode changed to", new_appearance_mode, "mode")

    def order_check_button(self, mid: str) -> None:
        """Check button pressed. Add or remove the medicine from the order list.

        Args:
            mid (str): Medicine ID
        """
        try:
            self.order_list.remove(mid)
            print("Removed", mid)
        except ValueError:
            self.order_list.append(mid)
            print("Added", mid)

    def final_confirm_button_pressed(self) -> None:
        """Final confirm button pressed. Place the order."""

        self.db_object.add_orders(self.order_list, self.user_id)

        self.order_list = []
        self.order_confirmation.destroy()
        print("Order placed.")

    def place_order(self) -> None:
        """Pop up a window to confirm the order. Displays the order list."""

        self.order_confirmation = ctk.CTkToplevel(self.root)
        self.order_confirmation.title("Order Confirmation")
        self.order_confirmation.resizable(False, False)

        CenterWindow.center_window(self.order_confirmation, 1000, 400)

        if not self.order_list:

            order_confirmation_label = ctk.CTkLabel(
                self.order_confirmation,
                text="No medicines selected.",
                font=self.text_font,
            )
            order_confirmation_label.pack(padx=20, pady=20, anchor=ctk.CENTER)

            close_button = ctk.CTkButton(
                self.order_confirmation,
                text="Close Window",
                command=self.order_confirmation.destroy,
            )
            close_button.pack(pady=20)

        else:

            order_confirmation_label = ctk.CTkLabel(
                self.order_confirmation,
                text="The following medicines have been selected:",
                font=self.text_font,
            )
            order_confirmation_label.pack(padx=20, pady=20, anchor=ctk.CENTER)

            order_list_frame = ctk.CTkFrame(self.order_confirmation)

            row = 0
            total_amount = 0
            for i in self.dataset:
                if i[0] in self.order_list:

                    for j in range(0, len(i) - 1):
                        order_cell = ctk.CTkEntry(
                            order_list_frame,
                            width=self.column_widths[j],
                        )
                        try:
                            order_cell.insert(0, i[j].capitalize())
                        except AttributeError:
                            order_cell.insert(0, i[j])
                        order_cell.grid(
                            row=row,
                            column=(j + 1),
                            pady=5,
                            ipady=1,
                            padx=5,
                        )
                    row += 1
                    total_amount += i[-2]

            order_list_frame.pack(padx=20, pady=20, anchor=ctk.CENTER)

            self.final_confirmation_button = ctk.CTkButton(
                self.order_confirmation,
                text="Confirm Order",
                font=self.text_font,
                command=self.final_confirm_button_pressed,
                corner_radius=10,
                height=40,
            )

            total_amount_label = ctk.CTkLabel(
                self.order_confirmation,
                text=f"Number of medicines ordered: {row}\nTotal Amount: {total_amount}",
                font=self.text_font,
            )

            total_amount_label.pack(padx=20, pady=20, anchor=ctk.CENTER)
            self.final_confirmation_button.pack(padx=20, pady=20, anchor=ctk.CENTER)

    def display_table(self) -> None:
        """Display the table of medicines."""

        check_box_var = ctk.StringVar()

        for pos, text in enumerate(self.col_headers):

            col_cell = ctk.CTkLabel(
                self.scrollable_frame,
                text=text.capitalize(),
                font=self.text_font,
                width=self.column_widths[pos],
                height=50,
            )
            col_cell.grid(row=1, column=(pos + 1), pady=(10, 20), ipady=1, padx=5)

            col = ctk.CTkEntry(
                self.scrollable_frame,
                width=self.column_widths[pos],
                height=50,
                font=self.text_font,
            )

            col.insert(ctk.END, text.capitalize())
            col.configure(state=ctk.DISABLED)

            col.grid(row=1, column=(pos + 1), pady=(10, 20), ipady=1, padx=5)

        order_entry = ctk.CTkEntry(
            self.scrollable_frame, height=50, font=self.text_font, width=80
        )
        order_entry.insert(ctk.END, "Order")
        order_entry.grid(row=1, column=6, pady=(10, 20), ipady=1, padx=5)

        row = 2
        for i in self.dataset:

            for j in range(0, len(i)):
                entry = ctk.CTkEntry(
                    self.scrollable_frame,
                    width=self.column_widths[j],
                    font=self.small_text_font,
                )
                entry.grid(row=row, column=(j + 1), padx=5)

                try:
                    entry.insert(ctk.END, i[j].capitalize())
                except AttributeError:
                    entry.insert(ctk.END, i[j])

                entry.configure(state=ctk.DISABLED)

            order_checkbox = ctk.CTkCheckBox(
                self.scrollable_frame,
                text="",
                variable=check_box_var,
                onvalue=i[0],
                offvalue=i[0],
                command=lambda: self.order_check_button(check_box_var.get()),
                width=70,
            )

            if i[-1].lower() == "no":
                ctk.CTkLabel(
                    self.scrollable_frame,
                    text="  -",
                    font=self.small_text_font,
                    anchor=ctk.W,
                    width=70,
                ).grid(row=row, column=6, padx=5)
            else:
                order_checkbox.grid(row=row, column=6, padx=5)

            row += 1

    def display_mrec(self) -> None:
        """Display the medicine records of the user."""

        mrec = self.db_object.get_medicine_record(self.user_id)

        if mrec == []:
            ctk.CTkLabel(
                self.mrec_frame,
                text="No records found",
                font=self.text_font,
            ).grid(row=1, column=0, padx=20, pady=20, sticky=ctk.NSEW)
        else:
            mrec_col_headers = [
                "Mid",
                "Name",
                "Treatment",
                "Price",
                "Time of Purchase",
            ]

            mrec_col_widths = [80, 150, 450, 80, 220]

            for i in range(0, len(mrec_col_headers)):
                col_cell = ctk.CTkEntry(
                    self.mrec_frame,
                    width=mrec_col_widths[i],
                    font=self.text_font,
                )
                col_cell.insert(ctk.END, mrec_col_headers[i].capitalize())
                col_cell.configure(state=ctk.DISABLED)
                col_cell.grid(row=1, column=i, pady=(10, 20), ipady=1, padx=5)

            for i in range(0, len(mrec)):
                m_row = self.db_object.get_medicine_details(mrec[i][1])
                for j in range(0, len(m_row) - 1):
                    entry = ctk.CTkEntry(
                        self.mrec_frame,
                        width=self.column_widths[j],
                        font=self.small_text_font,
                    )
                    try:
                        entry.insert(ctk.END, m_row[j].capitalize())
                    except AttributeError:
                        entry.insert(ctk.END, m_row[j])
                    entry.configure(state=ctk.DISABLED)
                    entry.grid(row=(i + 2), column=j, padx=5)

            for i in range(len(mrec)):
                e = ctk.CTkEntry(
                    self.mrec_frame, width=mrec_col_widths[4], font=self.small_text_font
                )
                e.insert(ctk.END, mrec[i][2])
                e.configure(state=ctk.DISABLED)
                e.grid(row=(i + 2), column=4, padx=5)

        self.mrec_frame.pack(fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20))

    def show_dashboard_frame(self) -> None:
        """Display the user dashboard."""

        # ------------------------ User Dashboard ------------------------#
        self.dashboard_frame = ctk.CTkFrame(self.root)

        ctk.CTkLabel(
            self.dashboard_frame,
            text="ASCLEPIUS: Your Wellness Partner",
            font=self.op_font,
        ).pack(padx=20, pady=20)
        ctk.CTkLabel(
            self.dashboard_frame,
            text="""Hello. Welcome to Asclepius: Your Wellness Partner. Following are your details
saved in our database.""",
            font=self.text_font,
            anchor=ctk.CENTER,
        ).pack(anchor=ctk.CENTER, padx=20, pady=(20, 40))

        user_detail_labels = [
            "ENROLLMENT NUMBER: ",
            "FULL NAME: ",
            "HOSTELLER/DAY SCHOLAR: ",
            "ROOM No.: ",
            "PHONE NUMBER: ",
        ]
        user_details = self.db_object.get_signupdetails(self.user_id)

        for i in range(len(user_details) - 1):

            if user_details[i] == "":
                text_label = "Not Provided"
            elif user_details[i] == 0:
                text_label = "Day Scholar"
            elif user_details[i] == 1:
                text_label = "Hosteller"
            else:
                try:
                    text_label = user_details[i].capitalize()
                except AttributeError:
                    text_label = user_details[i]

            ctk.CTkLabel(
                self.dashboard_frame,
                text=f"{user_detail_labels[i]} : {text_label}",
                font=self.text_font,
                anchor=ctk.W,
            ).pack(anchor=ctk.W, padx=40, pady=20)

        # ------------------------ User Dashboard ------------------------#

        # ----------------------- Medicines Dashboard -----------------------#

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.meds_canvas.configure(
                scrollregion=self.meds_canvas.bbox("all")
            ),
        )

        place_order_button = ctk.CTkButton(
            self.meds_frame, text="Place Order", command=self.place_order
        )
        place_order_button.pack(padx=(0, 25), side="bottom", anchor=ctk.E)

        self.meds_canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor=ctk.N
        )
        self.meds_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.meds_canvas.pack(side="left", fill="both", expand=True)

        self.display_table()

        # ----------------------- Medicines Dashboard -----------------------#

        # ----------------------- Med Help Dashboard -----------------------#

        wellness_description = """
To ensure students’s well-being, Bennett provides a well-equipped wellness centre with four beds and round-the-clock,
with a small nursing staff on standby. A well-qualified general physician is available on campus 24*7.For prolonged 
medical illness, or for case of infection, recovery rooms are available. The centre organizes health check-up camps, 
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
            row=0, column=0, padx=20, pady=20, columnspan=7
        )
        # -------------------- Medical Records Dashboard --------------------#

        self.dashboard_frame.pack(
            fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20)
        )

    def show_dashboard(self) -> None:
        """Show the dashboard."""

        self.navigation_frame()
        self.title_frame("Asclepius")
        self.show_dashboard_frame()

        CenterWindow.center_window(self.root, self.width, self.height)
        self.root.mainloop()
