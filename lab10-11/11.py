import psycopg2
from psycopg2 import Error
import csv

conn = psycopg2.connect(user="postgres",
                                password="gE%Jyq@p",
                                host="localhost",
                                port="5432",
                                database="phonebook")        
cursor = conn.cursor()

def act1():
    global query
    query = """SELECT * FROM contacts
    WHERE """
    mode = input("Do you want to search by name or phone? ")
    try:
        if mode == "name":
                query += "name"
                substr = input("Enter letter: ")
                query += " iLIKE '{}%'".format(substr)
                cursor.execute(query+";")
                print(cursor.fetchall())
        elif mode == "phone":
                query += "phone"
                number = input("Enter number: ")
                query += " iLIKE '%{}%'".format(substr)
                cursor.execute(query+";")
                print(cursor.fetchall())
        cursor.close()
        conn.commit()        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def act2(name, phone):
    try:
        while True:
            cursor.execute("SELECT COUNT(*) FROM contacts WHERE name = %s", (name,))
            count = cursor.fetchone()[0]
            if count == 0:
                cursor.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
            else:
                mode = input("Seems like user already exists. Do you want to update? ")
                if mode.lower() == "yes":
                    phone = input("Enter new phone number: ")
                    cursor.execute("UPDATE contacts SET phone = %s WHERE name = %s", (phone, name))
                else:
                    break
            conn.commit()
            cursor.close()
            print("Contact added successfully!")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error adding contact:", error)
    finally:
        if conn is not None:
            conn.close()

def act3():
    try:
        banned = []
        while True: 
                print("Want to enter a listyes? yes/no")
                mode = input()
                if mode == "no":
                    break
                print("Enter users' name and phone: ")
                person = input().split()
                if len(person)>2:
                    banned.append(person)
                    continue
                if not person[1].isdigit():
                    banned.append(person)
                    continue
                act2(person[0], person[1])
            
        if len(banned) == 0:
            return
        print("This data were not added due to incorrect format:")
        for i in banned:
            print(i)
        conn.commit()
        cursor.close()
        print("Contact added successfully!")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
   
def act4():
    mode = input("Do you need offset? ")
    if mode.lower() == "yes":
        offset = int(input("Enter offset: "))
        query = """SELECT * FROM contacts OFFSET {}""".format(offset)
        cursor.execute(str(query))
        print(cursor.fetchall())
    mode = input("Do you need limit? ")
    if mode.lower() == "yes":
        limit = int(input("Enter limit:"))
        query = """SELECT * FROM contacts LIMIT {}""".format(limit)
        cursor.execute(str(query))
        print(cursor.fetchall())
    

def act5():
    mode = input("Do you want to delete by name or phone? ")
    try:
        if mode == "name":
            name = input("Enter name to delete: ")
            cursor.execute(
                    f"""DELETE FROM contacts WHERE name = '{name}'"""
                )         
        elif mode == "phone":
            phone = input("Enter phone to delete: ")
            cursor.execute(
                    f"""DELETE FROM contacts WHERE phone = '{phone}'"""
                )
        print("Deleted successfully!")   
        cursor.close()
        conn.commit()        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



print("""       1 to search data
                2 to insert new user by name and phone/update
                3 to add users by list of name and phone
                4 querying data with pagination
                5 to delete by username or phone
            """)
action = input("""What do you want to do?: """)
match action:
    case "1": act1()
    case "2":
        name = input("Enter user's name: ")
        phone = input("Enter user's phone number: ")
        act2(name, phone)
    case "3": act3()
    case "4": act4()
    case "5": act5()
