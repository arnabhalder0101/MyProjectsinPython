winner = 0
player1 = []
player2 = []

baseList = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
winning_list = []

for a in range(2):
    l0 = []
    for b in range(3):
        if a == 0:
            x = y = b
            l0.append(str(x) + str(y))
        else:
            x = b
            y = 2 - b
            l0.append(str(x) + str(y))
    winning_list.append(l0)

for i in range(3):
    l1 = []
    l2 = []
    for j in range(3):
        l1.append(str(i) + str(j))
        l2.append(str(j) + str(i))

    winning_list.append(l1)
    winning_list.append(l2)

print(winning_list)


def AskInputs(n):
    print(f"Player {n}")
    inp = input("Enter (\"X\" OR \"O\") With Position you want to acquire:").split()
    return inp


def gamePlot(value=None, positionX=None, positionY=None):
    # baseList = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    if positionX is None and positionY is None:
        for i1 in range(len(baseList)):
            for i2 in range(len(baseList[i])):
                print(f"|  {baseList[0][0]}  |", end="")
            print("\n")
    else:
        for run in range(len(baseList)):
            for runIn in range(len(baseList[i])):
                print(f"|  {baseList[run][runIn]}  |", end="")
            print("\n")


def pointValidation(listPlayer):
    global winner
    if listPlayer in winning_list:
        print("Winner found!")
        winner = 1


gamePlot()
maxRun = 0

while maxRun < 9:
    # pointing to player 1 or 2 --
    playerNum = (maxRun % 2 + 1)
    userInp = AskInputs(playerNum)  # returns a list --> ["X", "00"]

    # updating the main base list --
    if baseList[int(userInp[1][0])][int(userInp[1][1])] == "-":
        baseList[int(userInp[1][0])][int(userInp[1][1])] = userInp[0]
    else:
        print("Sorry, this position is already taken!\nGo With another Position -->\n")
        continue

    # calling gamePlot to show the output to the player --
    userCall = userInp[0]
    possX = int(userInp[1][0])
    possY = int(userInp[1][1])
    gamePlot(userCall, possX, possY)

    # game validation goes here--
    if playerNum == 1:
        player1.append(userInp[1])
    else:
        player2.append(userInp[1])

    if len(player1) >= 3 or len(player2) >= 3:
        # last 3 choices --
        if len(player1) >= 3:
            player1LastThree = player1[-3:]
            print(player1LastThree)
            pointValidation(player1LastThree)
            # if winner fount just break the loop, then & there --
            if winner == 1:
                print(f"Player {playerNum} is the winner!")
                break

        if len(player2) >= 3:
            player2LastThree = player2[-3:]
            print(player2LastThree)
            pointValidation(player2LastThree)
            # if winner fount just break the loop, then & there --
            if winner == 1:
                print(f"Player {playerNum} is the winner!")
                break

    maxRun += 1
