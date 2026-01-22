price = float(input("Price of item: "))
tax_rate = float(input("Tax rate (decimal): "))

tax = price * tax_rate
total = price + tax

print("Price:", price)
print("Tax:", tax)
print("Total: $", total)