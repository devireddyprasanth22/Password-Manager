import sqlite3 as db

def db_setup():
    try:
        connection = db.connect("usr.db")
        print(connection.total_changes)
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS usr_details (username TEXT NOT NULL, email TEXT, password TEXT NOT NULL, application TEXT NOT NULL)")
        connection.commit()
    except db.Error as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def add_user(username, email, password, application):
    try:
        db_setup()
        connection = db.connect("usr.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO usr_details (username, email, password, application) VALUES (?,?,?,?)", (username, email, password, application))
        connection.commit()
    except db.Error as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def find_user(application):
    try:
        connection = db.connect("usr.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM usr_details WHERE application = ?", (application,))
        result = cursor.fetchall()
        if result:
            for row in result:
                return list(row)
        else:
            print("No users found for application:", application)
    except db.Error as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def change_password(email, username, new_password):
    try:
        connection = db.connect("usr.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE usr_details SET password = ? WHERE email = ? AND username = ?", (new_password, email, username))
        connection.commit()
    except db.Error as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def del_user(email, username, password, application):
    try:
        connection = db.connect("usr.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM usr_details WHERE email = ? AND username = ? AND password = ? AND application = ?", (email, username, password, application))
        connection.commit()
    except db.Error as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def verify(email, username, password):
    try:
        connection = db.connect("usr.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM usr_details WHERE email = ? AND username = ? AND password = ?", (email, username, password))
        result = cursor.fetchall()
        if result:
            print('Verified!')
        else:
            print("Incorrect credentials")
    except db.Error as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def all_users():
    connection = db.connect("usr.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM usr_details")
    # Fetch all rows from the executed query
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()