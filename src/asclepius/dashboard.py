import customtkinter as ctk
from PIL import Image


class Dashboard:
    def __init__(self, width: int, height: int) -> None:
        self.root = ctk.CTk()
        self.root.title("Asclepius")
        self.root.resizable(False, False)
        self.height = height
        self.width = width

        self.op_font = ctk.CTkFont(
            family="Microsoft Sans Serif", size=30, weight="bold"
        )
        self.title_font = ctk.CTkFont(
            family="Microsoft Sans Serifs", size=60, weight="bold"
        )

    def center_window(self) -> None:
        """Center the window."""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coord = (screen_width / 2) - (self.width / 2)
        y_coord = (screen_height / 2) - (self.height / 2)
        self.root.geometry(f"{self.width}x{self.height}+{int(x_coord)}+{int(y_coord)}")

    def options_frame(self) -> None:
        """Create the options frame."""
        self.options_frame = ctk.CTkFrame(
            self.root, width=200, height=self.height, corner_radius=15
        )

        self.options_frame.pack(side="left", fill="y", padx=(20, 0), pady=20)
        options_title = ctk.CTkLabel(
            self.options_frame, text="Options", font=self.op_font, corner_radius=10
        )

        options_title.grid(row=0, column=0, padx=20, pady=20)

    def title_frame(self, title):
        self.title_frame = ctk.CTkFrame(
            self.root, width=self.width - 200, height=50, corner_radius=10
        )
        self.title_frame.pack(side="top", fill="x", padx=20, pady=20)
        title_label = ctk.CTkLabel(self.title_frame, text=title, font=self.title_font)
        title_label.grid(row=0, column=0, padx=20, pady=20)

    def main_frame(self):
        self.main_frame = ctk.CTkFrame(
            self.root, width=self.width - 200, height=self.height - 50, corner_radius=10
        )
        self.main_frame.pack(side="bottom", fill="both", padx=20, pady=(0, 20))

    def show_dashboard(self) -> None:
        self.options_frame()
        self.title_frame("Dashboard")
        self.main_frame()
        self.center_window()
        self.root.mainloop()
