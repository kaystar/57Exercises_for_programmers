# !python3
# Numbers to names

calendar = {'January': '1',
            'February': '2',
            'March': '3',
            'April': '4',
            'May': '5',
            'June': '6',
            'July': '7',
            'August': '8',
            'September': '9',
            'October': '10',
            'November': '11',
            'December': '12'}

num = int(input("Please enter a number for the month: \n"))


if num in calendar:
    month_name = calendar[num]
    message = "\nThe name of the month is " + month_name + "."
else:
    message = "\nPlease enter the correct number of month."

print(message)