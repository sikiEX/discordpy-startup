from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def atk(ctx):
    await ctx.send('::atk')
    
    
@bot.command()
async def login(ctx):
    await ctx.send('::login')
    

bot.run(token)
