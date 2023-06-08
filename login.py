from tkinter import *
import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="rakshith",
    password="password",
    database="logindb"
)

# Create table if it doesn't exist
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")

def register_user():
    username_info = username.get()
    password_info = password.get()

    # Check if username already exists
    mycursor.execute("SELECT * FROM users WHERE username = %s", (username_info,))
    result = mycursor.fetchone()
    if result:
        Label(register_screen, text="Username already taken", fg="red", font=("calibri", 11)).pack()
        return

    # Insert user data into table
    mycursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username_info, password_info))
    mydb.commit()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_label = Label(register_screen, text="Username * ")
    username_label.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_label = Label(register_screen, text="Password * ")
    password_label.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command=register_user).pack()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title("Password not recognised")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Password Error").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(main_screen)
    user_not_found_screen.title("User not found")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()


        
def username_verify():
    return username_entry.get()

def password_verify():
    return password_entry.get()

def clear_entries():
    username_entry.delete(0, END)
    password_entry.delete(0, END)

def login():
    # Get username and password from entries
    username1 = username_verify()
    password1 = password_verify()

    # Check if username and password exist in table
    mycursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username1, password1))
    result = mycursor.fetchone()
    if result:
        clear_entries()
        main_screen.destroy()
        # Code to open another window or perform other actions after successful login
    else:
        clear_entries()
        password_not_recognised()
def mainscreen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Login or Register")

    Label(text="Choose Login or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()

    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()
