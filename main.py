from Keep_alive import keep_alive




dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8', '8.8.4.4']  

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

GUILD_ID = discord.Object(id=1321156782634045616)

@client.command(name="sync")
async def sync(ctx):
    if ctx.author.id == 1295292832721928232:
        try:
            await client.tree.sync(guild=GUILD_ID)
            await ctx.send("Slash commands synced!")
        except Exception as e:
            await ctx.send(f"Failed to sync commands: {str(e)}")
    else:
        await ctx.send("You don't have permission to use this command!")

@client.tree.command(name="log", description="logs a arrest", guild=discord.Object(id=GUILD_ID.id))
async def log_command(interaction: discord.Interaction, user: str, suspect: str, reason: str, charges: str):
    embed = discord.Embed(
        title="**Los Police Department | Arrest Log**",
        description="",
        color=0x2C4C8F
    )

    embed.set_image(url="https://cdn.discordapp.com/attachments/1345612602650132520/1348039097347735636/image7.jpg?ex=67d1f73e&is=67d0a5be&hm=63dbf89e3521fff8a4e371b2c5915f00889a6a1448eae934e2c6f191f8f8ed64&")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1345612602650132520/1345615751515602944/IMG_5350.png?ex=67d260d3&is=67d10f53&hm=bc40855f349370cb7217ae77da5a2b1239d32d4e05441921a368418084598c31&")
    embed.add_field(name="Officer Name:", value=f"{user}", inline=True)
    embed.add_field(name="Suspect:", value=f"{suspect}", inline=True)
    embed.add_field(name="Reason:", value=f"{reason}", inline=True)
    embed.add_field(name="Charges:", value=f"{charges}", inline=True)
    embed.set_footer(text="Property of Lawrence Police Department")
    embed.set_author(name="Lawrence Police Department", icon_url="https://cdn.discordapp.com/attachments/1345612602650132520/1345615828204126288/IMG_5345.png?ex=67d260e5&is=67d10f65&hm=bf679c2ae195b3e1dc924025d2c1969f5218edbc036026d2f14c5f3712f4dbf4&")
    await interaction.response.send_message(embed=embed)

@client.tree.command(name= "citation", description= "log a citation", guild=discord.Object(id=GUILD_ID.id))
async def send_embed(interaction: discord.Interaction, name: str, suspect: str, location: str, violation: str, signature: str):
    embed = discord.Embed(title=" **Los Angeles Police Department | Citation Log**", description="",color=0x03205a)

    embed.set_image(url="https://cdn.discordapp.com/attachments/1345612602650132520/1356793689204068412/Screenshot_2025-04-01_175323.png?ex=67f32217&is=67f1d097&hm=7ae242549d30638e004c28305e8681043aa779748852108421d70136d9350453&")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1345612602650132520/1356830574744047817/IMG_5738.png?ex=67f34471&is=67f1f2f1&hm=9495db519f6062903e709a24619068d41d4dd075193495cf29a406e5153a08eb&")
    embed.add_field(name="Officer Name:", value=f"{name}", inline=True)
    embed.add_field(name="Suspect:", value=f"{suspect}", inline=True)
    embed.add_field(name="Reason:", value=f"{location}", inline=True)
    embed.add_field(name="Charges:", value=f"{violation}", inline=True)
    embed.add_field(name="Charges:", value=f"{signature}", inline=True)
    embed.set_footer(text="Property of Los Angeles Police Department")
    embed.set_author(name="Los Angeles Police Department", icon_url="https://cdn.discordapp.com/attachments/1345612602650132520/1356830574744047817/IMG_5738.png?ex=67f34471&is=67f1f2f1&hm=9495db519f6062903e709a24619068d41d4dd075193495cf29a406e5153a08eb&")
    
    general_channel = interaction.guild.get_channel(1349265967301263401) 
    await general_channel.send(embed=embed)
    await interaction.response.send_message("Your log was sent!", ephemeral=True)

@client.tree.command(name="addrole", description="Adds a role to a user", guild=GUILD_ID) 
async def addrole(interaction: discord.Interaction, member: discord.Member, role: discord.Role):
    try:
        await member.add_roles(role)
        await interaction.response.send_message(f"{member.mention} has been given the {role.name} role!", ephemeral=True)
    except discord.HTTPException as e:
        await interaction.response.send_message(f"Failed to add role: {e}")

