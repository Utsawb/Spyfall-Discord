from discord.ext import commands
import random
class Game():
    def __init__(self, ctx):
        self.state = False
        self.channel = ctx.guild.id
        self.players = []
        self.places = ['Airplane', 'Bank', 'Beach', 'Cathedral', 'Circus tent', 'Corporate Party', 'Crusader Army', 'Casino',
          'Day Spa', 'Embassy', 'Hospital', 'Hotel', 'Military Base', 'Movie Studio', 'Ocean Liner', 'Passenger Train',
          'Space Station', 'Restaurant', 'School', 'Service Station', 'Space Station', 'Submarine', 'Supermarket',
          'Theatre', 'University', 'World War II Squad', 'Race Track', 'Art Museum', 'Vineyard', 'Baseball Stadium', 'Library'
          'Cat Show', 'Retirement home', 'Jail', 'Construction site', 'The United Nations', 'Candy Factory', 'Subway', 'Coal mine'
          'Cemetry', 'Rock concert', 'Jazz club', 'Wedding', 'Gas station', 'Harbor docks', 'Sightseeing bus']
    async def start(self, ctx):
        self.state = True
        self.players.append(ctx.author)
        await ctx.send('<@%s> has started a game\nJoin with $join' % ctx.author.id)
    async def join(self, ctx):
        self.players.append(ctx.author)
        await ctx.send('<@%s> has joined the game' % ctx.author.id)
    async def play(self, ctx):
        self.state = False
        random.shuffle(self.players)
        await self.players[0].send("You are the spy")
        loc = random.choice(self.places)
        for p in self.players[1:]:
            await p.send("%s is the location" % loc)

