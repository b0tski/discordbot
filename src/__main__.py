import discord 
import src
import asyncio
from src import constants
from discord.ext.commands import Bot


async def main():
    intents = discord.Intents.all()
    
    src.instance = Bot(
        command_prefix= "<", 
        activity=discord.Game(name=f"heheheha"),
        case_insensitive=True,
        max_messages=10_000,
        allowed_mentions=discord.AllowedMentions(everyone=False),
        intents=intents,
    )
    
    async with src.instance as _bot:
        await _bot.start(constants.data["token"], reconnect=True)
        
        
if __name__ == '__main__':
    asyncio.run(main())
