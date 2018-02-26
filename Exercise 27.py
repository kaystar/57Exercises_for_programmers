# !python3

# Validating Input

import re

global valid
global check


def validate_input(fname, lname, id, zip):
    global valid
    global check
    name_checker(fname, lname)
    id_checker(id)
    zip_checker(zip)
    if valid == True:
        print("There were no errors found.")
    else:
        print(check)


def name_checker(fname, lname):
    global check
    global valid
    if fname == '':
       check = print("First name cannot be empty, please try again.")
       valid = False
    elif lname == '':
       check = print("Last name cannot be empty, please try again.")
       valid = False

    if len(fname) < 2:
        check = "'{}' is not a valid first name as it is too short, names must at least be 2 characters long." .format(fname)
        valid = False
    elif len(lname) < 2:
        check = "'{}' is not a valid last name as it is too short, names must at least be 2 characters long." .format(lname)
        valid = False


def id_checker(id):
    global check
    global valid
    id_regex = re.compile(r"\W{2}-\d{3}")
    if id_regex.search(id) == False:
        check = "{} isn't a correct ID format".format(id)
        valid = False


def zip_checker(zip):
    global check
    global valid
    zip_regex = re.compile(r"\d{5}")
    if zip_regex.search(zip) == False:
        check = "{} isn't a correct ZIP format" .format(zip)
        valid = False

while True:

    first_name = input("Please enter your first name: \n")
    last_name = input("Please enter your last name: \n")
    employee_id = input("Please enter your Employee ID: \n")
    zip_code = input("Please enter your ZIP Code \n")

    validate_input(first_name,last_name,employee_id,zip_code)

