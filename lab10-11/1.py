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
    try:
        with open("C:/data.csv") as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            for row in reader:
                print(f"Inserting row: {row}")
                cursor.execute(
                    """INSERT INTO contacts(id, name, phone) VALUES (%s,%s,%s)""", row
                )
        print("Data added successfully!")
        cursor.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def act2():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    try:
        cursor.execute(
            f"""INSERT INTO contacts (name, phone) VALUES ('{name}','{phone}' )
            """
        )
        print("Contact added successfully!")
        cursor.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def act3():
    try:
        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        id = input("Enter the id to update: ")
        column = input("What do you want to update?: ")
        new_value = input("Enter the new value: ")
        cursor.execute("""
                UPDATE contacts
                SET {}='{}'
                WHERE id='{}'
            """.format(column, new_value, id))
        print("Contact updated successfully!")
        cursor.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def act4():
    query = input("How do you want to get the data? ")
    try:
        if query not in ["id", "name", "phone"]:
            print("Invalid query.")
            return    
        cursor.execute(f"SELECT id, name, phone FROM contacts ORDER BY {query}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def act5():
    name = input("Enter name: ")
    try:
        cursor.execute(
            f"""DELETE FROM contacts WHERE name = '{name}'"""
        )
        print("Contact deleted successfully!")
        cursor.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

print("""       1 to add CSV file
                2 to write new data from console
                3 to update data
                4 quering data 
                5 to delete by username
            """)
action = input("""What do you want to do?: """)
match action:
    case "1": act1()
    case "2": act2()
    case "3": act3()
    case "4": act4()
    case "5": act5()