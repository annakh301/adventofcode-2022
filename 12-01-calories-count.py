import read_function

calories = read_function.read_file("input-puzzle/calories.txt")

counter = 0 
elfStash = 0
elfSum = []

for foodPiece in calories:
    if len(foodPiece)==0:
        elfSum.append(elfStash)
        elfStash = 0
    else: elfStash = elfStash + int(foodPiece)

print(elfSum)
print(max(elfSum))
print(min(elfSum))

elfSum.sort()
print(elfSum)

top3 = elfSum[-3:]

print(top3)
print(sum(top3))

