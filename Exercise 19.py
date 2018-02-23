# !python3

# BMI Calculator

weight = int(input("What is your weight?\n"))
height = int(input("What is your height?\n"))

bmi = (weight / (height * height)) * 703

if bmi >= 18.5 and bmi <= 25:
    print("Your BMI is: {}, you are of normal weight range" .format(bmi))
elif bmi < 18.5:
    print("Your BMI is {}, you are underweight, you should see your doctor".format(bmi))
else:
    print("Your BMI is {}, you're overweight, you should see your doctor".format(bmi))