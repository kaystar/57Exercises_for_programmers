# !python3

# Alcohol Content calculator

menDist = 0.73
womenDist = 0.66
bac_limit = 0.08

weight = float(input("Please enter your weight: \n"))
gender = str(input("Please enter your gender:\n "))
noOfDrinks = int(input("How many drinks have you had?:\n "))
alcoholByVolume = float(input("Amount of units in alcohol: \n"))
timeSinceLastDrink = float(input("Time since last drink: \n"))

if gender.lower() == 'm' or gender.lower() == "male":
	r = 0.73
elif gender.lower() == 'f' or gender.lower() == "female":
	r = 0.6
else:
	print("please enter a correct gender.")


alcoholContent = (alcoholByVolume * 5.14 / weight * menDist) - 0.15 * timeSinceLastDrink

if alcoholContent >= 0:
	message1 = "\nyour blood alcohol content: " + str(bac_limit)
else:
	message1 = "\nyour blood alcohol content: 0"

if alcoholContent < bac_limit:
	message2 = "\nIt is legal for you to drive."
else:
	message2 = "\nIt is not legal for you to drive."

print(message1, message2)
