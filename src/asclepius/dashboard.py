import customtkinter as ctk
from PIL import Image

from asclepius import database


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

        self.db = database.Database()

        self.width = width
        self.height = height

        self.dataset = self.db.get_medicines()
        self.col_headers = self.db.get_col_headings("medicines")

        ctk.set_appearance_mode(appearance)
        ctk.set_default_color_theme(theme_color)

        self.root = ctk.CTk()
        self.root.title("Asclepius")
        self.root.resizable(False, False)

        self.root.iconbitmap("assets/images/logo-no-background.ico")

        self.order_list = []
        self.column_widths = [80, 150, 450, 80, 100]

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

    def center_window(self, root: ctk.CTk, width: int, height: int) -> None:
        """Center the window."""

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x_coord = (screen_width / 2) - (width / 2)
        y_coord = (screen_height / 2) - (height / 2)
        root.geometry(f"{self.width}x{self.height}+{int(x_coord)}+{int(y_coord)}")

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
        title_logo = ctk.CTkImage(
            Image.open("assets/images/logo-no-background.png"), size=(125, 100)
        )
        title_logo_label = ctk.CTkLabel(title_frame, image=title_logo, text="")

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

    def final_confirm_button_pressed(self):
        """Final confirm button pressed. Place the order."""

        self.db.add_orders(self.order_list)

        self.order_list.clear()
        self.order_confirmation.destroy()

    def place_order(self):
        """Pop up a window to confirm the order. Displays the order list."""

        self.order_confirmation = ctk.CTkToplevel(self.root)
        self.order_confirmation.title("Order Confirmation")
        self.order_confirmation.resizable(False, False)

        self.order_confirmation.geometry(
            f"{self.meds_frame.winfo_width() - 40}x{self.meds_frame.winfo_height() - 100}+300+300"
        )

        if len(self.order_list) == 0:

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

        self.order_confirmation.mainloop()

    def display_table(self) -> None:
        """Display the table of medicines."""

        check_box_var = ctk.StringVar()

        for i in range(0, len(self.col_headers)):

            col_cell = ctk.CTkLabel(
                self.scrollbar_frame,
                text=self.col_headers[i].capitalize(),
                font=self.text_font,
                width=self.column_widths[i],
                height=50,
            )
            col_cell.grid(row=1, column=(i + 1), pady=(10, 20), ipady=1, padx=5)

            col = ctk.CTkEntry(
                self.scrollbar_frame,
                width=self.column_widths[i],
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
                    width=self.column_widths[j],
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

            if i[-1].lower() == "no":
                ctk.CTkLabel(
                    self.scrollbar_frame,
                    text="  -",
                    font=self.small_text_font,
                    anchor=ctk.W,
                    width=70,
                ).grid(row=row, column=6, padx=5)
            else:
                order_checkbox.grid(row=row, column=6, padx=5)

            row += 1

    def display_mrec(self):

        no_rec = ctk.CTkLabel(
            self.mrec_frame,
            text="No records found",
            font=self.text_font,
        )

        mrec = self.db.get_medicine_record()

        if mrec == []:
            no_rec.grid(row=1, column=0, padx=20, pady=20)
        else:
            no_rec.grid_forget()
            for i in range(0, len(self.record_set)):
                ctk.CTkLabel(
                    self.mrec_frame,
                    text=self.record_set[i],
                    font=self.text_font,
                ).grid(row=(i + 1), column=0, padx=20, pady=20)

        self.mrec_frame.pack(fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20))

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

        place_order_button = ctk.CTkButton(
            self.meds_frame, text="Place Order", command=self.place_order
        )
        place_order_button.pack(padx=(0, 25), side="bottom", anchor=ctk.E)

        self.meds_canvas.create_window(
            (0, 0), window=self.scrollbar_frame, anchor=ctk.N
        )
        self.meds_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.meds_canvas.pack(side="left", fill="both", expand=True)

        self.display_table()

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
        # -------------------- Medical Records Dashboard --------------------#

        self.dashboard_frame.pack(
            fill=ctk.BOTH, expand=True, padx=(0, 20), pady=(0, 20)
        )

    def show_dashboard(self) -> None:
        """Show the dashboard."""

        self.navigation_frame()
        self.title_frame("Asclepius")
        self.dashboard_frame()

        self.center_window(self.root, self.width, self.height)
        self.root.mainloop()
