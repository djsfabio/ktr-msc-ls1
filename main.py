#!/Users/fabiodjs/.local/share/virtualenvs/ktr-msc-ls1-7epH9NVt/bin/python

import csv
import getpass
import os
import time
from pathlib import Path

import pyfiglet
from termcolor import colored

from Contact import Contact
from User import User


def main():
    running = True
    while running:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored(pyfiglet.figlet_format("The Business Card Manager", font="slant"), "cyan"))
        print(colored("[1] ", "blue"), "Log In")
        print(colored("[2] ", "green"), "Create New Profile")
        print(colored("[3] ", "red"), "Exit")
        runningChoice = True
        while runningChoice:
            # Catch the case that isn't a digit
            try:
                userChoice = int(input("\nPlease choose one of the following options : "))
            except:
                userChoice = -1

            if 1 <= userChoice <= 3:
                runningChoice = False
            else:
                print("Please select a value between 1 and 3.")

        if userChoice == 1:
            login()

        elif userChoice == 2:
            create_user()

        elif userChoice == 3:
            exit_program()


def login():
    """
    Function allowing to connect to the service by verifying that the user exists and uses the correct password.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(pyfiglet.figlet_format("Log In", font="slant"), "cyan"))
    notLogIn = True
    while notLogIn:
        userId = input("Please enter your login ID : ")
        userPswd = getpass.getpass('Please enter your password : ')
        listOfUsers = get_list_of_users()
        for aUser in listOfUsers:
            if userId == aUser.get_name() and userPswd == aUser.get_password():
                actualUser = aUser
                notLogIn = False
                break
        print("The id of connexion or the password you’ve entered is incorrect. Please try again.")
    choice_page_logIn(userId)


def choice_page_logIn(userId):
    """
    Choice page allowing actions to be performed once logged in.
    :param userId: ID of the user we are logged in.
    :return:
    """
    loginPage = True
    while loginPage:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored(pyfiglet.figlet_format("Welcome " + userId, font="slant"), "cyan"))
        print(colored("[1] ", "blue"), "Add a contact")
        print(colored("[2] ", "green"), "See my library")
        print(colored("[3] ", "red"), "Log out")
        runningChoiceLogIn = True
        while runningChoiceLogIn:
            try:
                userChoiceLogin = int(input("\nPlease choose one of the following options : "))
            except:
                userChoiceLogin = -1
            if 1 <= userChoiceLogin <= 3:
                runningChoiceLogIn = False
            else:
                print("Please select a value between 1 and 3.")
        if userChoiceLogin == 1:
            create_contact(userId)
        elif userChoiceLogin == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colored(pyfiglet.figlet_format("Library of " + userId, font="slant"), "green"))
            listOfContacts = get_library(userId)
            for contact in listOfContacts:
                print(colored("--------------------------------", "green", "on_green"))
                print("Name :", contact.get_name())
                print("Company :", contact.get_company())
                print("E-Mail :", contact.get_email())
                print("Telephone :", contact.get_telephone())
            print(colored("--------------------------------", "green", "on_green"))
            input("To return to the previous page, please press the enter key.")
        elif userChoiceLogin == 3:
            loginPage = False


def create_user():
    """
    Allows you to create a new user for the service.
    """
    newUser = User()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(pyfiglet.figlet_format("Create New Profile", font="slant"), "green"))
    name = input(colored("[Mandatory]", "red") + " Name : ")
    newUser.set_name(name)
    company = input("(Optionnal) Company : ")
    newUser.set_company(company)
    email = input("(Optionnal) E-Mail : ")
    newUser.set_email(email)
    telephone = input("(Optionnal) Telephone : ")
    newUser.set_telephone(telephone)
    password = getpass.getpass(colored('[Mandatory]', "red") + ' Password : ')
    newUser.set_password(password)

    print("The profile has been create with the following informations : ")
    print(colored("--------------------------------", "green", "on_green"))
    print("Name :", newUser.get_name())
    print("Company :", newUser.get_company())
    print("E-Mail :", newUser.get_email())
    print("Telephone :", newUser.get_telephone())
    print(colored("--------------------------------", "green", "on_green"))

    add_user(newUser)

    print("Back to the home page...")
    time.sleep(3)


def exit_program():
    """
    Allows you to exit the program running.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(pyfiglet.figlet_format("We hope to see you very soon.", font="slant"), "cyan"))
    exit()


def create_contact(userId):
    """
    Allows you to create a new contact for the current user's library.
    :param userId: ID of the user on whom we want to create a new contact.
    """
    newContact = Contact()
    os.system('cls' if os.name == 'nt' else 'clear')

    print(colored(pyfiglet.figlet_format("Add a new contact", font="slant"), "green"))
    name = input("(Optionnal) Name : ")
    newContact.set_name(name)
    company = input("(Optionnal) Company : ")
    newContact.set_company(company)
    email = input(colored("[Mandatory]", "red") + " E-Mail : ")
    newContact.set_email(email)
    telephone = input("(Optionnal) Telephone : ")
    newContact.set_telephone(telephone)

    print("The contact has been create with the following informations : ")
    print(colored("--------------------------------", "green", "on_green"))
    print("Name :", newContact.get_name())
    print("Company :", newContact.get_company())
    print("E-Mail :", newContact.get_email())
    print("Telephone :", newContact.get_telephone())
    print(colored("--------------------------------", "green", "on_green"))

    add_contact(newContact, userId)

    print("Back to the previous page...")
    time.sleep(3)


def add_user(user):
    """
    Add a new user to the users.csv file
    :param user: The user we want to add in the csv file
    """
    with open('users.csv', 'a+') as file:
        writer = csv.writer(file)
        writer.writerow(
            [user.get_name(), user.get_company(), user.get_email(), user.get_telephone(), user.get_password()])


def add_contact(contact, userId):
    """
    Add a new contact in the library of the current user
    :param contact: Is the contact we want to add
    :param userId: Is the current user name
    """
    with open(userId + '_library.csv', 'a+') as file:
        writer = csv.writer(file)
        writer.writerow(
            [contact.get_name(), contact.get_company(), contact.get_email(), contact.get_telephone()])


def get_library(userId):
    """
    Get the contact library linked to the user passed in parameter
    :param userId:Is the current user name.
    :return:
    """
    listOfContacts = []
    my_file = Path("./" + str(userId) + "_library.csv")
    if my_file.is_file():
        with open(userId + '_library.csv', 'r') as fp:
            reader = csv.reader(fp, delimiter=',')

            for eachRow in reader:
                newContact = Contact()

                newContact.set_name(eachRow[0])
                newContact.set_company(eachRow[1])
                newContact.set_email(eachRow[2])
                newContact.set_telephone(eachRow[3])
                listOfContacts.append(newContact)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Please create a contact to see your library.", "red"))
        exit()
    return listOfContacts


def get_list_of_users():
    """
    Get the list of all the users stocked in the users.csv file.  
    """
    listOfUsers = []
    my_file = Path("./users.csv")
    if my_file.is_file():
        with open('users.csv', 'r') as fp:
            reader = csv.reader(fp, delimiter=',')

            for eachRow in reader:
                newUser = User()

                newUser.set_name(eachRow[0])
                newUser.set_company(eachRow[1])
                newUser.set_email(eachRow[2])
                newUser.set_telephone(eachRow[3])
                newUser.set_password(eachRow[4])
                listOfUsers.append(newUser)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Please create a profile before logging in.", "red"))
        exit()
    return listOfUsers


if __name__ == '__main__':
    main()
