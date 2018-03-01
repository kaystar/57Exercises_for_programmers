# !python3

# Exercise 34 - Employee List Removal

employee_list = ['John Smith',
                'Jackie Jackson',
                'Chris Jones',
                'Amanda Cullen',
                'Jeremy Goodwin'
                ]

def add_employee():
    while True:
        employee_to_add = input("Enter the name of the employee you would like to add: \n")
        employee_list.append(employee_to_add)
        main()

def remove_employee():
    while True:
        employee_to_remove = input("Enter an employee name to remove: \n")
        if employee_to_remove not in employee_list:
            print("Sorry that employee doesn't seem to be in our database. Please try again.")
            continue
        employee_list.remove(employee_to_remove)
        main()

def main():
    print("There are " + str(len(employee_list)) + " employees: ")
    print('\n'.join(employee_list))
    add_or_remove = input("Would you like to add or remove an employee? [Add or A / Remove or R] : \n")

    if add_or_remove.lower() in ['add', 'a']:
        add_employee()
    elif add_or_remove.lower() in ['remove', 'r']:
        remove_employee()
    else:
        return("What?")

if __name__ == "__main__":
    main()



