price = int(input("Enter the price of the bike: "))


if price > 100000:
    tax = 0.15 * price
    print("The road tax is:", tax)
elif price > 50000 and price <= 100000:
    tax = 0.10 * price
    print("The road tax is:", tax)
else:
    tax = 0.05 * price
    print("The road tax is:", tax)