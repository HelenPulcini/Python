from time import sleep
from add import *
from deleteJob import *
from update import *
from read import *

def menuOptions():
    menu = \
    """

    Please select one of the options below

        1. Display Jobs List
        2. Add a New Job Application
        3. Delete an Existing Entry
        4. Update an Existing Entry
        5. Exit Application

    """

    options = ["1", "2", "3", "4", "5"]

    choice = 0
    while choice not in options:
        print(menu)
        choice = input("Please Enter Your Option: ")
        if choice not in options:
            print(choice, "is not a valid option. Please try again.")
            sleep(2)
    return choice
        
mainProgram = True
while mainProgram:
    userChoice = menuOptions() #userChoice is what menuOptions returns
    if userChoice == "1":
        read()
    elif userChoice == "2":
        addJob()
    elif userChoice == "3":
        deleteIt()
    elif userChoice == "4":
        updateJob()
    else:
        mainProgram = False

