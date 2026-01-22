
# ask the user for inputs
end = int(input("Enter a number to count up to: "))
step = int(input("Enter a step amount: "))

# count by step amount
for i in range(0, end + 1, step):
    print(i)

print("Blast off!")
