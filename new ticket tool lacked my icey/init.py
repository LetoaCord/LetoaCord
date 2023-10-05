import discord
import asyncio
from discord.ui import *
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=",", intents=intents)

TICKET_CHANNEL = 1151339209123180564 #Ticket ID

WELCOME_CHANNEL = 1157465883803926538 #Wekcome ID

GUILD_ID = 1093666992856252457 #Server ID

CATEGORY_ID = 1148801711222313100 #Support Channel

TEAM_ROLE = 1093666992910778451 #Permissions for Support

LOG_CHANNEL = 1156357149660819567 #Log Channel

@bot.event
async def on_ready():
    print(f"Successfully Booted {bot.user.name}!")
    bot.add_view(MyView())
    bot.add_view(delete())
    await bot.change_presence(activity=discord.Game('boosting-plug | Tickets'))

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL)
    embed = discord.Embed(title="boosting-plug | Welcome", description=f"**Welcome {member.mention} to boosting-plug, if you have any questions or concerns please create a ticket.**", color=0x9400ff)
    embed.set_image(url="https://cdn.discordapp.com/attachments/1057652912119107655/1156674826736517201/boosting-plugbanner.png?ex=6515d4e0&is=65148360&hm=1af98b049f21fc140d965037d1abf6e46a90578d05f2db37d46814f8bdf59d3c&")
    embed.set_footer(text="boosting-plug ©")
    await channel.send(embed=embed)

class MyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.select(
        custom_id="support",
        placeholder="Open A Ticket!",
        options=[
            discord.SelectOption(
                label="General Questions",
                emoji="❓",
                description="Have a question? Click Below",
                value="option1"
            ),
            discord.SelectOption(
                label="Members",
                emoji="<a:pg:1149556941778075710>",
                description="Have a question? Click Below",
                value="option2"
            ),
            discord.SelectOption(
                label="Bot Development",
                emoji="🛠",
                description="Have a question? Click Below",
                value="option3"
            ),
            discord.SelectOption(
                label="Tokens",
                emoji="<a:pg:1149556941778075710>",
                description="Have a question? Click Below",
                value="option4"
            ),
            discord.SelectOption(
                label="Server Boosts",
                emoji="<a:pg:1149556941778075710>",
                description="Want to Purchase server boost? Click Below",
                value="option5"
            ),
        ]
    )
    async def callback(self, select, interaction):
        if "option1" in interaction.data['values']:
            if interaction.channel.id == TICKET_CHANNEL:
                guild = bot.get_guild(GUILD_ID)
                for ticket in guild.channels:
                    if str(interaction.user) in ticket.name:
                        embed = discord.Embed(title=f"You can only open one Ticket!", description=f"Here is your opend Ticket --> {ticket.mention}", color=0x9400ff)
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        await asyncio.sleep(3)
                        embed = discord.Embed(title="boosting-plug | Tickets", color=0x9400ff)
                        await interaction.message.edit(embed=embed, view=MyView())
                        return
                category = bot.get_channel(CATEGORY_ID)
                ticket_channel = await guild.create_text_channel(f"ticket-{interaction.user.name}", category=category,
                                                                topic=f"Ticket from {interaction.user.name} \nUser-ID: {interaction.user}")

                await ticket_channel.set_permissions(guild.get_role(TEAM_ROLE), send_messages=True, read_messages=True, add_reactions=False,
                                                    embed_links=True, attach_files=True, read_message_history=True,
                                                    external_emojis=True)
                await ticket_channel.set_permissions(interaction.user, send_messages=True, read_messages=True, add_reactions=False,
                                                    embed_links=True, attach_files=True, read_message_history=True,
                                                    external_emojis=True)
                await ticket_channel.set_permissions(guild.default_role, send_messages=False, read_messages=False, view_channel=False)
                embed = discord.Embed(description=f'Welcome {interaction.user.mention}!\n'
                                                   'Our development team would like to thank you for opening a ticket with boosting-plug, please wait our support to respond.',
                                                color=0x9400ff)
                embed.set_image(url="https://cdn.discordapp.com/attachments/1057652912119107655/1156674826736517201/boosting-plugbanner.png?ex=6515d4e0&is=65148360&hm=1af98b049f21fc140d965037d1abf6e46a90578d05f2db37d46814f8bdf59d3c&")
                await ticket_channel.send("@everyone",embed=embed, view=delete())

                embed = discord.Embed(description=f'📬 Ticket was Created! Look here --> {ticket_channel.mention}',
                                        color=0x9400ff)
                await interaction.response.send_message(embed=embed, ephemeral=True)
                await asyncio.sleep(10000000000000000000000)
                embed = discord.Embed(title="boosting-plug | Tickets", color=0x9400ff)
                await interaction.message.edit(embed=embed, view=MyView())
                return
        if "option2" in interaction.data['values']:
            if interaction.channel.id == TICKET_CHANNEL:
                guild = bot.get_guild(GUILD_ID)
                for ticket in guild.channels:
                    if str(interaction.user) in ticket.name:
                        embed = discord.Embed(title=f"You can only open one Ticket", description=f"Here is your opend Ticket --> {ticket.mention}", color=0x9400ff)
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        await asyncio.sleep(3)
                        embed = discord.Embed(title="boosting-plug | Tickets", color=0x9400ff)
                        await interaction.message.edit(embed=embed, view=MyView())
                        return 
                category = bot.get_channel(CATEGORY_ID)
                ticket_channel = await guild.create_text_channel(f"ticket-{interaction.user.name}", category=category,
                                                                    topic=f"Ticket from {interaction.user.name} \nUser-ID: {interaction.user}")
                await ticket_channel.set_permissions(guild.get_role(TEAM_ROLE), send_messages=True, read_messages=True, add_reactions=False,
                                                        embed_links=True, attach_files=True, read_message_history=True,
                                                        external_emojis=True)
                await ticket_channel.set_permissions(interaction.user, send_messages=True, read_messages=True, add_reactions=False,
                                                        embed_links=True, attach_files=True, read_message_history=True,
                                                        external_emojis=True)
                await ticket_channel.set_permissions(guild.default_role, send_messages=False, read_messages=False, view_channel=False)
                embed = discord.Embed(description=f'Welcome {interaction.user.mention}!\n'
                                                   'Our development team would like to thank you for opening a ticket with boosting-plug, please wait our support to respond.',
                                                    color=0x9400ff)
                embed.set_image(url="https://cdn.discordapp.com/attachments/1057652912119107655/1156674826736517201/boosting-plugbanner.png?ex=6515d4e0&is=65148360&hm=1af98b049f21fc140d965037d1abf6e46a90578d05f2db37d46814f8bdf59d3c&")
                await ticket_channel.send("@everyone",embed=embed, view=delete())

                embed = discord.Embed(description=f'📬 Ticket was Created! Look here --> {ticket_channel.mention}',
                                        color=0x9400ff)
                await interaction.response.send_message(embed=embed, ephemeral=True)

                await asyncio.sleep(10000000000000000000000)
                embed = discord.Embed(title="boosting-plug | Tickets", color=0x9400ff)
                await interaction.message.edit(embed=embed, view=MyView())
                return
        if "option3" in interaction.data['values']:
            if interaction.channel.id == TICKET_CHANNEL:
                guild = bot.get_guild(GUILD_ID)
                for ticket in guild.channels:
                    if str(interaction.user) in ticket.name:
                        embed = discord.Embed(title=f"You can only open one Ticket", description=f"Here is your opend Ticket --> {ticket.mention}", color=0x9400ff)
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        await asyncio.sleep(3)
                        embed = discord.Embed(title="boosting-plug | Tickets", color=0x9400ff)
                        await interaction.message.edit(embed=embed, view=MyView())
                        return 
                category = bot.get_channel(CATEGORY_ID)
                ticket_channel = await guild.create_text_channel(f"ticket-{interaction.user.name}", category=category,
                                                                    topic=f"Ticket from {interaction.user.name} \nUser-ID: {interaction.user}")
                await ticket_channel.set_permissions(guild.get_role(TEAM_ROLE), send_messages=True, read_messages=True, add_reactions=False,
                                                        embed_links=True, attach_files=True, read_message_history=True,
                                                        external_emojis=True)
                await ticket_channel.set_permissions(interaction.user, send_messages=True, read_messages=True, add_reactions=False,
                                                        embed_links=True, attach_files=True, read_message_history=True,
                                                        external_emojis=True)
                await ticket_channel.set_permissions(guild.default_role, send_messages=False, read_messages=False, view_channel=False)
                embed = discord.Embed(description=f'Welcome {interaction.user.mention}!\n'
                                                   'Our development team would like to thank you for opening a ticket with boosting-plug, please wait our support to respond.',
                                                    color=0x9400ff)
                embed.set_image(url="https://cdn.discordapp.com/attachments/1057652912119107655/1156674826736517201/boosting-plugbanner.png?ex=6515d4e0&is=65148360&hm=1af98b049f21fc140d965037d1abf6e46a90578d05f2db37d46814f8bdf59d3c&")
                await ticket_channel.send("@everyone",embed=embed, view=delete())

                embed = discord.Embed(description=f'📬 Ticket was Created! Look here --> {ticket_channel.mention}',
                                        color=0x9400ff)
                await interaction.response.send_message(embed=embed, ephemeral=True)

                await asyncio.sleep(10000000000000000000000)
                embed = discord.Embed(title="boosting-plug | Tickets", color=0x9400ff)
                await interaction.message.edit(embed=embed, view=MyView())
                return
        if "option4" in interaction.data['values']:
            if interaction.channel.id == TICKET_CHANNEL:
                guild = bot.get_guild(GUILD_ID)
                for ticket in guild.channels:
                    if str(interaction.user) in ticket.name:
                        embed = discord.Embed(title=f"You can only open one Ticket", description=f"Here is your opend Ticket --> {ticket.mention}", color=0x9400ff)
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        await asyncio.sleep(3)
                        embed = discord.Embed(title="boosting-plug | Tickets", color=0x9400ff)
                        await interaction.message.edit(embed=embed, view=MyView())
                        return 
                category = bot.get_channel(CATEGORY_ID)
                ticket_channel = await guild.create_text_channel(f"ticket-{interaction.user.name}", category=category,
                                                                    topic=f"Ticket from {interaction.user.name} \nUser-ID: {interaction.user}")
                await ticket_channel.set_permissions(guild.get_role(TEAM_ROLE), send_messages=True, read_messages=True, add_reactions=False,
                                                        embed_links=True, attach_files=True, read_message_history=True,
                                                        external_emojis=True)
                await ticket_channel.set_permissions(interaction.user, send_messages=True, read_messages=True, add_reactions=False,
                                                        embed_links=True, attach_files=True, read_message_history=True,
                                                        external_emojis=True)
                await ticket_channel.set_permissions(guild.default_role, send_messages=False, read_messages=False, view_channel=False)
                embed = discord.Embed(description=f'Welcome {interaction.user.mention}!\n'
                                                   'Our development team would like to thank you for opening a ticket with boosting-plug, please wait our support to respond.',
                                                    color=0x9400ff)
                embed.set_image(url="https://cdn.discordapp.com/attachments/1057652912119107655/1156674826736517201/boosting-plugbanner.png?ex=6515d4e0&is=65148360&hm=1af98b049f21fc140d965037d1abf6e46a90578d05f2db37d46814f8bdf59d3c&")
                await ticket_channel.send("@everyone",embed=embed, view=delete())

                embed = discord.Embed(description=f'📬 Ticket was Created! Look here --> {ticket_channel.mention}',
                                        color=0x9400ff)
                await interaction.response.send_message(embed=embed, ephemeral=True)

                await asyncio.sleep(10000000000000000000000)
                embed = discord.Embed(title="boosting-plug | Tickets", color=0x9400ff)
                await interaction.message.edit(embed=embed, view=MyView())
                return
        if "option5" in interaction.data['values']:
            if interaction.channel.id == TICKET_CHANNEL:
                guild = bot.get_guild(GUILD_ID)
                for ticket in guild.channels:
                    if str(interaction.user) in ticket.name:
                        embed = discord.Embed(title=f"You can only open one Ticket", description=f"Here is your opend Ticket --> {ticket.mention}", color=0x9400ff)
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        await asyncio.sleep(3)
                        embed = discord.Embed(title="boosting-plug | Tickets", color=0x9400ff)
                        await interaction.message.edit(embed=embed, view=MyView())
                        return 
                category = bot.get_channel(CATEGORY_ID)
                ticket_channel = await guild.create_text_channel(f"ticket-{interaction.user.name}", category=category,
                                                                    topic=f"Ticket from {interaction.user.name} \nUser-ID: {interaction.user}")
                await ticket_channel.set_permissions(guild.get_role(TEAM_ROLE), send_messages=True, read_messages=True, add_reactions=False,
                                                        embed_links=True, attach_files=True, read_message_history=True,
                                                        external_emojis=True)
                await ticket_channel.set_permissions(interaction.user, send_messages=True, read_messages=True, add_reactions=False,
                                                        embed_links=True, attach_files=True, read_message_history=True,
                                                        external_emojis=True)
                await ticket_channel.set_permissions(guild.default_role, send_messages=False, read_messages=False, view_channel=False)
                embed = discord.Embed(description=f'Welcome {interaction.user.mention}!\n'
                                                   'Our development team would like to thank you for opening a ticket with boosting-plug, please wait our support to respond.',
                                                    color=0x9400ff)
                embed.set_image(url="https://cdn.discordapp.com/attachments/1057652912119107655/1156674826736517201/boosting-plugbanner.png?ex=6515d4e0&is=65148360&hm=1af98b049f21fc140d965037d1abf6e46a90578d05f2db37d46814f8bdf59d3c&")
                await ticket_channel.send("@everyone",embed=embed, view=delete())

                embed = discord.Embed(description=f'📬 Ticket was Created! Look here --> {ticket_channel.mention}',
                                        color=0x9400ff)
                await interaction.response.send_message(embed=embed, ephemeral=True)

                await asyncio.sleep(10000000000000000000000)
                embed = discord.Embed(title="boosting-plug | Tickets", color=0x9400ff)
                await interaction.message.edit(embed=embed, view=MyView())
                return

