import discord
from discord.ext import commands
from utils.pages import Pages

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="help", description="Show this help message.")
    async def help(self, ctx):
        pages = []
        COMMANDS_PER_PAGE = 5
        commands_list = self.bot.tree.get_commands()

        for i in range(0, len(commands_list), COMMANDS_PER_PAGE):
            embed = discord.Embed(title="Help - Command List", color=discord.Color.blurple())
            for cmd in commands_list[i:i + COMMANDS_PER_PAGE]:
                embed.add_field(name=f"/{cmd.name}", value=cmd.description, inline=False)
            pages.append(embed)

        view = Pages(pages)
        await ctx.send(embed=pages[0], view=view)

async def setup(bot):
    await bot.add_cog(Help(bot))