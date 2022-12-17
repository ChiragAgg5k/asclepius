import sqlite3

from asclepius import dashboard, database, login_screen

login = login_screen.Login(
    appearance_mode="light", color_theme="green", width=450, height=350
)

# while True:
#     login.display()
#     if login.submit:
#         password = login.password.get()
#         enrollmentid = login.enrollment_id.get()
#         break

dash_board = dashboard.Dashboard(
    width=1280,
    height=720,
    appearance="dark",
    theme_color="green",
)

dash_board.show_dashboard(canvas_offset_width=(-460), canvas_offset_height=(-460))


print("Program exited successfully.")
