import discord
from discord.ext import commands
from discord import app_commands

# Request Intents
intents = discord.Intents.default()
intents.guilds = True
intents.members = True

# Read token (create file "token.txt" and put your key in plain text for this to work)
tokenFile = open("token.txt", "r")
token = tokenFile.read()
tokenFile.close()

# Create client object
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Create game variables
playerList = []
inGame = []
currentMatch = 0
matchNum = 1

# Log onto discord 
@client.event
async def on_ready():
    await tree.sync()
    print(f"We have logged in as {client.user}")

group = app_commands.Group(name="koth", description="koth")

# Returns a username form ID
async def userFormId(id: int):
    member = await client.get_user(id)
    return member


# Shows the current game if there is one
# @tree.command(name = "koth", description = "Shows dtnt KOTH", guild=discord.Object(id=1154608524450603068)) 
@tree.command(name = "show", description = "Shows the current match")
async def koth(interaction):
    if (len(playerList) > 1):
        if (len(inGame < 2)):
            inGame = [playerList[0], playerList[1]]
        
        embed=discord.Embed(title="Match " + str(matchNum), color=0x986a44)
        embed.add_field(name="", value=await userFormId(inGame[0]) + " vs. " + await userFormId(inGame[1]))
        embed.add_field(name="", value="\nHint: User /koth winner ``user``")
    else:
        embed=discord.Embed(title="Add more players")
    
    await interaction.response.send_message(embed=embed)


@tree.command(name = "winner", description = "Selects a winner for the current match")
@app_commands.describe(member="Enter the winning member number")
async def winner(interaction, member: discord.Member):
    pass


# Adds a right click menu to add a user to game
@tree.context_menu(name='Add to game')
async def addToGame(interaction: discord.Interaction, member: discord.Member):
    # The format_dt function formats the date time into a human readable representation in the official client
    if (member.id not in playerList):
        playerList.append(member.id)
        await interaction.response.send_message(f"Added {member.mention} to game")
    else:
        await interaction.response.send_message(f"{member.mention} is already in the game")


@tree.context_menu(name='Remove from game')
async def removeFromGame(interaction: discord.Interaction, member: discord.Member):
    # The format_dt function formats the date time into a human readable representation in the official client
    if (member.id in playerList):
        playerList.pop(playerList.index(member.id))
        await interaction.response.send_message(f"Removed {member.mention} from game")
    elif (existingGame == False):
        await interaction.response.send_message(f"Please create a KOTH game")
    else:
        await interaction.response.send_message(f"{member.mention} is not in the game")


@group.command(name = "addplayer", description = "Enter a player name and add them to the queue")
@app_commands.describe(newPlayer="Enter the player name you want to add")
async def addPlayer(interaction, newPlayer: str):
    playerList.append(addPlayer)


@group.command(name = "create", description = "Create a KOTH game")
@app_commands.describe(startingPlayer1="Enter the first players name you want to add (seperated with space)")
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