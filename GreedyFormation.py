import sys
import pandas as pd # to read csv file about club players

class Player:
    # FOOTBALL PLAYER
    def __init__(self, name, position, rating, condition):
        self.name = name
        self.rating = rating
        self.condition = condition
        self.position = position

    def getPoint(self):
        if (self.condition == 1):
            return self.rating*50/100
        elif (self.condition == 2):
            return self.rating*75/100
        elif (self.condition == 3):
            return self.rating
        elif (self.condition == 4):
            return self.rating*125/100
        elif (self.condition == 5):
            return self.rating*150/100

class Formation:
    # FORMATION OF FOOTBALL: DEFENDER MIDFIELDER FORWARD
    def __init__(self, df = 0, mf = 0, fw = 0):
        self.forward = fw
        self.midfielder = mf
        self.defender = df
        self.score = 0
    
    def addScore(self, score):
        self.score += score

class Squad:
    #SQUAD OF FOOTBALL CLUB
    def __init__(self):
        self.goalkeeper = []
        self.forward = []
        self.midfielder = []
        self.defender = []

    def inputGoalKeeper(self, player):
        if (len(self.goalkeeper) == 0):
            self.goalkeeper.append(player)
        else:
            found = False
            for i in range(0,len(self.goalkeeper)):
                if (player.getPoint() > self.goalkeeper[i].getPoint()):
                    found = True
                    self.goalkeeper.insert(i, player)
                    break
                elif (player.getPoint() == self.goalkeeper[i].getPoint()):
                    if (player.rating >= self.goalkeeper[i].rating):
                        found = True
                        self.goalkeeper.insert(i, player)
                        break
            if (not found):
                self.goalkeeper.append(player)

    def inputForward(self, player):
        if (len(self.forward) == 0):
            self.forward.append(player)
        else:
            found = False
            for i in range(0,len(self.forward)):
                if (player.getPoint() > self.forward[i].getPoint()):
                    found = True
                    self.forward.insert(i, player)
                    break
                elif (player.getPoint() == self.forward[i].getPoint()):
                    if (player.rating >= self.forward[i].rating):
                        found = True
                        self.forward.insert(i, player)
                        break

            if (not found):
                self.forward.append(player)

    def inputMidfielder(self, player):
        if (len(self.midfielder) == 0):
            self.midfielder.append(player)
        else:
            found = False
            for i in range(0,len(self.midfielder)):
                if (player.getPoint() > self.midfielder[i].getPoint()):
                    found = True
                    self.midfielder.insert(i, player)
                    break
                elif (player.getPoint() == self.midfielder[i].getPoint()):
                    if (player.rating >= self.midfielder[i].rating):
                        found = True
                        self.midfielder.insert(i, player)
                        break

            if (not found):
                self.midfielder.append(player)
    
    def inputDefender(self, player):
        if (len(self.defender) == 0):
            self.defender.append(player)
        else:
            found = False
            for i in range(0,len(self.defender)):
                if (player.getPoint() > self.defender[i].getPoint()):
                    found = True
                    self.defender.insert(i, player)
                    break;
                elif (player.getPoint() == self.defender[i].getPoint()):
                    if (player.rating >= self.defender[i].rating):
                        found = True
                        self.defender.insert(i, player)
                        break
            if (not found):
                self.defender.append(player)

#Input Data for All Possible Formation
list_formation = []
with open('formation.txt') as formation:
    for form in formation:
        line = form.split(" ")
        list_formation.append(Formation(int(line[0]), int(line[1]), int(line[2])))
print('FORMATION ALL LOADED')

#Input Data for Squad
squad = Squad()
if (len(sys.argv) == 2):
    squadname = sys.argv[1]
else: 
    squadname = "ManchesterUnited.csv"

man = pd.read_csv(squadname)
i = 0
while (i < len(man.Nama)):
    p = Player(man.Nama[i], man.Posisi[i], man.Rating[i], man.Kondisi[i])
    if (p.position == 'DF'):
        squad.inputDefender(p)
    elif (p.position == 'MF'):
        squad.inputMidfielder(p)
    elif (p.position == 'FW'):
        squad.inputForward(p)
    elif (p.position == 'GK'):
        squad.inputGoalKeeper(p)
    i += 1
print('SQUAD LOADED')

#Using Greedy Algorithm to find the best Formation
best_formation = Formation()
for formation in list_formation:
    #Check if squad is valid for the formation
    if (formation.forward <= len(squad.forward) and formation.midfielder <= len(squad.midfielder) and formation.defender <= len(squad.defender)):
        # Add Score
        for player in squad.forward:
            i = 0
            if (i <= formation.forward):
                formation.addScore(player.getPoint())
                i += 1
        for player in squad.midfielder:
            i = 0
            if (i <= formation.midfielder):
                formation.addScore(player.getPoint())
                i += 1  
        for player in squad.defender:
            i = 0
            if (i <= formation.defender):
                formation.addScore(player.getPoint())
                i += 1
        formation.addScore(squad.goalkeeper[0].getPoint())

        if (formation.score > best_formation.score):
            best_formation = formation
    else:
        continue

#Show the best formation
if (best_formation.defender == 0 and best_formation.midfielder == 0 and best_formation.forward == 0):
    print('No Best Formation Found')
else:
    print('Best Formation : ')
    print(best_formation.defender, best_formation.midfielder, best_formation.forward)

    print('Forward : ')
    i = 1
    for fw in squad.forward:
        if (i <= best_formation.forward):
            print(fw.name)
            i+=1

    print()
    print('Midfielder : ')
    i = 1
    for mf in squad.midfielder:
        if (i <= best_formation.midfielder):
            print(mf.name)
            i+=1

    print()
    print('Defender : ')
    i = 1
    for df in squad.defender:
        if (i <= best_formation.defender):
            print(df.name)
            i+=1

    print()
    print('GoalKeeper :')
    print(squad.goalkeeper[0].name)

