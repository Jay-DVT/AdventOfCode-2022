with open('testB.txt') as l:
    ls = l.readlines()

class Choice:
    def __init__(self, ch:str):
        if ch == 'A':
            self.type = "Rock"
        if ch == 'B':
            self.type = "Paper"
        if ch == 'C':
            self.type = "Scissors"
        if ch == 'X': # Lose
            self.val = 0
            pass
        if ch == 'Y': # Draw
            self.val = 3
            pass  
        if ch == 'Z': # Win
            self.val = 6
            pass

#A = Rock, B = Paper, C = Scissors
#X = Rock, Y = Paper, Z = Scissors

score = 0
out = []
for readLine in ls:
    line = readLine.split()
    bot, player = Choice(line[0]), Choice(line[1])
    if line[1] == "X":
        if bot.type == "Rock":
            score += 3
        if bot.type == "Paper":
            score += 1
        if bot.type == "Scissors":
            score += 2
    if line[1] == "Y":
        if bot.type == "Rock":
            score += 1
        if bot.type == "Paper":
            score += 2
        if bot.type == "Scissors":
            score += 3
    if line[1] == "Z":
        if bot.type == "Rock":
            score += 2
        if bot.type == "Paper":
            score += 3
        if bot.type == "Scissors":
            score += 1


    score += player.val #win loss situation

print(score)

