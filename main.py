from secrets import COMMAND_TOKEN, DEV_ID
from discord.ext import commands
import os

'''
Основной файл бота. Запусти его что бы бот заработал.
На борту имеет команды:
    $$clear - Удаляет указанное количество сообщений, по умолчанию 1
    $$load - Загружает указанный Cog файл если позволено.
    $$unload - Выгружает указанный Cog файл из программы если позволено.
    $$reload - Перезагружает указанный Cog файл если позволено.
'''

# ============== Channel IDs as int ==============
tst_bot = 882679504177356870 # testing channel for bot development


# ============== Funcions block ==============

bot = commands.Bot(command_prefix=["!", "$$"])
#bot.remove_command("help") # TODO uncomment this line after developement

@bot.event
async def on_ready():
    print(f"Подключен как {bot.user} и готов к бою!")

@bot.command()
async def clear(ctx, count=1):
    '''Удаляет указанное количество сообщений, по умолчанию 1'''
    if ctx.author.id == DEV_ID and ctx.prefix == "$$" and ctx.channel.id == tst_bot:
        await ctx.channel.purge(limit=count)

@bot.command()
async def load(ctx, extension):
    '''Загружает указанный Cog файл если позволено.'''
    if ctx.author.id == DEV_ID and ctx.prefix == "$$":
        bot.load_extension(f"commands.{extension}")
        await ctx.send(f"{extension} загружен")
    else:
        await ctx.send("Действие не разрешено.")

@bot.command()
async def unload(ctx, extension):
    '''Выгружает указанный Cog файл из программы если позволено.'''
    if ctx.author.id == DEV_ID and ctx.prefix == "$$":
        bot.unload_extension(f"commands.{extension}")
        await ctx.send(f"{extension} выгружен")
    else:
        await ctx.send("Действие не разрешено.")

@bot.command()
async def reload(ctx, extension):
    '''Перезагружает указанный Cog файл если позволено.'''
    if ctx.author.id == DEV_ID and ctx.prefix == "$$":
        bot.unload_extension(f"commands.{extension}")
        bot.load_extension(f"commands.{extension}")
        await ctx.send(f"{extension} перезагружен")
    else:
        await ctx.send("Действие не разрешено.")

# Проходит циклом по файлам в каталоге ./commands для их загрузки.
for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        cog_name = filename[:-3] # срез необходим что бы избавиться от расширения файла
        bot.load_extension(f"commands.{cog_name}")
        print(f"{cog_name} загружен")



# ============== MAIN LOOP ==============
bot.run(COMMAND_TOKEN)
