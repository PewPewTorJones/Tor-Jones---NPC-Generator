import random
#Making the Name
NPC1 = input("Enter a NPC name: ")
score = []
score.append(NPC1) 
#Making the Age
NPC1AGE = random.randint(1, 85)
score.append(NPC1AGE)
#Making the Characteristics
NPC1CHARLIST = ["Hero" or "Villian"] 
NPC1CHAR = random.choice(NPC1CHARLIST)
score.append(NPC1CHAR)

#Making the Strength 
NPC1STRENGTH = random.randint(1, 1000000)
PowerLevel = "Power Level: ", NPC1STRENGTH
score.append(PowerLevel)
#Making the Health
NPC1HEALTH = random.randint(1, 10000)
Health = "Health: ", NPC1HEALTH
score.append(Health)
#looping it 10 times
print(score)

for choice in range(10):
    NPC1 = input("Enter a NPC name: ")
    score = []
    score.append(NPC1) #inserts the user input into the lis
    NPC1AGE = random.randint(1, 85) #generating the age
    score.append(NPC1AGE)

    NPC1CHARLIST = ["Hero", "Vilian"] 
    NPC1CHAR = random.choice(NPC1CHARLIST)
    score.append(NPC1CHAR)

 
    NPC1STRENGTH = random.randint(1, 1000000)
    PowerLevel = "Power Level: ", NPC1STRENGTH
    score.append(PowerLevel)

    NPC1HEALTH = random.randint(1, 10000)
    Health = "Health: ", NPC1HEALTH
    score.append(Health)

    print(score)
    
