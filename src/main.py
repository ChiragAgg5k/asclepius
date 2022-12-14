from asclepius import dashboard, database, login_screen

database = database.Database()
med_data = database.get_medicines()

# login = login_screen.Login(
#     appearance_mode="light", color_theme="green", width=450, height=350
# )

# while True:
#     login.display()
#     if login.submit:
#         password = login.password.get()
#         username = login.username.get()

#         break

# print("Username: ", username)
# print("Password:", password)

dashboard = dashboard.Dashboard(
    width=1280, height=720, appearance="dark", theme_color="green", data=med_data
)
dashboard.show_dashboard()
