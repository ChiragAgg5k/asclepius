import sqlite3

import customtkinter as ctk


class Dashboard:
    def __init__(
        self, width: int, height: int, appearance: str, theme_color: str
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
            family="Copperplate", size=30, weight="bold", underline=True
        )
        self.title_font = ctk.CTkFont(family="Copperplate", size=60, weight="bold")
        self.button_font = ctk.CTkFont(family="Copperplate", size=20, weight="bold")

        self.dashboard_frame = ctk.CTkFrame(
            self.root,
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
            height=30,
        )

        navigation_frame.pack(fill="y", side="left", padx=20, pady=(0, 20))
        self.dashboard_button.pack(fill="x", padx=10, pady=20)

    def reset_frame(self, frame_name) -> None:
        self.dashboard_frame.pack_forget()

        if frame_name == "home":
            self.dashboard_frame.pack(
                fill="both", expand=True, padx=(0, 20), pady=(0, 20)
            )

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
            height=30,
        )

        quit_button = ctk.CTkButton(
            options_frame,
            text="Quit",
            font=self.button_font,
            command=self.root.destroy,
            corner_radius=10,
            height=30,
        )

        options_title.pack(side="top", fill="x", padx=10, pady=20)
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

    def show_dashboard(self) -> None:
        """Show the dashboard."""

        # frames
        self.options_frame()
        self.title_frame("Asclepius")
        self.navigation_frame()

        self.center_window()
        self.root.mainloop()
