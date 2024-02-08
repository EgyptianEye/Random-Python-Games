import random

player_name = input("Enter your name: ")

player_health = 100
player_attack = 10
player_defense = 0
player_points = 0

healing_potion_uses = 2
time_stop_uses = 1
shield_uses = 1
banana_uses = 1
bomb_uses = 1

enemies = [
    {"name": "Goblin", "health": 50, "attack": 5, "max_health": 50, "points": 10},
    {"name": "Orc", "health": 80, "attack": 8, "max_health": 80, "points": 20},
    {"name": "Dragon", "health": 200, "attack": 15, "max_health": 200, "points": 50},
    {"name": "Troll", "health": 100, "attack": 10, "max_health": 100, "points": 30},
    {"name": "Giant", "health": 150, "attack": 12, "max_health": 150, "points": 40}
]

enemy_frozen_turns = 0

def get_health_color(health, max_health):
    percentage = (health / max_health) * 100

    if percentage >= 50:
        return "\033[92m"  # Green
    elif percentage >= 25:
        return "\033[93m"  # Yellow
    else:
        return "\033[91m"  # Red

def display_health(name, health, max_health):
    color_code = get_health_color(health, max_health)
    health_bar_length = health // 5
    health_bar = '#' * health_bar_length
    print(f"{name} Health: {color_code}{health} |{health_bar}|\033[0m")

def attack(enemy):
    enemy["health"] -= player_attack
    print(f"You attacked the {enemy['name']} for {player_attack} damage.")

def defend(enemy):
    global player_health
    damage = max(0, enemy["attack"] - player_defense)
    player_health -= damage
    print(f"The {enemy['name']} attacked you for {damage} damage.")

def use_item(item, enemy):
    global healing_potion_uses, shield_uses, time_stop_uses, banana_uses, bomb_uses
    if item == "1":
        if healing_potion_uses > 0:
            heal_item()
            healing_potion_uses -= 1
        else:
            print("You have no more uses of Healing Potion.")
    elif item == "2":
        if shield_uses > 0:
            defense_item()
            shield_uses -= 1
        else:
            print("You have no more uses of Shield of Protection.")
    elif item == "3":
        if time_stop_uses > 0:
            time_item()
            time_stop_uses -= 1
        else:
            print("You have no more uses of Time Stopper.")
    elif item == "4":
        if banana_uses > 0:
            banana_item(enemy)
            banana_uses -= 1
        else:
            print("You have no more uses of Banana.")
    elif item == "5":
        if bomb_uses > 0:
            bomb_item(enemy)
            bomb_uses -= 1
        else:
            print("You have no more uses of Bomb.")
    else:
        print("Invalid item. Try again.")

def heal_item():
    healing_amount = 30
    global player_health
    player_health = min(100, player_health + healing_amount)
    print(f"You used a Healing Potion and recovered {healing_amount} health.")

def defense_item():
    global player_defense
    if player_defense == 0:
        player_defense = player_attack // 2
        print("You used the Shield of Protection. Your defense is increased.")
    else:
        print("You are already protected by the shield. It will not stack.")

def time_item():
    global enemy_frozen_turns
    if enemy_frozen_turns == 0:
        enemy_frozen_turns = 3
        print("You used the Time Stopper. The enemy's turns are frozen for 2 turns.")
    else:
        print("The enemy is already frozen. Wait for their turns to resume.")

def banana_item(enemy):
    global player_health
    chance = random.random()
    if chance < 0.5:
        enemy["health"] = 0
        print("The enemy slipped on the banana peel and died!")
    else:
        player_health -= 20
        print("Oops, the enemy ate the banana and punched you in the face!")

def bomb_item(enemy):
    global bomb_uses
    if bomb_uses > 0:
        damage = random.randint(20, 50)
        enemy["health"] -= damage
        print(f"You used a Bomb and dealt {damage} damage to the enemy.")
        bomb_uses -= 1
    else:
        print("You have no more uses of Bomb.")

def run_away():
    print("You ran away from the battle.")

def game_over():
    print("\nYou lost, lol!")
    exit()

def game_won():
    print("\nCongratulations, you're a true NERD HAAAAAAAHAHA")
    exit()

def battle(enemy):
    global enemy_frozen_turns, player_points
    enemy_frozen_turns = 0
    print(f"A wild {enemy['name']} appeared!")
    while player_health > 0 and enemy["health"] > 0:
        print("\n---------------------------")
        display_health(player_name, player_health, 100)
        display_health(enemy["name"], enemy["health"], enemy["max_health"])
        print("---------------------------\n")

        print("Actions: 1. Attack, 2. Defend, 3. Use Item, 4. Run Away")
        action = input("Enter your action: ")

        if action == "1":
            attack(enemy)
            if enemy["health"] > 0 and enemy_frozen_turns == 0:
                defend(enemy)
        elif action == "2":
            if enemy_frozen_turns == 0:
                defend(enemy)
        elif action == "3":
            print("Items: 1. Healing Potion, 2. Shield of Protection, 3. Time Stopper, 4. Banana, 5. Bomb")
            item = input("Enter the item number: ")
            use_item(item, enemy)
        elif action == "4":
            run_away()
            break
        else:
            print("Invalid action. Try again.")

        if enemy_frozen_turns > 0:
            enemy_frozen_turns -= 1

        if enemy["health"] <= 0:
            print(f"You defeated the {enemy['name']}!")
            player_points += enemy["points"]
            print(f"You earned {enemy['points']} points!")
            game_won()
        elif player_health <= 0:
            game_over()
            break
#para de le o codigo dos otro fi...
def shop():
    global player_points, healing_potion_uses, time_stop_uses, shield_uses, banana_uses, bomb_uses
    print("\nWelcome to the shop!")
    print("Items: 1. Healing Potion (10 points), 2. Shield of Protection (20 points), 3. Time Stopper (30 points), 4. Banana (40 points), 5. Bomb (50 points)")
    item = input("Enter the item number you want to buy: ")
    if item == "1" and player_points >= 10:
        healing_potion_uses += 1
        player_points -= 10
        print("You bought a Healing Potion.")
    elif item == "2" and player_points >= 20:
        shield_uses += 1
        player_points -= 20
        print("You bought a Shield of Protection.")
    elif item == "3" and player_points >= 30:
        time_stop_uses += 1
        player_points -= 30
        print("You bought a Time Stopper.")
    elif item == "4" and player_points >= 40:
        banana_uses += 1
        player_points -= 40
        print("You bought a Banana.")
    elif item == "5" and player_points >= 50:
        bomb_uses += 1
        player_points -= 50
        print("You bought a Bomb.")
    else:
        print("You don't have enough points or entered an invalid item number.")

while True:
    chosen_enemy = random.choice(enemies)
    chosen_enemy["health"] += 10
    battle(chosen_enemy)
    shop()