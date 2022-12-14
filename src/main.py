from asclepius import dashboard, database, login_screen

login = login_screen.Login(
    appearance_mode="light", color_theme="green", width=450, height=350
)

while True:
    login.display()
    if login.submit:
        password = login.password.get()
        enrollmentid = login.enrollment_id.get()

        break

print("Enrollment ID: ", enrollmentid)
print("Password:", password)

database = database.Database()
med_data = database.get_medicines()

dashboard = dashboard.Dashboard(
    width=1280,
    height=720,
    appearance="dark",
    theme_color="green",
    dataset=med_data,
    col_headers=database.get_col_headings("medicines"),
)
dashboard.show_dashboard()
