from connect import *
from read import *
from time import sleep

def deleteIt():
    read()

    sure = False

    while sure == False:
        givenID = input("Please enter the ID of the job to delete: ")
        print(f"The entry you want to delete is number {givenID}.")
        confirm = input("Is this correct? y/n  ")
        if confirm == "y" or confirm == "yes" or confirm == "Y":
            sure = True

    cursor.execute(f"DELETE FROM jobs WHERE jobID = {givenID}")
    connection.commit()

    print("Deleting the selected entry...")
    sleep(2)
    read()
if __name__ == "__main__": # to stop the function from auto run in other modules
   deleteIt() 
