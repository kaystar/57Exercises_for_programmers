# !python3
#
# Exercise 38 - Filtering Values

numbers = []
even_list = []

def calculate():
    for i in numbers:
        if i % 2 == 0:
            even_list.append(i)
    print("The even numbers are: " + str(even_list))

def main():
    while True:
        entry = int(input("Enter a number [0 to stop entry] : "))
        if entry == 0:
            calculate()
            break
        numbers.append(entry)

if __name__ == "__main__":
    main()
