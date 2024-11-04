# Tor-Jones---NPC-Generator

## This generator takes the input of the user for the name and randomly generates everything else.
# Name:

```
NPC1 = input("Enter a NPC name: ") 
score = [] 
score.append(NPC1) 
```
## In the name section it takes the input of the user for the name. It also holds the score list which will contain all of the other atributes of the characters. At the end of the list it appends the name into the list.

# Age:

```
  NPC1AGE = random.randint(1, 85)
    score.append(NPC1AGE)
```
## In the age section it randomly chooses a number in between 1 and 85. This will represent the age for the character, then it is appended into our list from before.

# Characteristics:

```
NPC1CHARLIST = ["Hero", "Villain"] 
    NPC1CHAR = random.choice(NPC1CHARLIST)
    score.append(NPC1CHAR)
```
## In the Characteristics section it creates it own list that will contains the Hero atribute and the Villain atribute. It then uses random.choice to select either one which then appends it to the main list.

# Strength:

```
NPC1STRENGTH = random.randint(1, 1000000)
    PowerLevel = "Power Level: ", NPC1STRENGTH
    score.append(PowerLevel)
```
## In the Strength section it chooses a random number between 1 and 1000000. It then creates a new varible that lists it as Power Level and puts the total power. Then it is appended into the main list.

# Health:

```
NPC1HEALTH = random.randint(1, 10000)
    Health = "Health: ", NPC1HEALTH
    score.append(Health)
```
## In the Health section it chooses a random number between 1 and 10000. It then also creates a new variable that lists it as health and puts the total health. Then it is also appended into the main list.

# Print and Looping:

```
print(score)

for choice in range(10):
```
## In the last section it prints the score (The main list). It then loops it 10 times for the other ten NPC's.
