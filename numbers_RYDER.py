# This program writes a list of numbers to a text file

numbers = [1, 2, 3, 4]

# open the file in write mode ("w")
with open("numbers.txt", "w") as file:
    # turn the list into a string and write it
    file.write(str(numbers))

print("Done! Check numbers.txt")
