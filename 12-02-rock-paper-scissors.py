import read_function

games = read_function.read_file("input-puzzle/rock-paper-scissors-input.csv")

def rounds(combination):
    if combination == "A Y":
        return 6
    elif combination == "A X":
        return 3
    elif combination == "A Z":
        return 0
    elif combination == "B Y":
        return 3
    elif combination == "B X":
        return 0
    elif combination == "B Z":
        return 6
    elif combination == "C Y":
        return 0
    elif combination == "C X":
        return 6
    elif combination == "C Z":
        return 3

def rockpaperscissors(mychoice):
    if mychoice == "Y":
        return 2
    elif mychoice == "X":
        return 1
    elif mychoice == "Z":
        return 3


def rounds2(combination):
    if combination == "A Y":
        return 1
    elif combination == "A X":
        return 3
    elif combination == "A Z":
        return 2
    elif combination == "B Y":
        return 2
    elif combination == "B X":
        return 1
    elif combination == "B Z":
        return 3
    elif combination == "C Y":
        return 3
    elif combination == "C X":
        return 2
    elif combination == "C Z":
        return 1

def rockpaperscissors2(mychoice):
    if mychoice == "Y":
        return 3
    elif mychoice == "X":
        return 0
    elif mychoice == "Z":
        return 6



points = []

for game in games:
    pointforaround = rounds2(game)+rockpaperscissors2(game[-1:])
    points.append(pointforaround)

print(points)
print(sum(points))