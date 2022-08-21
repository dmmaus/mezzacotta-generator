import discord
from datetime import datetime
import generique
from albumart import AlbumArt

class GenClient(discord.Client):
    def __init__(self):
        discord.Client.__init__(self)

        self.request = None
        self.count = 1
        self.my_channel = None
        self.templates = {}

        self.register_template('dish', 'A restaurant dish', ['dish/base'])
        self.register_template('dungeon', 'An RPG dungeon module', ['dungeon/module', 'dungeon/attribution', 'dungeon/adventure'])
        self.register_template('releasenote', 'Release note item for an online RPG', ['releasenote/release-note'])
        self.register_template('game', 'A board and description', ['game/title-full', 'game/desc-paragraph-1', 'game/desc-paragraph-2', 'game/desc-paragraph-3'])
        self.register_template('insult', 'A medieval style insult', ['insult/base'])
        self.register_template('moon', 'An absurd supermoon', ['supermoon/moon'])
        self.register_template('movie', 'A movie title and synopsis', ['movie/title', 'movie/directed', 'movie/synopsis'])
        self.register_template('law', 'An obscure law for some part of the world', ['law/base'])
        self.register_template('babble', 'A line of technobabble from sci-fi', ['technobabble/babble'])
        self.register_template('village', 'A quaint village and it\'s famous festival', ['village/base', 'village/festival-base'])
        self.register_template('band', 'A band name', ['band/base'])
        self.register_template('wine', 'The name of a wine, and it\'s description', ['dish/wine-name', 'dish/wine-description'])


    async def on_ready(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print(dt_string)
        print('------')

    async def on_message(self, message):
        if message.author == client.user:
            return

        smsg = message.content.split()
        if len(smsg) == 0:
            return

        if smsg[0] == '!gen':
            self.my_channel = message.channel

            if len(smsg) == 1:
                await self.generate(self.request, self.count)
            elif len(smsg) == 2:
                self.request = smsg[1]
                await self.generate(self.request, 1)
            elif len(smsg) == 3 and smsg[2].isnumeric():
                self.request = smsg[1]
                self.count = min(5, int(smsg[2]))
                await self.generate(self.request, self.count)

        if smsg[0] == '!templates':
            msg = ':information_source: Available templates are:\n'
            for t in sorted(self.templates.keys()):
                msg += '**{}**: {}\n'.format(t, self.templates[t]['desc'])
            await message.channel.send(msg)

        if smsg[0] == '!album':
            # Random generation of a band, album and keywords
            res = generique.generate(['band/keywords', 'band/album', 'band/base', '1'])[0]
            album_title = res.split('~~')[1].strip()
            band_name = res.split('~~')[2].strip()

            keywords = []
            for a in res.split('~~')[0].split('~'):
                keywords.append(a.strip())

            album = AlbumArt(band_name, album_title, keywords)
            cover = album.generate()
            album.emit()

            await message.channel.send(':game_die: Your random album cover. (WARNING - may be NSFW)', file=discord.File('res.jpg', 'SPOILER_album.jpg'))




    def register_template(self, n, desc, parts):
        self.templates[n] = {'parts': parts, 'desc': desc}

    async def generate(self, n, count=1):
        if n not in self.templates.keys():
            await self.my_channel.send(':warning: Unknown template')
        else:
            for i in range(count):
                res = generique.generate(self.templates[n]['parts'] + ['1'])[0]
                msg = ':game_die: '
                for part in res.split('~~'):
                    msg += part.strip() + '\n'
                await self.my_channel.send(msg)


if __name__ == '__main__':
    tokenfile = open('token.txt', 'r')
    TOKEN = tokenfile.readline().strip()
    client = GenClient()
    client.run(TOKEN)

