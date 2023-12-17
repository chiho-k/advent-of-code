file = open("games.txt", "r")

newfile = []

def gamesplitter(text):
    rounds = []
    n = text.count(";")
    start = 0
    newtext = text
    for i in range(0, n+1):
        index = newtext.find(";")
        if index == -1:
            round = newtext[start:]
        else:
            round = newtext[start:index]
        newtext = newtext[index+2:]
        rounds.append(round)
    return rounds

for line in file:
    newfile.append(gamesplitter(line))

def colourtester(list, colour, limit):
    gamepossible = []
    for line in list:
        possible = True
        for round in line:
            index = round.find(colour)
            if index != -1:
                if index-3 >= 0:
                    number = round[index-3:index]
                else:
                    number = round[index-2:index]
            else:
                number = 0

            if int(number) > limit:
                possible = False
        gamepossible.append(possible)
    return gamepossible

blue = colourtester(newfile, "blue", 14)
green = colourtester(newfile, "green", 13)
red = colourtester(newfile, "red", 12)

possibleGames = []
for i in range(0, 100):
    if blue[i] and green[i] and red[i]:
        possibleGames.append(i+1)

IDsum = 0
for i in possibleGames:
    IDsum += i

print("Sum of possible game IDs: ", IDsum)
