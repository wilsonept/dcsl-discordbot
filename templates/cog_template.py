from discord.ext import commands



'''
Это темплейт для Cog файлов.
Используй этот темплейт для того что бы начать разрабатывать каждую новую команду для бота.
Не удаляй обязательные строки и будет счастье. :)
Обязательно изменить название класса MyCog на название новой команды в формате PascalCase, саму функцию команды в формате snake_case
'''

class MyCog(commands.Cog): # обязательная строка. измени название класса по потребности.
    def __init__(self, client): # обязательная строка.
        self.client = client # обязательная строка.

    @commands.Cog.listener() # тоже самое что и @event но для Cog файлов
    async def on_ready(self):
        print("cog_template.py loaded")

    @commands.command() # тоже самое что и bot.command но для Cog файлов
    async def test(self, ctx):
        '''Send Hello world message'''
        await ctx.send("Hello, World!")

def setup(bot): # обязательная строка.
    bot.add_cog(MyCog(bot)) # обязательная строка. убедись что название класса совпадает с названием класса объявленным ранее.