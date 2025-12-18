import discord
from discord.ui import View as view
from discord.ui import Button

class Pages(view):
    def __init__(self, pages: list[str]):
        super().__init__(timeout=120)
        self.pages = pages
        self.current_page = 0
        self.message = None

        self.previous = Button(label="◀️", style=discord.ButtonStyle.blurple)
        self.first = Button(label="🏠", style=discord.ButtonStyle.blurple)
        self.next = Button(label="▶️", style=discord.ButtonStyle.blurple)

        self.previous.callback = self.go_prev
        self.first.callback = self.go_first
        self.next.callback = self.go_next

        self.add_item(self.previous)
        self.add_item(self.first)
        self.add_item(self.next)

    async def on_timeout(self):
        if self.message:
            await self.message.edit(view=None)
    
    async def send(self, ctx):
        self.message = await ctx.send(embed=self.pages[0], view=self)

    async def update(self, interaction):
        embed = self.pages[self.current_page]
        await interaction.response.edit_message(embed=embed, view=self)

    async def go_first(self, interaction):
        self.current_page = 0
        await self.update(interaction)

    async def go_prev(self, interaction):
        self.current_page = max(0, self.current_page - 1)
        await self.update(interaction)

    async def go_next(self, interaction):
        self.current_page = min(len(self.pages)-1, self.current_page + 1)
        await self.update(interaction)