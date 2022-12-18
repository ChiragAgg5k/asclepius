import faulthandler

from asclepius import dashboard, home_screen

faulthandler.enable()

home_window = home_screen.HomeScreen(width=500, height=500)
home_window.show_homescreen()

dash_board = dashboard.Dashboard(
    width=1280,
    height=720,
    appearance="dark",
    theme_color="green",
    enrollment_id=home_window.get_user_enrollment_id(),
)

dash_board.show_dashboard()

print("Program exited successfully.")
