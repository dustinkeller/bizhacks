import discord
from discord.ext import commands
import os
from database import bizzHackBot_db as bh_db
from QuestionAnswer import Question as q
from dataVizulation import bizzHackGraph as bh_g
import asyncio

#static API key
api_key = os.environ.get("discbot")

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
  print('the bot is ready')

@bot.command()
async def quiz(ctx):
    user = ctx.author
    llm = 'gpt-3.5-turbo'
    interests = 'music'
    topic = 'algebra'
    ask_question = q.problem(interests, topic, llm)
    answer = q.check_answer(ask_question, llm)
    await ctx.send(ask_question)
    def check(response):
        return response.author == ctx.author and response.channel == ctx.channel
    try:
        response = await bot.wait_for('message', check=check, timeout=60)  # Wait for a response for 60 seconds
        
        if response.content.strip().lower() == answer.strip().lower():
            bh_db.insert_question_answer(user, ask_question, answer, 1)
            await ctx.send("Correct answer!")
        else:
            bh_db.insert_question_answer(user, ask_question, answer, 0)
            await ctx.send("Incorrect answer. Please try again.")
    except asyncio.TimeoutError:
        await ctx.send("Sorry, you took too long to respond.")

async def stats(ctx, *, user=None):
    if user == None:
        user = ctx.message.author
    else:
        pass

    df = bh_db.individual_score(user)
    user = df['user_name'][0]
    questions_correct = df['points'].sum()
    questions_wrong = len(df['points'])-questions_correct
    grade = questions_correct/questions_wrong

    embed = discord.Embed(title=f"Questions done by {user}", description=f'Grade: {grade:.0f}')
    embed.add_field(name='Questions Correct', value=f'{questions_correct}')
    embed.add_field(name='Questions Wrong', value=f'{questions_wrong}')

    file = bh_g.stats(user)
    image = discord.File(file, filename='graph.png')
    embed.set_image(url=f'attachment://graph.png')
    await ctx.send(file=image, embed=embed)

def main():
    bh_db.create_question_table()
    bh_db.create_question_answer_table()
    bot.run(api_key)

if __name__ == "__main__":
    main()