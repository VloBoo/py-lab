import discord
from discord.ext import commands
import logging
from gtts import gTTS

#логги
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN ='NzgzNTg1ODA5ODUyMzk5NjY2.GkUZA_.PKc2szRpHhdVcOoRniC8FWU0g9LnzzPs5PBtVk'

client = discord.Client(activity=discord.Activity(name='Python', type=discord.ActivityType.watching))

@client.event
async def on_ready():
    print('Запуск бота {0.user} завершен'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('$help'):
        await message.channel.send('```\n$help - Список команд\n$ping - Проверка соединения\n$play - Преобразует текст в речь (файл)\n$stop - Остановка бота```')

    if message.content.startswith('$ping'):
        await message.channel.send('Pong!')
        
    if message.content.startswith('$stop'):
        await client.close()
        
    if message.content.startswith('$play'):
        author = message.author
        voice = message.guild.voice_channels
        for v in voice:
            for m in v.members:
                if author == m:
                    await message.channel.send(f'Ты сидишь в голосовом канале \'{v.name}\'')
                    vc = await v.connect()
                    #vc.play(discord.FFmpegPCMAudio(executable="P:\Overwolf\0.168.0.12\obs\bin\64bit\ffmpeg.exe",source=".\buf.mp3"), after=lambda e: print('done', e)) #Временно не работате
                    #v.disconnet()
                    s = gTTS(message.content)
                    s.save('buf.mp3')
                    await message.channel.send('Твой файл',file=discord.File('buf.mp3')) # временная реализация голосового в чат, в будущем будет отправка в сам голосовой чат.
                    return
        #В библиотеке беды с кешированием, если ты до запуска был в голосовом канале, то тебя не найдут
        await message.channel.send('Мы тебя не нашли')

#библиотека по умолчанию пытается получить все шлюзы дискорда, не понимаю, зачем, у меня и так бот с пингом большим, а тут еще и лишний трафик
client.run(TOKEN)