from asclepius import dashboard, database

db = database.Database()

dashboard = dashboard.Dashboard(
    width=1280, height=720, appearance="System", theme_color="green"
)
dashboard.show_dashboard()
