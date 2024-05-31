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

class ScheduleBot(commands.Bot):
    async def on_ready(self):
        guild = discord.utils.get(self.guilds, id=GUILD_ID)

        print(f'{self.user} is connected to {guild.name}!')

        scheduling_channel = discord.utils.get(guild.channels, name='scheduling')

        print(f'Found channel with name {scheduling_channel}')

        last_message = await scheduling_channel.fetch_message(scheduling_channel.last_message_id)

        print(last_message.content)

        await last_message.edit(content='Sunday April 21st @7pm Eastern')

async def main():
    intents = discord.Intents.default()
    async with ScheduleBot(command_prefix='!', intents=intents) as bot:
        await bot.start(TOKEN)

asyncio.run(main())
