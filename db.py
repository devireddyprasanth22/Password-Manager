import sqlite3 as db

def db_setup():
    #create a usr databse and check if databae creation is successful
    connection = db.connect("usr.db")
    print(connection.total_changes)
    # cursor object can send sql commands to database and table structure defined
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usr_details (username TEXT NOT NULL, email TEXT, password TEXT NOT NULL, application TEXT NOT NULL)")
    connection.commit()

def add_user(username, email, password, application):
    connection = db.connect("usr.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO usr_details (username, email, password, application) VALUES (?,?,?,?)", (username, email, password, application))
    connection.commit()

# def find_user():

# def del_user():

