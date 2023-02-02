from connect import *

def read(): 
    cursor.execute("SELECT * FROM jobs")
    row = cursor.fetchall()
    for record in row:
        print(record)

if __name__ == "__main__": # to stop the function from auto run in other modules
   read()  