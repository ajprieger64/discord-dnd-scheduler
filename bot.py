#!/bin/python3
import asyncio
import datetime
import sys
import zoneinfo
import discord
from discord.ext import commands, tasks
import secrets

TOKEN = secrets.DISCORD_TOKEN
GUILD_ID = secrets.DISCORD_GUILD

SCHEDULE_TIME = datetime.time(hour=16, tzinfo=zoneinfo.ZoneInfo('US/Central'))

# print((datetime.datetime.combine(datetime.date.today(), SCHEDULE_TIME) - datetime.datetime.now(datetime.UTC)).total_seconds())

def ordinal(n: int):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix

class ScheduleBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.send_scheduling_update.start()
        self.scheduling_channel = None

    async def on_ready(self):
        guild = discord.utils.get(self.guilds, id=GUILD_ID)

        print(f'{self.user} is connected to {guild.name}!')

        scheduling_channel = discord.utils.get(guild.channels, name='scheduling')

        print(f'Found channel with name {scheduling_channel}')

        self.scheduling_channel = scheduling_channel

    @tasks.loop(time=SCHEDULE_TIME)
    async def send_scheduling_update(self):
        today = datetime.date.today()
        if today.weekday() == 5: # If it's Saturday
            # Relative dating depends on it being Saturday - remember to change if you change the send day!
            next_friday = today + datetime.timedelta(days=13)
            next_saturday = today + datetime.timedelta(days=14)
            next_sunday = today + datetime.timedelta(days=15)
            print(f'Sending messages at time {datetime.datetime.now().astimezone(zoneinfo.ZoneInfo("US/Central")):%Y/%m/%d %H:%M:%S:%f %Z}')
            await self.scheduling_channel.send('@everyone New scheduling poll! (Note this is for two weeks from now.)')
            await self.scheduling_channel.send(f'Friday {next_friday.strftime("%B")} {ordinal(next_friday.day)} @7pm Eastern')
            await self.scheduling_channel.send(f'Saturday {next_saturday.strftime("%B")} {ordinal(next_saturday.day)} @9am Eastern')
            await self.scheduling_channel.send(f'Saturday {next_saturday.strftime("%B")} {ordinal(next_saturday.day)} @7pm Eastern')
            await self.scheduling_channel.send(f'Sunday {next_sunday.strftime("%B")} {ordinal(next_sunday.day)} @7pm Eastern')

async def main():
    intents = discord.Intents.default()
    async with ScheduleBot(command_prefix='!', intents=intents) as bot:

        # await bot.load_extension('cogs.schedule_cog')
        await bot.start(TOKEN)

asyncio.run(main())
