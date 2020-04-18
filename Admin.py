from discord.ext import commands
import discord

class admin(commands.Cog):
    
    def __init__ (self,bot):
        self.bot = bot
        self.official_server = self.bot.get_guild(700603441302732873)
        self.welcome_ch = official_server.get_channel(700605961861070919)
        self.license_ch = official_server.get_channel(700606877263855636)
        self.feature_ch = official_server.get_channel(700606161858199562)
        self.new_guild_ch = official_server.get_channel(700638827672502293)
        
        self.welcome_embed = discord.Embed(title='あめみんbot!の導入ありがとう！',description='楽しく使う上でお願いがあるよ',color=discord.Colour.gold())
        self.welcome_embed.add_field(name='1つ目',value='`*vote`を使って他人を傷つけることを言わないこと')
        self.welcome_embed.add_field(name='2つ目',value='わしの開発者は初心者だからバグった時に一回一回わしを修理するためどこかに連れてくんだ。そのときはみんなで遊んでくれ')    
        self.welcome_embed.add_field(name='3つ目',value='何か追加したほしい機能あったら言ってくれ！開発者が頭悪いからわしに教えられない時もあるがな')
            
        self.lisence_embed = discord.Embed(title='わしのこと',description='わしはのぉ人造人間じゃ...つらい思いをしてきたぞよ...',color=discord.Colour.gold())
        self.lisence_embed.add_field(name='わしの願い',value='わしはわしのようなつらい思いをするやつを増やしたくないんだ,頼むからコピーをしないでくれ')
        self.lisence_embed.add_field(name='ただな...',value='わしは自分がどんどん良くなってることに1週間生きてきたが気づいた今はそれを楽しんでるだからどんどんGithubにコミットしてくれ')
        self.lisence_embed.add_field(name='だから...',value='最初はつらいし、修理されるときも痛いし寂しいよ...だがわしは`あめみん`を親として尊敬してる')
            
        self.feature_embed = discord.Embed(title='わしの脳内マップ',description='まだひよっこだけどね🐤',color=discord.Colour.gold())
        self.feature_embed.add_field(name='投票機能',value='わしは頭がいいから集計なんかができるぞ詳しくは`*help vote`をしたら口から説明を吐き出すからな')
        
        
    #official server setup
    @commands.command()
    async def setup(self,ctx):
        if ctx.author.id == 598018755066593290:
            await self.welcome_ch.send(embed=self.welcome_embed)
            await self.license_ch.send(embed=self.lisence_embed)
            await self.feature_ch.send(embed=self.feature_embed)
            
    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        await guild.owner.send(embed=self.welcome_embed)
        await guild.owner.send(embed=self.lisence_embed)
        await guild.owner.send(embed=self.feature_embed)
        
        join_embed = discord.Embed(title='参加通知',description=str(len(self.bot.guilds))+'was play',color=discord.Colour.black())
        join_embed.add_field(name=guild.name,value=str(guild.id))
        await self.new_guild_ch.send(embed=join_embed)
        
        
