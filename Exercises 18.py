def convert_celsius(num):
    farenheit = round((num - 32) * (5 / 9),2)
    print("Your value was: {}, converted to Farenheit is: {}".format(num,farenheit))

def convert_farenheit(num):
    celsius = round((num * 9/5) + 32 ,2)
    print("Your value was: {}, converted to Farenheit is: {}".format(num,celsius))


temp = int(input("What is the temperature?: \n"))
print("Press C to convert from Celsius to Farenheit")
print(("Press F to convert from Farenheit to Celsius"))
unit = input("What unit would you want to convert to \n")

if unit.lower() == 'c':
    convert_celsius(temp)
elif unit.lower() == 'f':
    convert_farenheit(temp)
else:
    print("I'm not too sure what you entered")


