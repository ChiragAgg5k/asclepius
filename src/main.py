from asclepius import dashboard, database, login_screen

database = database.Database()
med_data = database.get_medicines()

login = login_screen.Login(
    appearance_mode="light", color_theme="green", width=450, height=350
)

dash_board = dashboard.Dashboard(
    width=1280,
    height=720,
    appearance="dark",
    theme_color="green",
    dataset=med_data,
    col_headers=database.get_col_headings("medicines"),
)

while True:
    login.display()
    if login.submit:
        password = login.password.get()
        enrollmentid = login.enrollment_id.get()
        break

while True:
    dash_board.display()
    if dash_board.submit:
        break

print("Program exited successfully.")
print(dash_board.order_list)
