from connect import *
from read import *
import time

def updateJob():
    read()
    idField = input("Enter the jobID of the job to be updated: ")   

    def inputField():
        fieldName = input(
            f"Which field would you like to update (Date/Company/Location/Position/Salary/Contact)? \n You can type the first three character: ").title()
        newFieldValue = input(f"Enter the new value for: {fieldName}: ")
        # add single quotes to newFieldValue to match the data in the table
        newFieldValue = "'" + newFieldValue + "'"
        if fieldName == "Date" or fieldName == "date" or fieldName == "dat":
            cursor.execute(
                f"UPDATE jobs SET dateApplied = {newFieldValue} WHERE jobID = {idField}")
        elif fieldName == "Company" or fieldName == "company" or fieldName == "com":
            cursor.execute(
                f"UPDATE jobs SET companyName = {newFieldValue} WHERE jobID = {idField}")
        elif fieldName == "Position" or fieldName == "position" or fieldName == "pos":
            cursor.execute(
                f"UPDATE jobs SET position = {newFieldValue} WHERE jobID = {idField}")
        elif fieldName == "Location" or fieldName == "location" or fieldName == "loc":
            cursor.execute(
                f"UPDATE jobs SET location = {newFieldValue} WHERE jobID = {idField}")
        elif fieldName == "Salary" or fieldName == "salary" or fieldName == "sal":
            cursor.execute(
                f"UPDATE jobs SET salary = {newFieldValue} WHERE jobID = {idField}")
        elif fieldName == "Contact" or fieldName == "contact" or fieldName == "con":
            cursor.execute(
                f"UPDATE jobs SET contact = {newFieldValue} WHERE jobID = {idField}")
        connection.commit()
        done = print(f"Record {idField} updated in the jobs table")
        time.sleep(1)
        read()
        confirm = input(
            "Would you like to update other fields in the same jobID? y/n  ")
        if confirm == "y" or confirm == "yes" or confirm == "Y":
            inputField()
        else:
            updateJob()

    inputField()

if __name__ == "__main__":
    updateJob()
