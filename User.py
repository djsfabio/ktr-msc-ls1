import re

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
TELEPHONE_REGEX = re.compile(
    r"^(?:(?:\+|00)33[\s.-]{0,3}(?:\(0\)[\s.-]{0,3})?|0)[1-9](?:(?:[\s.-]?\d{2}){4}|\d{2}(?:[\s.-]?\d{3}){2})$")


class User:

    def __init__(self, name="", company="", email="", telephone="", password=""):
        self.__name = name
        self.__company = company
        self.__email = email
        self.__telephone = telephone
        self.__password = password

    # Getters
    def get_name(self):
        return self.__name

    def get_company(self):
        return self.__company

    def get_email(self):
        return self.__email

    def get_telephone(self):
        return self.__telephone

    def get_password(self):
        return self.__password

    # Setters
    def set_name(self, newName):
        if len(newName) >= 5:
            self.__name = newName
        else:
            raise Exception(
                "Fill in a correct name and first name (At least 2 characters for the name and the first name separated by a space).")
            exit()

    def set_company(self, newCompany):
        if newCompany != "":
            if len(newCompany) <= 100:
                self.__company = newCompany.capitalize()
            else:
                raise Exception("Please enter a company name of less than 100 characters.")
                exit()

    def set_email(self, newEmail):
        if newEmail != "":
            if not EMAIL_REGEX.match(newEmail):
                raise Exception("Please enter a valid email address.")
                exit()
            else:
                self.__email = newEmail

    def set_telephone(self, newTelephone):
        if newTelephone != "":
            if not TELEPHONE_REGEX.match(newTelephone):
                raise Exception("Please enter a valid French number.")
                exit()
            else:
                self.__telephone = newTelephone

    def set_password(self, newPassword):
        if newPassword in " " == True:
            raise Exception("Please provide a valid password without space character.")
            exit()
        elif len(newPassword) < 6:
            raise Exception("Please provide a valid password without space character and with 6 characters at least.")
            exit()
        else:
            self.__password = newPassword
