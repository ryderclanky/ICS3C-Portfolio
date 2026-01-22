# Step 1: Create a list called 'foods' that stores 5 of your favourite foods.
# Example: foods = ["pizza", "tacos", "pasta", "ice cream", "sushi"]
foods = ["pizza", "tacos", "pasta", "pierogis", "sushi"]


# Step 2: Print the entire list.
print(foods)


# Step 3: Print the FIRST and LAST food using their index numbers.
# Hint: The first item is index 0, and the last one is index 4 (if you have 5 items).
print(foods[0])
print(foods[4])


# Step 4: Use len() to find how many foods are in your list.
print(len(foods))


# Step 5: Use a for loop to print each food on its own line.
for food in foods:
    print(food)


#Bonus Challenge:
# - Add one more food to your list using append()
# - Print your list again to see the change.

foods.append("burgers")
print(foods)
