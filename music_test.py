from secrets import MUSIC_TOKEN, DEV_ID
import discord
from discord.ext import commands
import youtube_dl


'''
Основной файл музыкального бота. Запусти его что бы бот заработал.
На борту имеет команды:
    !connect - присоединяет бота к голосовому каналу автора.
    !disconnect - отключает бота от всех голосовых каналов.
    !play - проигрывает музыку доступную по ютубовской ссылке или просто воспроизводит поочереди все что есть в плейлисте.
    !pause - приостанавливает воспроизведение музыки в голосовом канале.
    !resume - продолжает воспроизведение если трек был поставлен на паузу.
    !stop - останавливает воспроизведение музыки в голосовом канале и отключается от канала.
    !add - добавляет ссылку в прейлист
    !playlist - отображает текущий плейлист
    !clear - очищает плейлист
'''

# ============== Channel IDs as int ==============
tst_bot = 882679504177356870 # testing text channel for bot development
PLAY_LIST = []
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}
YDL_OPTIONS = {
    'format': 'bestaudio',
}

# ============== Funcions block ==============
bot = commands.Bot(command_prefix="!")
#bot.remove_command("help") # TODO uncomment this line after developement

class Music(commands.Cog): # обязательная строка. измени название класса по потребности.
    def __init__(self, client): # обязательная строка.
        self.client = client # обязательная строка.

    @commands.command()
    async def connect(self, ctx):
        '''Подключает бота к голосовому каналу автора.'''
        if ctx.author.voice is None:
            await ctx.send("Вам необходимо зайти в голосовой канал!")
        else:
            v_channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await v_channel.connect()
            else:
                await ctx.voice_client.move_to(v_channel)

    @commands.command()
    async def disconnect(self, ctx):
        '''Отключает бота от голосового канала.'''
        for v_client in self.voice_clients:
            await v_client.disconnect()
            await ctx.send("Бот вышел из чата.")

    @commands.command()
    async def play(self, ctx, url=None):
        '''Воспроизводит музыку в голосовом канале, принимает url в виде
        ссылки на youtube видео или youtube музыку. Если параметры не 
        переданы, воспроизводит треки из плейлиста.'''
        global PLAY_LIST
        async def play_url(urls:list):
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                for url in urls:
                    if isinstance(url, str): # проверяем является ли url строкой
                        if not url.startswith("https://r4--"):
                            info = ydl.extract_info(url, download=False)
                            source_url = info['formats'][0]['url']
                        else: 
                            source_url = url
                    else:
                        source_url = url['formats'][0]['url']

                    source = await discord.FFmpegOpusAudio.from_probe(source_url, **FFMPEG_OPTIONS)
                    v_client.play(source)

        if ctx.author.voice is None:
            await ctx.send("Вам необходимо зайти в голосовой канал!")
        else:
            await self.connect(ctx)
            v_client = ctx.voice_client
            if url is None:
                if PLAY_LIST != []:
                    await play_url(PLAY_LIST)
                else:
                    ctx.send("Плейлист пока пустой. Добавь в него треки командой !add и повтори попытку или добавь ссылку на youtube видео к команде !play")
            else:
                url = [url]
                await play_url(url)

    @commands.command()
    async def stop(self, ctx):
        '''Останавливает воспроизведение музыки в голосовом канале'''
        if ctx.author.id == DEV_ID:
            for v_client in bot.voice_clients:
                v_client.stop()

    @commands.command()
    async def pause(self, ctx):
        '''Приостанавливает воспроизведение музыки в голосовом канале'''
        if ctx.author.id == DEV_ID:
            for v_client in bot.voice_clients:
                v_client.pause()

    @commands.command()
    async def resume(self, ctx):
        '''Продолжает воспроизведение музыки в голосовом канале'''
        if ctx.author.id == DEV_ID:
            for v_client in bot.voice_clients:
                v_client.resume()

    @commands.command()
    async def add(self, ctx, url):
        '''Добавляет трек в плейлист'''
        global PLAY_LIST
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            print(url)
            info = ydl.extract_info(url, download=False)
        PLAY_LIST.append(info)
        await ctx.send(f"{info['title']} добавлен в плейлист")

    @commands.command()
    async def playlist(self, ctx):
        '''Выводит список треков в плейлисте'''
        global PLAY_LIST
        message = ""
        n = 1
        for track in PLAY_LIST:
            message = message + f"{n}. {track['title']}\n"
            n += 1
        embed = discord.Embed(
            description=message,
            color=discord.Colour.purple()
        )    
        await ctx.send(embed=embed)

    @commands.command()
    async def clear(self, ctx):
        '''Очищает плейлист'''
        global PLAY_LIST
        PLAY_LIST = []
        await ctx.send("playlist cleared")


# ============== MAIN LOOP ==============
#bot.run(MUSIC_TOKEN)