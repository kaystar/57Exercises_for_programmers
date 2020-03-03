shopList = []
quantitylist = []
length = 3
tax = 5.5

def printing(subtot,vat,tot):
    print("Subtotal: {}, \n Tax: {}, \n Total: {}" .format(subtot,vat,tot))

def calculation(list_a, list_b):
    tax = 5.5
    subtotal = 0
    for x, y in zip(shopList, quantitylist):
        subtotal += x * y
    round(subtotal, 2)
    h = tax = round(subtotal * tax /100,2)
    round(tax, 2)
    total = subtotal + tax
    round(total, 2)
    printing(subtotal,h,total)

while len(shopList) < length:
    item = int(input("Please enter the price of item: "))
    shopList.append(item)
    quantity = int(input("How many?: "))
    quantitylist.append(quantity)

calculation(shopList,quantitylist)