class delete(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Close Ticket 🎫", style = discord.ButtonStyle.red, custom_id="close")
    async def close(self, button: discord.ui.Button, interaction: discord.Interaction):
        channel = bot.get_channel(LOG_CHANNEL)
        embed = discord.Embed(
                description=f'Ticket is closing in 5 Sec.',
                color=0x9400ff)
        await asyncio.sleep(1)
        await interaction.response.send_message(embed=embed)
        await asyncio.sleep(5)
        await interaction.channel.delete(reason="Ticket closed by user")

@bot.slash_command(description="Sends Ticket Panel")
async def ticket(ctx):
    channel = bot.get_channel(TICKET_CHANNEL)
    embed = discord.Embed(description="> If you have a question or would like to purchase from boosting-plug, please click on the button corresponding to the type of ticket you wish to open.", color=0x9400ff)
    embed.set_author(name="boosting-plug | Support Tickets", icon_url="https://cdn.discordapp.com/attachments/1057652912119107655/1156674826736517201/boosting-plugbanner.png?ex=6515d4e0&is=65148360&hm=1af98b049f21fc140d965037d1abf6e46a90578d05f2db37d46814f8bdf59d3c&")
    embed.set_footer(text="boosting-plug ")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1057652912119107655/1156674826736517201/boosting-plugbanner.png?ex=6515d4e0&is=65148360&hm=1af98b049f21fc140d965037d1abf6e46a90578d05f2db37d46814f8bdf59d3c&")
    await channel.send(embed=embed, view=MyView())
    
bot.run('MTE1ODEyNTk2NzgxNDk1MDk3Mg.GlbXBe.afhyxmGNJ2GJZH-7qcVycnHA6T4HMnniizgBIg')