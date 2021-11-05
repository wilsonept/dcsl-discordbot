from discord.ext import commands
from random import choice
import re

'''
Этот файл содержит Coin_Toss Cog класс.
Добавляет боту команду !coin <*args>. Позволяет бросать жребий. При простом использовании просто скажет орел или решка.
Команда принимает аргументы в качестве никнеймов пользователей сервера в формате дискорда @nickname.
Что бы бросить жребий например вчетвером достаточно использовать команду: !coin @user1 @user2 @user3 @user4
В ответ бот назовет кто победил.
'''
        
MESSAGES = {
    "winner": [
        "{author} бросает монеткой прямиком в лоб {opponent} и побеждает в этой неравной схватке умов."
    ],
    "loser": [
        "{author} бросает монетку в унитаз. В этой схватке умов с огромным отрывом побеждает {opponent}"
    ],
    "weirdo": [
        "{author} любит поиграть сам с собой, в монетку конечно же...",
        "{author} кинул монетку к себе в рот и чуть не задохнулся. Держите монеты от него подальше."
    ],
    "threesome": [
        "Тройничек прошел отлично, {opponent} самый симпатичный",
        "Тянули жребий трое. {opponent} быстро победил, совсем без геморроя"
    ],
    "orgy": ["Тусовка бурная была лишь {opponent}'у и не дали, но это плюс раз чистый он, ведь все ушли с цветами."],
    "common": [":coin:", ":eagle:"]
}

class CoinToss(commands.Cog): # CoinToss cog класс, доступен каждому на сервере.
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def coin(self, ctx, *args):
        '''Позволяет бросать жребий. При простом использовании просто скажет орел или решка.
Команда принимает аргументы в качестве никнеймов пользователей сервера в формате дискорда @nickname.
Что бы бросить жребий например вчетвером достаточно использовать команду: !coin @user1 @user2 @user3 @user4.
В ответ бот назовет победителя.'''

        author = f"<@!{ctx.message.author.id}>" # получаем автора тут, так как используем эту переменную как в проверках так и после них.
        opponent = '' # нужна здесь для того чтобы метод replace в конце функции не выдал ошибку если во время проверки эта переменная не будет определена.

        if args != ():
            opponents = [user for user in args if re.match('<@.+>', user)]
            if len(opponents) == 0:
                status = "common"
            elif len(opponents) == 1:
                opponent = opponents[0]
                if author != opponent:
                    status = choice(["winner", "loser"]) # если два игрока.
                else:
                    status = "weirdo" # если игрок играет сам с собой.
            elif len(opponents) > 1:
                opponent = choice(opponents)
                if len(opponents) == 3:
                    status = choice(["threesome", "orgy"]) # если три игрока. WARNING данная строка корректна до тех пор пока сообщения "orgy" не имеют в себе конкретики касающейся четырех и более человек.
                else:
                    status = "orgy" # если более трех игроков.
            else:
                status = "common" # если переданные в качестве параметров имена не прошли проверку на валидность.
        else:
            status = "common" # если не передано имен игроков в качестве параметров.

        message = choice(MESSAGES[status]).replace("{author}", author).replace("{opponent}", opponent) # приводим шаблон к желаемому виду.
        await ctx.send(message)

def setup(bot):
    bot.add_cog(CoinToss(bot))