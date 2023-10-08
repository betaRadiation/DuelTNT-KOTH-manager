from readchar import readkey,key
import os

players = []
n = 0
rounds = []
players_dict = {}

while True:
    p = input("Input a player name press. ENTER when done: ")
    if p != "":
        players.append(p)
    else:
        os.system("clear")
        break

c = 0
first = False

for p in players:
    players_dict[p] = 0

while True:
    print(f'Round {c+1}: {players[n]} vs. {players[n+1]}')
    print("1) " + players[n] + " won round")
    print("2) " + players[n+1] + " won round")
    print("3) Undo last match")
    print("4) Add player")
    print("5) Remove player")
    print("6) List players")
    print("7) List round history")
    print("8) List player wins")
    print("9) Exit")
    print("> ", end="")
    inpt = readkey()
    print()
    os.system("clear")
    if inpt == "1":
        rounds.append((f"{players[n]} won against {players[n+1]}"))
        print(rounds[len(rounds)-1])
        p = players.pop(n+1)
        players_dict[players[0]] += 1
        players.append(p)
        c += 1
        
    elif inpt == "2":
        rounds.append((f"{players[n+1]} won against {players[n]}"))
        print(rounds[len(rounds)-1])
        p = players.pop(n)
        players_dict[players[0]] += 1
        players.append(p)
        c += 1
    elif inpt == "3":
        if c > 0:
            rounds.pop(len(rounds)-1)
            p = players.pop(len(players)-1)
            players.insert(1,p)
            players_dict[players[0]] -= 1
            c -= 1
    elif inpt == "4":
        p = input("Input a player name. Press ENTER when done: ")
        if p != "":
            players.append(p)
        else:
            break
    elif inpt == "5":
        while True:
            for i in range(len(players)):
                print(f"{i+1}) {players[i]}")
            print("Type a number to remove a player. Press ENTER to exit")
            k = readkey()
            if k == key.ENTER:
                os.system("clear")
                break
            try: 
                players.pop(int(k)-1)
            except (ValueError, IndexError): pass
            os.system("clear")
    elif inpt == "6":
        for i in range(len(players)):
                print(f"{i+1}) {players[i]}")
        print("Press any key to continue.")
        readkey()
        os.system("clear")
    elif inpt == "7":
        for i in range(len(rounds)):
            print(f"Round {i+1}: {rounds[i]}")
        print("Press any key to continue.")
        readkey()
        os.system("clear")
    elif inpt == "8":
        for k,v in sorted(players_dict.items(), key=lambda x:x[1],reverse=True):
            print(f"{k}: {v} wins")
        print("Press any key to continue.")
        readkey()
        os.system("clear")
    elif inpt == "9":
        break
