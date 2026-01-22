"""
Assignment 4 - List
Name: Ryder Armstrong
Date: December 13th 
________________________________________________________________________________________________
PART A
________________________________________________________________________________________________
Prompt the user to enter positive numbers repeatedly which represent test scores. 
Continue accepting float inputs until the user enters -1.  
Value -1 will act as a sentinel to stop the input process. 
Store all positive numbers entered by the user in a list.  
After input ends, loop through the list and print each number on a new line. - This needs to be completed for a Level 4  
Bonus: Calculate the average of the test scores – One bonus mark
"""

test_scores = []  

# keep asking until the user enters -1
while True:
    score = float(input("Enter test score (positive float, -1 to stop): "))

    # -1 stops the loop
    if score == -1:
        break

    # only positive numbers are added
    if score > 0:
        test_scores.append(score)

# show all test scores
print("\nTest scores entered:")
for score in test_scores:
    print(score)  


if len(test_scores) > 0:
    total = 0
    for score in test_scores:
        total = total + score  

    average = total / len(test_scores)
    print("The average is:", average)
else:
    print("No valid test scores were entered.")
    

"""
________________________________________________________________________________________________
PART B
________________________________________________________________________________________________
Prompt the user to enter words repeatedly. 
Continue accepting input until the user enters "quit".  
The word "quit" will act as a stop for the input process. 
Store all words entered by the user in a list. 
After input ends, display all the words in the list. 
Ask the user if they want to check whether a specific word exists in the list: - This needs to be completed for a level 4 Level 4 
If yes, prompt them to enter a word. 
Display whether the word is found in the list.  
You may assume that the names are all lowercase including the word quit – You will lose marks for using upper(), lower() or find() 
"""


names = []  

# keep asking until "quit" is entered
while True:
    word = input("Enter a word (type 'quit' to stop): ")

    # "quit" stops the loop
    if word == "quit":
        break

    # store the word
    names.append(word)

# show all words entered
print("\nWords entered:")
for name in names:
    print(name)

# ask if the user wants to check for a word
choice = input("\nDo you want to check if a name exists in the list? (yes/no): ")

if choice == "yes":
    check_name = input("Enter the name to check: ")

    found = False
    for name in names:
        if name == check_name:
            found = True

    if found:
        print(check_name, "is in the list!")
    else:
        print(check_name, "is not in the list.")