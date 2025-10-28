import time as T
import random as R

# Setup
print("Welcome to training! First I need to know some things about you!")
type = float(input("What class are you?\n1. Rogue\n2. Wizard\n3. Lizard\n!*&#$. Nerd\n"))
name = input("What is your name?")
scenario = R.randint(1, 3)
turn = R.randint(1, 2)

# Player stats
if type == 1:
    player_health = 25
    player_attack = 15
    player_defense = 15
    player_damage = 5
elif type == 2:
    player_health = 40
    player_attack = 20
    player_defense = 5
    player_damage = 10
elif type == 3:
    player_health = 1
    player_attack = 15
    player_defense = 100
    player_damage = 1
elif type == 3.14159:
    player_health = 3.14
    player_attack = 9999
    player_defense = 9999
    player_damage = 9999
else:
    player_health = 10
    player_attack = 5
    player_defense = 5
    player_damage = 2

# Enemy stats
if scenario == 1:
    print("You are walking through a dark forest when suddenly a wild Chris Pratt appears!")
    T.sleep(2)
    print("Prepare for battle!")
    T.sleep(1)
    enemy_health = 30
    enemy_attack = 10
    enemy_defense = 5
    enemy_damage = 8
elif scenario == 2:
    print("You are in a dark dungeon when a wild Jack Black appears!")
    T.sleep(2)
    print("Prepare for battle!")
    T.sleep(1)
    enemy_health = 35
    enemy_attack = 8
    enemy_defense = 10
    enemy_damage = 7
elif scenario == 3:
    print("You are walking in China Town and suddenly a wild Jackie Chan appears!")
    T.sleep(2)
    print("Prepare for battle!")
    T.sleep(1)
    enemy_health = 28
    enemy_attack = 12
    enemy_defense = 8
    enemy_damage = 9
else:
    enemy_health = 1
    enemy_attack = 1
    enemy_defense = 1
    enemy_damage = 1

# Turn functions
def player_turn():
    print("Your turn!")
    action = input("Choose:\n1. Attack\n2. Defend\n3. Heal\n4. Flee\n")
    return action

def enemy_turn():
    return R.choice(["attack", "defend"])

# Game loop
while player_health > 0 and enemy_health > 0:
    if turn == 1:
        action = player_turn()
        if action == "1":
            dmg = max(player_damage - enemy_defense // 2, 1)
            enemy_health -= dmg
            print(f"You deal {dmg} damage! Enemy health is now {enemy_health}.")
        elif action == "2":
            player_defense += 5
            print("You defend. Defense increased.")
        elif action == "3":
            player_health += 10
            print(f"You heal. Health is now {player_health}.")
        elif action == "4":
            if R.random() < 0.5:
                print("You fled successfully!")
                break
            else:
                print("You failed to flee!")
        else:
            print("Invalid action.")
        turn = 2
    else:
        print("Enemy's turn!")
        action = enemy_turn()
        if action == "attack":
            dmg = max(enemy_damage - player_defense // 2, 1)
            player_health -= dmg
            print(f"Enemy deals {dmg} damage! Your health is now {player_health}.")
        else:
            enemy_defense += 5
            print("Enemy defends. Defense increased.")
        turn = 1

# Outcome
if player_health <= 0:
    print("You were defeated.")
elif enemy_health <= 0:
    print(f"{name} wins!")