# BB 1st Combate Project
import time as T
import random as R

print("Welcome to training! First I need to know some things about you!")
type = input("What class are you?\n1. Rogue\n2. Wizard\n3. Lizard\n!*&#$. Nerd\n")
na = input("What is your useless name?")
scenareo = R.randint(1,3)
turn = R.randint(1,2)

if type == 1: 
    health = 25
    attack = 15
    defence = 15
    damage = 5
elif type == 2: 
    health = 40
    attack = 20
    defense = 5
    damage = 10
elif type == 3:
    health = 1
    attack = 15
    defence = 100
    damage = 1
elif type == 3.14159: 
    health = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989380952572010654858632788659361533
    attack = 9999
    defence = 9999
    damage = 9999

if scenareo == 1:
    print("You are walking through a dark forest when suddenly a wild Chris Pratt appears!")
    T.sleep(2)
    print("Prepare for battle!")
    T.sleep(1)
    chris_pratt_health = 30
    chris_pratt_attack = 10
    chris_pratt_defence = 5
    chris_pratt_damage = 8
elif scenareo == 2:
    print("You are in a dark dungeon when a wild Jack Black appears!")
    T.sleep(2)
    print("Prepare for battle!")
    T.sleep(1)
    jack_black_health = 35
    jack_black_attack = 8
    jack_black_defence = 10
    jack_black_damage = 7
elif scenareo == 3:
    print("You ar walking in China Town and suddenly a wild Jackie Chan appears!")
    T.sleep(2)
    print("Prepare for battle!")
    T.sleep(1)
    jackie_chan_health = 28
    jackie_chan_attack = 12
    jackie_chan_defence = 8
    jackie_chan_damage = 9
else: 
    print("Error: Invalid scenario.")
    pass

def player_turn(action):
    health
    attack
    defence
    damage
    print("Your turn!")
    action = input("What do you want to do?\n1. Attack\n2. Defend\n")
    if action == 1:
        print("You attack the enemy!")
    elif action == 2:
        print("You defend against the next attack!")
        # Update player defence here
    else:
        print("Invalid action. You lose your turn.") 
    return action