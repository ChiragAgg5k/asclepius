# Code Working

The code is divided into different modules inside the package named _asclepius_, which are then combined to form the final code. The modules are:
## Dashboard

The custom Tkinter dashboard is a tool that provides a visual interface for analyzing and interpreting data in a project. It has a main class named Dashboard, which has an `__init__` function for defining the height, width, appearance, dataset, and header variables. These variables are used across other methods in the dashboard. The dashboard has different methods, such as `navigation`, `title`, `display`, and `change_appearance`.


## Login Screen

The custom Tkinter interface is used for the display. It takes the username and password from the user and checks if it is present in the database of the sign-up module. If the username and password are present, the user will be logged in and will be shown their respective dashboard.


## SignUp

The Sign-up window takes data from the user such as their name, enrollment ID, and phone number, and stores it. This data is further used for the login window.


## Database

The Database dashboard is used to display a database of medicines. It imports data from the "data" folder, which is stored in a .db (SQL) file, and converts it into basic data to display it to the user through the dashboard. The data folder has the database of medicines stored.


## Main file

The Main file is used to attach all the .py files and compile them together to show the whole result of the code. It first uses the login file, and if the login is successful, it shows the dashboard to the user. If the login is incorrect, the user has to sign up first and try again.
