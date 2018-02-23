principal_amount = int(input("Input the principle amount: "))
interest = float(input("Input the interest rate: "))
years = int(input("Input the number of years: "))


solution = principal_amount + (1 + (interest * years))

print("After {} years at {}% this investment will be worth {}" .format(years,interest,solution))