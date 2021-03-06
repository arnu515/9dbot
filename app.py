from discord.ext.commands import Bot, Context
import discord
import os
import json

client = Bot(command_prefix="!")

bad_words = []
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "badwords.json")) as f:
    bad_words = json.load(f)["words"]


def contains_bad_word(sentence: str) -> bool:
    words = sentence.split()
    for word in words:
        if word.lower() in bad_words:
            return True

    return False


@client.command(name="source", help="Get the source code for the bot")
async def source_command(ctx: Context):
    await ctx.channel.send("""The source code for this bot is avaliable on **Github!**
    
    Feel free to take a look at: https://github.com/arnu515/9dbot
    """)


@client.event
async def on_ready():
    print("Connected to Discord as: " + client.user.name)


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if contains_bad_word(message.content):
        print("Deleting message by " +
              message.author.name + ": " + message.content)
        await message.delete()

if __name__ == "__main__":
    print("Running the bot...")
    try:
        client.run(os.getenv("TOKEN"))
    except Exception as e:
        print("An error occured: " + str(e))
