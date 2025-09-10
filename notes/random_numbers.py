# BB 1st Random Numbers Notes
import random


name = input("What is the name of your character?\n").strip().title()


# Generate Stat Options
stat_one = random.randint(1,10) + random.randint(1,10)
stat_two = random.randint(1,10) + random.randint(1,10)
stat_three = random.randint(1,10) + random.randint(1,10)
stat_four = random.randint(1,10) + random.randint(1,10)
stat_five = random.randint(1,10) + random.randint(1,10)
stat_six = random.randint(1,10) + random.randint(1,10)
stat_seven = random.randint(1,10) + random.randint(1,10)


# Telling user stat choices
print(f"Your stat options are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}, {stat_seven}")

# Set Stats
strength = int(input("which stat do you want for strength: \n")) +2

print(f"This a number from 0-1 {random.random()}")
print(f"This a number from 1-20 {random.randint(1,20)}")