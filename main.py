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
playerList = [ ]

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

class kothUI(discord.ui.View):
    global playerList

    def __init__(self):
        super().__init__()


    async def embed(self):
        global playerList
        if (len(playerList) > 1):
            embed=discord.Embed(title="Current Match", color=0x986a44)
            embed.add_field(name="", value=f"Player 1 {await client.fetch_user(playerList[0])} vs. Player 2 {await client.fetch_user(playerList[1])}", inline=False)
            embed.add_field(name="", value="Select a winner", inline=False)
        else:
            embed=discord.Embed(title="Add more players", color=0x986a44)
        return embed

    def logic(winner):
        global playerList
        if (winner == 0):
            playerList.append(playerList.pop(1))
        else:
            playerList.append(playerList.pop(0))

                
            
        
    @discord.ui.button(label="Player 1 wins", style=discord.ButtonStyle.danger)
    async def player1(self, interaction, button: discord.ui.button):
        kothUI.logic(0)
        await interaction.response.edit_message(embed = await self.embed())
    @discord.ui.button(label="Player 2 wins", style=discord.ButtonStyle.secondary)
    async def optionB(self, interaction, button: discord.ui.button):
        kothUI.logic(1)
        await interaction.response.edit_message(embed = await self.embed())


# Shows the current game if there is one
# @tree.command(name = "koth", description = "Shows dtnt KOTH", guild=discord.Object(id=1154608524450603068)) 
@tree.command(name = "show", description = "Shows the current match")
async def show(interaction):
    view = kothUI()
    await interaction.response.send_message(embed=await view.embed(), view=view)



# Adds a right click menu to add a user to game
@tree.context_menu(name='Add to game')
async def addToGame(interaction: discord.Interaction, member: discord.Member):
    if (member.id not in playerList):
        playerList.append(member.id)
        await interaction.response.send_message(f"Added {member.mention} to game")
    else:
        await interaction.response.send_message(f"{member.mention} is already in the game")


@tree.context_menu(name='Remove from game')
async def removeFromGame(interaction: discord.Interaction, member: discord.Member):
    if (member.id in playerList):
        playerList.pop(playerList.index(member.id))
        await interaction.response.send_message(f"Removed {member.mention} from game")
    else:
        await interaction.response.send_message(f"{member.mention} is not in the game")

@tree.command(name = "leave", description = "Leave the game")
async def leave(interaction: discord.Interaction):
    if (interaction.user.id in playerList):
        playerList.pop(playerList.index(interaction.user.id))
        await interaction.response.send_message("Removed you from game")
    else:
        await interaction.response.send_message("You are not in the game")

@tree.command(name = "join", description = "Join the game")
async def join(interaction: discord.Interaction):
    if (interaction.user.id not in playerList):
        playerList.append(interaction.user.id)
        await interaction.response.send_message("Added you to game")
    else:
        await interaction.response.send_message("You are already in the game")

@tree.command(name = "clear", description = "Clears the player list")
async def clear(interaction):
    global playerList
    playerList = []
    await interaction.response.send_message("Cleared player list!")

client.run(token)