@client.tree.command(name="promote", description="Promotes a member to a new rank", guild=GUILD_ID)
async def promote(interaction: discord.Interaction, member: discord.Member, new_rank: discord.Role, feedback: str):
    if not interaction.user.guild_permissions.manage_roles:
        await interaction.response.send_message("You don't have permission to use this command!", ephemeral=True)
        return
        
    try:
        await member.add_roles(new_rank)
        # Send DM to the promoted member
        dm_embed = discord.Embed(
            title="🎉 Congratulations on Your Promotion!",
            description=f"You have been promoted to {new_rank.name} in the Los Angeles Police Department.",
            color=0x03205a
        )
        dm_embed.set_image(url="https://cdn.discordapp.com/attachments/1345612602650132520/1356791294214672535/Screenshot_2025-04-01_174022.png?ex=67f31fdc&is=67f1ce5c&hm=0ac6c82631e980c23cddfce3a1eac6f918d591d7013a0baa3f4decedbe443fea&")
        dm_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1345612602650132520/1356830574744047817/IMG_5738.png?ex=67f34471&is=67f1f2f1&hm=9495db519f6062903e709a24619068d41d4dd075193495cf29a406e5153a08eb&")
        dm_embed.add_field(name="Officer:", value=f"{member.name}", inline=True)
        dm_embed.add_field(name="New Rank:", value=f"{new_rank.name}", inline=True)
        dm_embed.add_field(name="feedback:", value=f"{feedback}", inline=True)
        dm_embed.add_field(name="Administration:", value=f"{interaction.user.name}", inline=True)
        try:
            await member.send(embed=dm_embed)
        except discord.Forbidden:
            # If DM fails, continue with the promotion announcement
            pass
            
        embed = discord.Embed(
            title="**<:LAPD:1356795262961586176> LAPD | Promotion Notice**",
            description="_Congratulations on your promotion, We appreciate your hard work and dedication._",
            color=0x03205a)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1345612602650132520/1356791294214672535/Screenshot_2025-04-01_174022.png?ex=67f31fdc&is=67f1ce5c&hm=0ac6c82631e980c23cddfce3a1eac6f918d591d7013a0baa3f4decedbe443fea&")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1345612602650132520/1356830574744047817/IMG_5738.png?ex=67f34471&is=67f1f2f1&hm=9495db519f6062903e709a24619068d41d4dd075193495cf29a406e5153a08eb&")

        embed.add_field(name="Officer:", value=f"{member.mention}", inline=True)
        embed.add_field(name="New Rank:", value=f"{new_rank.name}", inline=True)
        embed.add_field(name="feedback:", value=f"{feedback}", inline=True)
        embed.add_field(name="Administration:", value=f"{interaction.user.mention}", inline=True)
        embed.set_footer(text="Los Angeles Police Department")
        embed.set_author(name="Los Angeles Police Department", icon_url="https://cdn.discordapp.com/attachments/1345612602650132520/1356830574744047817/IMG_5738.png?ex=67f34471&is=67f1f2f1&hm=9495db519f6062903e709a24619068d41d4dd075193495cf29a406e5153a08eb&")
        guild = interaction.guild
        general_channel = guild.get_channel(1321160856121118771)
        await general_channel.send(f"{member.mention}", embed=embed)
        await interaction.response.send_message(f"{member.mention} has been promoted to {new_rank.name}!", ephemeral=True)
    except discord.HTTPException as e:
        await interaction.response.send_message(f"Failed to promote member: {e}", ephemeral=True)
    
     
@client.tree.command(name="infraction", description="Log an infraction", guild=GUILD_ID)
async def infraction(interaction: discord.Interaction, member: discord.Member, reason: str, punishment: str, notes: str):
    if not interaction.user.guild_permissions.kick_members:
        await interaction.response.send_message("You don't have permission to use this command!", ephemeral=True)
        return

    embed = discord.Embed(
        title="**<:LAPD:1356795262961586176> LAPD | Infraction Notice**",
        description="_Open a Internal Affairs Ticket if this isn't correct._",
        color=0x03205a
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1345612602650132520/1356791293791043735/Screenshot_2025-04-01_173940.png?ex=67f31fdc&is=67f1ce5c&hm=df2019950cb325f75520c29cc519565c782e0c6febe814cb706cb61e5d2202d2&")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1345612602650132520/1356830574744047817/IMG_5738.png?ex=67f34471&is=67f1f2f1&hm=9495db519f6062903e709a24619068d41d4dd075193495cf29a406e5153a08eb&")
    embed.add_field(name="Member:", value=member.mention, inline=True)
    embed.add_field(name="Reason:", value=reason, inline=True)
    embed.add_field(name="Punishment:", value=f"**{punishment}**", inline=True)
    embed.add_field(name="Notes:", value=notes, inline=True)
    embed.add_field(name="Issued By:", value=interaction.user.mention, inline=True)
    embed.set_footer(text="Los Angeles Police Department")
    embed.set_author(name="Los Angeles Police Department", icon_url="https://cdn.discordapp.com/attachments/1345612602650132520/1356830574744047817/IMG_5738.png")

    logs_channel = interaction.guild.get_channel(1321160939499814992)
    await logs_channel.send(f"{member.mention}", embed=embed)
    await interaction.response.send_message(f"Infraction logged for {member.mention}", ephemeral=True)

@client.event
async def on_ready():
    print('Logged on as', client.user)
    client.loop.create_task(my_background_task())

async def my_background_task():
    await client.wait_until_ready()
    await client.change_presence(
        status=discord.Status.idle,
        activity=discord.Activity(type=discord.ActivityType.watching, name="Over Los Angeles Police Department")
    )

    while True:
        print("Background task running")
        await asyncio.sleep(10) 
        await client.change_presence(
            status=discord.Status.idle,
            activity=discord.Activity(type=discord.ActivityType.watching, name="Over the Police Department")
        )

keep_alive()
dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)

