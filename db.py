import sqlite3 as db

def db_setup():
    #create a usr databse and check if databae creation is successful
    connection = db.connect("usr.db")
    print(connection.total_changes)
    # cursor object can send sql commands to database and table structure defined
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS acount (email TEXT NOT NULL, username TEXT, password TEXT NOT NULL, application TEXT NOT NULL)")
    connection.commit()

# def add_user():

# def find_user():

# def del_user():

