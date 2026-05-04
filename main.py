import random

clothing_db = []
with open("clothing_input.txt", encoding="utf-8") as file:
    for clothing in file:
        clothing_db.append(clothing.strip())

# User chooses which event they're going to, but this isn't actually taken into consideration yet
user_event = input("Which event are you going to? ")
print(f"\nChosen event: {user_event}\n")

# Choose an outfit at random
outfit = []
outfit = random.sample(clothing_db, 3)
print(f"Chosen outfit: {outfit}")
