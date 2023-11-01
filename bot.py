#1154431205538803784 application id
#MTE1NDQzMTIwNTUzODgwMzc4NA.GmqYVa.GzQGScYFo6CEPSSDOffB4pSxnsJljiIzKymKv4
#8

import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
queues = {}

def check_queue(ctx, id):
    if queues[id] != []:
        voice = ctx.guild.voice_client
        source = queues[id].pop(0)
        player = voice.play(source)


@client.event
async def on_ready():
    print("Loggen in as " + str(client.user))

@client.command()
async def hello(ctx):
    await (ctx.send("วอดซับ"))

@client.event
async def on_member_join(member):
    channel = client.get_channel(1161738682584289302)
    await channel.send(f"อันยองออนนี่  {member.name}")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1161738682584289302)
    await channel.send(f"{member.name} แบร่")

@client.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
    else:
        await ctx.send("เข้าห้องก่อน!!")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("มึนไร")
    
@client.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    if voice.is_playing:
        voice.pause()
    else:
        await ctx.send("เปิดเพลงก่อนพี่")

@client.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("ไม่มีเพลงโว้ย")

@client.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    voice.stop()

@client.command(pass_context = True)
async def play(ctx, arg):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio(arg + ".wav")
    player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.guild.id))

@client.command(pass_context = True)
async def queue(ctx, arg):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio(arg + ".wav")
    player = voice.play(source)

    guild_id = ctx.message.guild.id

    if guild_id in queues:
        queues[guild_id].append(source)
    else:
        queues[guild_id] = [source]

    await ctx.send("เพิ่มละ")



client.run("MTE1NDQzMTIwNTUzODgwMzc4NA.GmqYVa.GzQGScYFo6CEPSSDOffB4pSxnsJljiIzKymKv4")