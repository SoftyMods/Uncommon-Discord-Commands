import os
import sys
import json
import asyncio
import discord
from discord.ext import commands
from json import load


# Put this right under imports
# -------------------------------------
def restart():
    print("Config changed reloading the bot.")
    import os
    os.execv(sys.executable, ['python'] + sys.argv)
# -------------------------------------

# Put this where you have your other commands
# -------------------------------------
@bot.command()
async def edit(ctx, word_to_Edit, new_Config):
    config_File = open("config.json", "r")
    json_object = json.load(config_File)
    config_File.close()

    json_object[word_to_Edit] = new_Config #Magic happens here!

    await ctx.send(f"Changed `{word_to_Edit}` to `{new_Config}`")
    await asyncio.sleep(0.2)

    config_File = open("config.json", "w")
    json.dump(json_object, config_File, indent=4)

    config_File.close()

    restart()
# -------------------------------------
