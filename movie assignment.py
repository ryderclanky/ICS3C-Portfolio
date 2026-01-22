age = int(input("Enter your age: "))
student = input("Are you a student? (yes/no): ").lower()

if age < 12:
    price = 8
elif age <= 17:
    price = 10
elif age <= 64:
    price = 12
else:
    price = 6

if student == "yes" and age > 12:
    price -= 2

print("Final ticket price: $", price)
