import discord
from discord.ext import commands
import os
from database import bizzHackBot_db as bhb_db

#static API key
api_key = os.environ.get("discbot")

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
  print('the bot is ready')

@bot.command()
async def quiz(ctx):
    #some question and 4 answers
    pass

def main():
    bhb_db.create_question_table()
    bhb_db.create_question_answer_table()
    bot.run(api_key)

if __name__ == "__main__":
    main()