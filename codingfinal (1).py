
import random


# player stats
player_health = 100
MAX_HEALTH = 100


# enemy progression

enemy_health_levels = [30, 50, 100]
current_enemy = 0

 
# items
 
inventory = []
enemy_drops = ["Potion", "Gem", "Diamond"]

game_running = True


 
# menus
 
def show_menu():
    print("\n=== MAIN MENU ===")
    print("1. Fight enemy")
    print("2. Explore")
    print("3. Inventory")
    print("4. Quit")


 
# combat
 
def choose_attack():
    print("\nChoose your attack:")
    print("1. Fire (12 damage)")
    print("2. Ice (8 damage)")
    print("3. Lightning (15 damage)")

    choice = input("Attack choice: ")

    if choice == "1":
        return 12
    elif choice == "2":
        return 8
    elif choice == "3":
        return 15
    else:
        print("Invalid choice. You missed!")
        return 0


def fight_enemy(enemy_health):
    global player_health

    print("\nAn enemy appears!")
    print("Enemy health:", enemy_health)

    while enemy_health > 0 and player_health > 0:
        damage = choose_attack()
        enemy_health -= damage
        print("Enemy health:", enemy_health)

        if enemy_health <= 0:
            return True

        player_health -= 5
        print("Your health:", player_health)

    return False


 
# explore 
 
def explore():
    print("\nWhere do you want to explore?")
    print("1. Abandoned house")
    print("2. Dark forest")
    print("3. Old cave")

    place = input("Choose a place: ")

    if place not in ["1", "2", "3"]:
        print("Invalid location.")
        return

    print("You rummaged through the area...")

    chance = random.randint(1, 100)

    if chance <= 70:
        item = random.choice(["Tin Can", "Old Boot"])
    else:
        item = random.choice(["Potion", "Diamond", "Gem"])

    inventory.append(item)
    print("You found:", item)


 
# inventory
 
def inventory_menu():
    global player_health

    while True:
        print("\n=== INVENTORY ===")

        if len(inventory) == 0:
            print("Inventory is empty.")
            return

        for i in range(len(inventory)):
            print(i + 1, "-", inventory[i])

        print("0 - Exit inventory")

        choice = input("Select an item number: ")

        if choice == "0":
            return

        if not choice.isdigit():
            print("Please enter a number.")
            continue

        index = int(choice) - 1

        if index < 0 or index >= len(inventory):
            print("That item does not exist.")
            continue

        item = inventory[index]
        print("You selected:", item)

        if item == "Potion":
            player_health += 20
            if player_health > MAX_HEALTH:
                player_health = MAX_HEALTH
            print("You used a Potion. Health:", player_health)
            inventory.pop(index)

        elif item == "Diamond" or item == "Gem":
            print("You shine the", item + ". It sparkles ✨")

        else:
            print("You look at the", item + ". Nothing happens.")


 
# main Game Loop
 
print("Welcome To RPG Game!!")

while game_running:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        if current_enemy < len(enemy_health_levels):
            enemy_health = enemy_health_levels[current_enemy]
        else:
            enemy_health = enemy_health_levels[-1] + (current_enemy - 2) * 50

        won = fight_enemy(enemy_health)

        if won:
            print("Enemy defeated!")

            drop = random.choice(enemy_drops)
            inventory.append(drop)
            print("The enemy dropped:", drop)

            current_enemy += 1
        else:
            print("You died!")
            game_running = False

    elif choice == "2":
        explore()

    elif choice == "3":
        inventory_menu()

    elif choice == "4":
        print("Goodbye.")
        game_running = False

    else:
        print("Invalid choice.")

print("Game over.")
