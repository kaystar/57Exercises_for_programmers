shopList = []
quantitylist = []
length = 3
tax = 5.5

def printing(subtot,vat,tot):
    print("Subtotal: {}, \n Tax: {}, \n Total: {}" .format(subtot,vat,tot))

def calculation(list_a, list_b):
    tax = 5.5
    itemTotal1 = list_a[0] * list_b[0]
    itemTotal2 = list_a[1] * list_b[1]
    itemTotal3 = list_a[2] * list_b[2]
    subtotal = itemTotal1 + itemTotal2 + itemTotal3
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



