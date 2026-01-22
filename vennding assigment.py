print("1 - Chips ($2.00)")
print("2 - Chocolate ($2.50)")
print("3 - Soda ($3.00)")

choice = input("Choose an item (1, 2, or 3): ")

if choice == "1":
    cost = 2.00
elif choice == "2":
    cost = 2.50
elif choice == "3":
    cost = 3.00
else:
    print("Invalid choice.")
    quit()

money = float(input("Insert money: $"))

if money < cost:
    print("Not enough money. Transaction cancelled.")
elif money == cost:
    print("Enjoy your item!")
else:
    change = money - cost
    print("Enjoy your item! Your change is $", round(change, 2))
