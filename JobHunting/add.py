from connect import *
from read import *
from time import sleep

def addJob():
    appliedJobs = []

    print("Please enter the following information:")
    dateApplied = input("When did you apply? yyyy-mm-dd : ") 
    companyName = input("Company Name: ")
    location = input("Location: ")
    position = input("Position: ")
    salary = input("Salary: ")
    contact = input("Contact details: ")


    appliedJobs.append(dateApplied)
    appliedJobs.append(companyName)
    appliedJobs.append(location)
    appliedJobs.append(position)
    appliedJobs.append(salary)
    appliedJobs.append(contact)


    print(appliedJobs)

    cursor.execute("INSERT INTO jobs VALUES (NULL, ?, ?, ?, ?, ?, ?)", appliedJobs)

        # INSERT INTO tblfilms VALUES (NULL, "{appliedJobs[0]}", "{appliedJobs[1]}", "{appliedJobs[2]}", "{appliedJobs[3]}", "{appliedJobs[4]}")

    connection.commit()
    print(f"Your job application at '{companyName}' has been added")

    sleep(2)

    read()
if __name__ == "__main__": # to stop the function from auto run in other modules
    addJob() 