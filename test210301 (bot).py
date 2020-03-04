import discord
import asyncio
from discord.ext import commands
import requests

response = requests.get('https://example.org')

bot = commands.Bot(command_prefix='.')

chn_id = 682156076342312964

@bot.event
async def on_ready():
    print("logged in as :",bot.user.name)
    print("ID: ",bot.user.id)

@bot.event
async def on_message(message):
    if message.content.startswith('salut'):
        await bot.get_channel(chn_id).send('hellooo')

@bot.command()
async def msg(ctx, *, message):
    await bot.get_channel(chn_id).send(message)

@bot.command()
async def edt(ctx, *, messages):
    await bot.get_channel(chn_id).send('hzllo')

bot.run("NjgyMTU3MjUxMzIyMTgzNjgw.XlZ6CA.MlpGr-Das5j0PHd8oGPD9G3UZIk")
