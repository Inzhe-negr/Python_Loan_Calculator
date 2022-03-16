x, y = int(input()), int(input())
moves = 0
if x < 8:
    moves += 1
    if y < 8:
        moves += 1
    if y > 1: 
        moves += 1
if x > 1:
    moves += 1
    if y < 8:
        moves += 1
    if y > 1: 
        moves += 1
if y < 8:
    moves += 1
if y > 1: 
    moves += 1
print(moves)
