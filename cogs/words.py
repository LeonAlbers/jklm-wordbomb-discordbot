import discord
from discord.ext import commands

import random

from utils.search import find_words

MAX_WORD_AMOUNT = 20

class Words(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open("./data/wordlist-german.txt", encoding="utf-8") as f:
            self.wordlistAll = [line.strip() for line in f if line.strip()]
        with open("./data/bombparty-hyphen-german.txt", encoding="utf-8") as f:
            self.wordlistHyphen = [line.strip() for line in f if line.strip()]
        with open("./data/bombparty-longs-german.txt", encoding="utf-8") as f:
            self.wordlistLongs = [line.strip() for line in f if line.strip()]

    @commands.hybrid_command(name="find", aliases=["c", "search"], description="Find words containing a specific syllable.")
    async def find(self, ctx: commands.Context, syllable: str):
        results = find_words(self.wordlistAll, syllable)

        if not results:
            await ctx.send(f"❌ No words found containing the syllable '{syllable}'.")
            return
        
        if len(results) > MAX_WORD_AMOUNT:
            await ctx.send(f"✅ Found {len(results)} words containing the syllable '{syllable}'. Displaying 20 randomly:")
            results = random.sample(results, MAX_WORD_AMOUNT)
        else:
            await ctx.send(f"✅ Found {len(results)} words containing the syllable '{syllable}':")
        
        enumerated = [f"{i+1}. {w}" for i, w in enumerate(results)]
        await ctx.send("```" + "\n".join(enumerated) + "```")

    @commands.hybrid_command(name="long", aliases=["l"], description="Get a random long word.")
    async def long(self, ctx: commands.Context, syllable: str):
        results = find_words(self.wordlistLongs, syllable)

        if not results:
            await ctx.send(f"❌ No longs found containing the syllable '{syllable}'.")
            return
        
        if len(results) > MAX_WORD_AMOUNT:
            await ctx.send(f"✅ Found {len(results)} longs containing the syllable '{syllable}'. Displaying 20 randomly:")
            results = random.sample(results, MAX_WORD_AMOUNT)
        else:
            await ctx.send(f"✅ Found {len(results)} longs containing the syllable '{syllable}':")
        
        enumerated = [f"{i+1}. {w}" for i, w in enumerate(results)]
        await ctx.send("```" + "\n".join(enumerated) + "```")
        
    @commands.hybrid_command(name="hyphen", aliases=["h"], description="Get a random hyphenated word.")
    async def hyphen(self, ctx: commands.Context, syllable: str):
        results = find_words(self.wordlistHyphen, syllable)

        if not results:
            await ctx.send(f"❌ No hyphenated words found containing the syllable '{syllable}'.")
            return
        
        if len(results) > MAX_WORD_AMOUNT:
            await ctx.send(f"✅ Found {len(results)} hyphenated words containing the syllable '{syllable}'. Displaying 20 randomly:")
            results = random.sample(results, MAX_WORD_AMOUNT)
        else:
            await ctx.send(f"✅ Found {len(results)} hyphenated words containing the syllable '{syllable}':")
        
        enumerated = [f"{i+1}. {w}" for i, w in enumerate(results)]
        await ctx.send("```" + "\n".join(enumerated) + "```")

async def setup(bot):
    await bot.add_cog(Words(bot))