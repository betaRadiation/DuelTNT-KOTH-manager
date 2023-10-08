import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

# Read token
tokenFile = open("token.txt", "r")
token = tokenFile.read()
tokenFile.close()

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

existingGame = False
playerList = []
currentMatch = 0

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1154608524450603068))
    print(f"We have logged in as {client.user}")

class dtntKOTH(discord.ui.View):
    
    def __init__(self):
        super().__init__()
        self.value = None

    def embed(self):
        if (existingGame == True):
            embed=discord.Embed(title="Game, Player 1:" + playerList[currentMatch] + " vs. Player 2" + playerList[currentMatch+1], color=0x986a44)
            embed.add_field(name="Hint: User /koth winner ``(Player #)``")
        else:
            embed=discord.Embed(title="create game with /koth create ``Player1 Player2 Player3``")


@tree.command(name = "koth", description = "Shows dtnt KOTH", guild=discord.Object(id=1154608524450603068)) 
async def koth(interaction):
    await interaction.response.send_message(embed=view.embed())

group = app_commands.Group(name="koth", description="koth")

@group.command(name = "winner", description = "Selects a winner for the current match")
@app_commands.describe(selectWinner="Enter the player number")
async def winner(interaction, selectWinner: int):
    if (playerWinner < 1 or playerWinner > 2):
        await interaction.response.send_message("enter a valid player number")
    if (playerWinner == 1):
        await interaction.response.send_message(title=playerList[currentMatch] + " won")
        currentMatch = currentMatch + 1
        if(currentMatch + 1 >= len(playerList)):
            playerList.append(playerList.pop(0))
            playerList.insert(0, playerList.pop(currentMatch-1))
            currentMatch = 0
    else:
        await interaction.response.send_message(title=playerList[currentMatch+1] + " won")
    await interaction.response.send_message(embed=view.embed())
    currentMatch = currentMatch + 1
    if(currentMatch + 1 >= len(playerList)):
        playerList.append(playerList.pop(0))
        playerList.insert(0, playerList.pop(currentMatch-1))
        currentMatch = 0

@group.command(name = "addplayer", description = "Enter a player name and add them to the queue")
@app_commands.describe(newPlayer="Enter the player name you want to add")
async def addPlayer(interaction, newPlayer: str):
    playerList.append(addPlayer)

@group.command(name = "create", description = "Create a KOTH game")
@app_commands.describe(startingPlayers="Enter the player names you want to add (seperated with space)")
async def startGame(interaction, startingPlayers: str):
    if (existingGame == False):
        playerList = startingPlayers.split(" ")

@group.command(name = "end", description = "Ends a KOTH game")
async def ends(interaction):
    existingGame = False
    playerList = []
    currentMatch = 0
    await interaction.response.send_message("Goodbye")

client.run(token)





# while(True):
#     print("input a player name, type \"EXIT\" to exit:" , end=" ")
#     Player = input()

#     if (Player != "EXIT"):
#         playerList.append(Player)
#     else:
#         break

# print(" ")

# def listPlayers():
#     for i in range(len(playerList)):
#         print(str(i+1) + ") " + playerList[i])


# while(True):
#     print("Game " + playerList[currentMatch] + " vs. " + playerList[currentMatch+1] + "\n")
#     print("input a command: \n")

#     print("1) " + playerList[currentMatch] + " won round")
#     print("2) " + playerList[currentMatch+1] + " won round")
#     print("3) Add player")
#     print("4) Remove player")
#     print("5) List players")
#     print("6) Exit \n")

#     print(": " , end=" ")
#     Command = input()

#     if (Command == "1"):
#         print(playerList[currentMatch+1] + " has lost the round")
#         playerList.insert(0, playerList.pop(currentMatch+1))
#         currentMatch = currentMatch + 1
#         if(currentMatch + 1 >= len(playerList)):
#             playerList.append(playerList.pop(0))
#             playerList.insert(0, playerList.pop(currentMatch-1))
#             currentMatch = 0
#     elif (Command == "2"):
#         print(playerList[currentMatch] + " has lost the round")
#         playerList.insert(0, playerList.pop(currentMatch))
#         currentMatch = currentMatch + 1
#         if(currentMatch + 1 >= len(playerList)):
#             playerList.append(playerList.pop(0))
#             playerList.insert(0, playerList.pop(currentMatch-1))
#             currentMatch = 0
#     elif (Command == "3"):
#         print("input extra player name, type \"EXIT\" to exit:" , end=" ")
#         Player = input()
#         if (Player != "EXIT"):
#             playerList.append(Player)
#     elif (Command == "4"):
#         listPlayers()
#         print("Type select player to remove: ", end=" ")
#         PlayerNum = input()
#         try:
#             PlayerNum = int(PlayerNum)
#         except:
#             print("Enter valid player option")
#             pass
#         if(PlayerNum-1 > len(playerList) or PlayerNum-1 < 0):
#             print("Enter valid player option")
#             pass
#         playerList.pop(PlayerNum-1)
#     elif (Command == "5"):
#         listPlayers()
#     elif (Command == "6"):
#         exit()
#     else:
#         print("Enter valid option")

#     if (Player != "EXIT"):
#         playerList.append(Player)
#     else:
#         break

# print(" ")

# def listPlayers():
#     for i in range(len(playerList)):
#         print(str(i+1) + ") " + playerList[i])


# while(True):
#     print("Game " + playerList[currentMatch] + " vs. " + playerList[currentMatch+1] + "\n")
#     print("input a command: \n")

#     print("1) " + playerList[currentMatch] + " won round")
#     print("2) " + playerList[currentMatch+1] + " won round")
#     print("3) Add player")
#     print("4) Remove player")
#     print("5) List players")
#     print("6) Exit \n")

#     print(": " , end=" ")
#     Command = input()

#     if (Command == "1"):
#         print(playerList[currentMatch+1] + " has lost the round")
#         playerList.insert(0, playerList.pop(currentMatch+1))
#         currentMatch = currentMatch + 1
#         if(currentMatch + 1 >= len(playerList)):
#             playerList.append(playerList.pop(0))
#             playerList.insert(0, playerList.pop(currentMatch-1))
#             currentMatch = 0
#     elif (Command == "2"):
#         print(playerList[currentMatch] + " has lost the round")
#         playerList.insert(0, playerList.pop(currentMatch))
#         currentMatch = currentMatch + 1
#         if(currentMatch + 1 >= len(playerList)):
#             playerList.append(playerList.pop(0))
#             playerList.insert(0, playerList.pop(currentMatch-1))
#             currentMatch = 0
#     elif (Command == "3"):
#         print("input extra player name, type \"EXIT\" to exit:" , end=" ")
#         Player = input()
#         if (Player != "EXIT"):
#             playerList.append(Player)
#     elif (Command == "4"):
#         listPlayers()
#         print("Type select player to remove: ", end=" ")
#         PlayerNum = input()
#         try:
#             PlayerNum = int(PlayerNum)
#         except:
#             print("Enter valid player option")
#             pass
#         if(PlayerNum-1 > len(playerList) or PlayerNum-1 < 0):
#             print("Enter valid player option")
#             pass
#         playerList.pop(PlayerNum-1)
#     elif (Command == "5"):
#         listPlayers()
#     elif (Command == "6"):
#         exit()
#     else:
#         print("Enter valid option")