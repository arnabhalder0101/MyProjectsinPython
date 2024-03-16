winner = 0
player1 = []
player2 = []
playerNames = []

baseList = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
winning_list = []
win_dic = {}

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

for base in range(len(baseList)):
    for baseInside in range(len(baseList[base])):
        win_dic[baseList[base][baseInside]] = str(base) + str(baseInside)

print(win_dic)


def AskInputs(namePlayer):
    print(f"# {namePlayer} it's your turn -->")
    inp = input("Enter (\"X\" OR \"O\") With Position you want to acquire:").split()
    return inp


def askNames():
    for run1 in range(2):
        playerNames.append(input(f"Enter name for Player{run1 + 1}: "))


def gamePlot(value=None, positionX=None, positionY=None):
    # baseList = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    if positionX is None and positionY is None:
        for i1 in range(len(baseList)):
            for i2 in range(len(baseList[i])):
                print(f"|  {baseList[i1][i2]}  |", end="")
            print("\n")
    else:
        for run in range(len(baseList)):
            for runIn in range(len(baseList[i])):
                print(f"|  {baseList[run][runIn]}  |", end="")
            print("\n")


def pointValidation(listPlayer):
    global winner

    # if listPlayer in winning_list:
    #     print("Winner found!")
    #     winner = 1

    # if the player moves are according to the winning list then add +1
    # take each item of playerList and do check if that is present in any of the winning list -- by iteration!
    # +1 for presence

    for i1 in range(len(winning_list)):
        sumDeclaration = 0
        check = winning_list[i1]
        for i2 in range(len(listPlayer)):
            for i3 in range(len(check)):
                if listPlayer[i2] == check[i3]:
                    sumDeclaration += 1

        # if sum == 3 then declare the winner!
        if sumDeclaration == 3:
            print("Winner found!")
            winner = 1
            break


# basic gameplot to show at the very beginning --
gamePlot()
# ask name for respective players--
askNames()
maxRun = 0

while maxRun < 9:
    # pointing to player 1 or 2 --
    playerNum = (maxRun % 2)
    name = playerNames[playerNum]
    userInp = AskInputs(name)  # returns a list --> ["X", "1"]

    userCall = userInp[0]
    possX = int(win_dic[userInp[1]][0])
    possY = int(win_dic[userInp[1]][1])

    # updating the main base list --
    if baseList[possX][possY] not in ["X", "x", "O", "o", "0"]:
        baseList[possX][possY] = userInp[0]
    else:
        print("Sorry, this position is already taken!\nGo With another Position -->\n")
        continue

    # calling gamePlot to show the output to the player --
    gamePlot(userCall, possX, possY)

    # game validation goes here--
    if playerNum == 1:
        player1.append(win_dic[userInp[1]])
    else:
        player2.append(win_dic[userInp[1]])

    if len(player1) >= 3 or len(player2) >= 3:
        # choices -- for player 1
        if len(player1) >= 3:
            # player1LastThree = player1[-3:]
            # print(player1LastThree)
            pointValidation(player1)
            # if winner fount just break the loop, then & there --
            if winner == 1:
                print(f"{name} congratulations! \nYou got this... Well done!")
                break

        # for player 2 --
        if len(player2) >= 3:
            # player2LastThree = player2[-3:]
            # print(player2LastThree)
            pointValidation(player2)
            # if winner found just break the loop, then & there --
            if winner == 1:
                print(f"{name} congratulations! You got this... Well done!")
                break

    maxRun += 1
