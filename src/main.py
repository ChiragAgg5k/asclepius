from asclepius import dashboard, login_screen

login_window = login_screen.Login(
    width=450, height=350, appearance_mode="light", color_theme="green"
)

while True:
    login_window.display()
    if login_window.submit:
        password, enrollment_id = login_window.get_credentials()
        break

dash_board = dashboard.Dashboard(
    width=1280,
    height=720,
    appearance="dark",
    theme_color="green",
)

dash_board.show_dashboard()


print("Program exited successfully.")
