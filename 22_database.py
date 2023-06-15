import sqlite3
import csv

def printDB():
    try:
        result = theCursor.execute("SELECT id, FName, LName, Age, Address, Salary, HireDate FROM Employees")
        for row in result: 
            print("ID: ", row[0])
            print("First Name: ", row[1])
            print("Last Name: ", row[2])
            print("Age: ", row[3])
            print("Address: ", row[4])
            print("Salary: ", row[5])
            print("Hire Date: ", row[6])
    except sqlite3.OperationError:
            print("The table doesn't exist")
    except:
        print("Couldn't get the data")
        
db_conn = sqlite3.connect('test.db')
print("Database Created")
theCursor = db_conn.cursor()

try: 
    db_conn.execute("CREATE TABLE Employees (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT, LName TEXT, Age INT NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")
    db_conn.commit()
    print("Table Created")
except sqlite3.OperationalError:
        print("Table Not Created")

db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate) VALUES ('John', 'Doe', 30, '123 Main St', 10000.00, '2000-01-01');")
db_conn.commit()
printDB()
db_conn.close()