import discord
import requests
from discord.ext import commands

'''
Получение статистики.
Пока только для Quake Champions, делает API запрос и возвращает дуэльный рейтинг, рейтинг 2на2 и ссылку на полную статистику.
В планах проработать команду таким образом что бы она дергала API для каждой роли пользователя вызвавшего команду.
'''

ENDPOINTS = {
    "QUAKE": "https://quake-stats.bethesda.net/api/v2/Player/Stats/?name=",
}

class Stats(commands.Cog): # обязательная строка. измени название класса по потребности.
    def __init__(self, client): # обязательная строка.
        self.client = client # обязательная строка.

    @commands.command() # тоже самое что и bot.command но для Cog файлов
    async def stats(self, ctx):

        def quake_template(nickname:str, duel:str, tdm:str, icon:str, href:str): # добавить matches
            embed = discord.Embed(
                    description="Quake stats",
                    color=discord.Colour.blue()
            )
            embed.set_author(name=nickname, icon_url=icon_url)
            #embed.add_field(name="matches", value=matches, inline=True)
            embed.add_field(name="duel", value=duel, inline=True)
            embed.add_field(name="2v2", value=tdm, inline=True)
            embed.add_field(name="link", value=f"[more stats here]({stats_url})", inline=False)
            return embed

        # TODO
        ## получение ролей
        ## цикл по ролям для получения статистики.
        
        nickname = ctx.author.display_name
        ENDPOINT = ENDPOINTS["QUAKE"] + nickname
        response = requests.get(ENDPOINT)
        response.raise_for_status()
        stats = response.json()

        if stats.code != 404:
            duel = str(stats["playerRatings"]["duel"]["rating"])
            tdm = str(stats["playerRatings"]["tdm"]["rating"])
            icon_url = "https://dev.quake-champions.com/css/images/profile_icons/" + stats["playerLoadOut"]["iconId"] + ".png"
            stats_url = "https://dev.quake-champions.com/profile/" + nickname

            embed = quake_template(nickname, duel, tdm, icon_url, stats_url) # добавить matches

            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Не нашел статистику для {nickname} :tired_face:")

def setup(bot): # обязательная строка.
    bot.add_cog(Stats(bot)) # обязательная строка. убедись что название класса совпадает с названием класса объявленным ранее.
