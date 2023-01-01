"""Centers window the tkinter window passed"""
import customtkinter as ctk


def center_window(root: ctk.CTk, width: int, height: int) -> None:
    """Centers window the tkinter window passed

    Args:
        root (ctk.CTk): tkinter window
        width (int): width of the window
        height (int): height of the window
    """

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coord = (screen_width / 2) - (width / 2)
    y_coord = (screen_height / 2) - (height / 2)
    root.geometry(f"{width}x{height}+{int(x_coord)}+{int(y_coord)}")
