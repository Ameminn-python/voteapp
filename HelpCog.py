import discord
from discord.ext import commands

class helpcommands(commands.Cog):
    def __init__(self):
        pass
    
    @commands.command()
    async def help(self,ctx,feature=None):
        if feature is None:
            help_feature = discord.Embed(title='Help commands help :D',description='*help <**feature**>',colour=discord.Colour.orange())
            help_feature.add_field(name='**vote**',value='Vote feature help use this *help vote',inline=False)
            help_feature.add_field(name='**general**',value="this bot's general cmd help",inline=False)
            await ctx.send(embed=help_feature)
        elif feature == 'vote':
            help_vote = discord.Embed(title='Vote Help',description='if you want check other feature pls Type *help',colour=discord.Colour.orange())
            help_vote.add_field(name='① *vote <question> ',value='Disignation question',inline=False)
            help_vote.add_field(name='② *asr <asr1>/<asr2>',value='Disignation answer (split**/**)※Max4answer',inline=False)
            help_vote.add_field(name='③ *fin',value='finish questionnaire',inline=False)
            await ctx.send(embed=help_vote)
        elif feature == 'general':
            help_general = discord.Embed(title='General Help',description='this bot general command',colour=discord.Colour.orange())
            help_general.add_field(name='*code*',value='if you use this command, you can get source code',inline=False)
            help_general.add_field(name='*invite*',value='return this bot invite URL',inline=False)
            await ctx.send(embed=help_general)
        else:
            await ctx.send('can not found this feature pls chack *help .')
                                         
                                         
                                      
    
