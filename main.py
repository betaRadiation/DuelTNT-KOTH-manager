playerList = []
currentMatch = 0

while(True):
    print("input a player name, type \"EXIT\" to exit:" , end=" ")
    Player = input()

    if (Player != "EXIT"):
        playerList.append(Player)
    else:
        break

print(" ")

def listPlayers():
    for i in range(len(playerList)):
        print(str(i+1) + ") " + playerList[i])


while(True):
    print("Game " + playerList[currentMatch] + " vs. " + playerList[currentMatch+1] + "\n")
    print("input a command: \n")

    print("1) " + playerList[currentMatch] + " won round")
    print("2) " + playerList[currentMatch+1] + " won round")
    print("3) Add player")
    print("4) Remove player")
    print("5) List players")
    print("6) Exit \n")

    print(": " , end=" ")
    Command = input()

    if (Command == "1"):
        print(playerList[currentMatch+1] + " has lost the round")
        playerList.insert(0, playerList.pop(currentMatch+1))
        currentMatch = currentMatch + 1
        if(currentMatch + 1 >= len(playerList)):
            playerList.append(playerList.pop(0))
            playerList.insert(0, playerList.pop(currentMatch-1))
            currentMatch = 0
    elif (Command == "2"):
        print(playerList[currentMatch] + " has lost the round")
        playerList.insert(0, playerList.pop(currentMatch))
        currentMatch = currentMatch + 1
        if(currentMatch + 1 >= len(playerList)):
            playerList.append(playerList.pop(0))
            playerList.insert(0, playerList.pop(currentMatch-1))
            currentMatch = 0
    elif (Command == "3"):
        print("input extra player name, type \"EXIT\" to exit:" , end=" ")
        Player = input()
        if (Player != "EXIT"):
            playerList.append(Player)
    elif (Command == "4"):
        listPlayers()
        print("Type select player to remove: ", end=" ")
        PlayerNum = input()
        try:
            PlayerNum = int(PlayerNum)
        except:
            print("Enter valid player option")
            pass
        if(PlayerNum-1 > len(playerList) or PlayerNum-1 < 0):
            print("Enter valid player option")
            pass
        playerList.pop(PlayerNum-1)
    elif (Command == "5"):
        listPlayers()
    elif (Command == "6"):
        exit()
    else:
        print("Enter valid option")