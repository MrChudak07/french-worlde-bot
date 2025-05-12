import discord
import os 
import random 
import config
from discord.ext import commands
import json

token = config.TOKEN 
if not token:
    print("Error: No token found. Please check the Secrets tab!")
    exit()
    

# Data
word_list = config.word_list
word_list_test = ['tests']
guesses_list = config.guesses_list
players = config.players['players']

# Setting bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='w!', help_command=None)
# client = discord.Client(intents=intents)







# Test command to check embed
@bot.command()
async def com(ctx):
    # print(dir(ctx.author))
    id = str(ctx.author.id)
    msg = players[id]['word']
    await ctx.send(msg)
#     embed = discord.Embed(
#     title=f"{ctx.author.global_name}'s game",
#     description=f'''Attempt No: x/8

# {config.emojis_letters['y']['black']}{config.emojis_letters['y']['black']}{config.emojis_letters['y']['black']}{config.emojis_letters['y']['black']}{config.emojis_letters['y']['black']} 

# -# Enter `w!stop` to give up.''',
#     color=discord.Color.blue(),
    
# )

    # embed.set_author(name=f"{ctx.author}", url="https://example.com", icon_url="https://example.com/icon.png")
    # embed.set_footer(text="Футер эмбеда", icon_url="https://example.com/footer_icon.png")
    # embed.set_thumbnail(url="https://example.com/thumbnail.png")
    # embed.set_image(url="https://example.com/image.png")

    # embed.add_field(name="Поле 1", value="Значение поля 1", inline=False)
    # embed.add_field(name="Поле 2", value="Значение поля 2", inline=True)
    # embed.add_field(name="Поле 3", value="Значение поля 3", inline=True)
    # embed.add_field(name="Поле 4", value="Значение поля 4", inline=False)  # Пустое поле для отступа

    # Отправка embed в контексте команды


#* When ready
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

#* When see a message
@bot.event
async def on_message(message):
    id = str(message.author.id)
    content = message.content.lower()

    #* MESSAGE IS COMMAND
    if message.author == bot.user or 'w!' in content :
        await bot.process_commands(message)
        return


    #* MESSAGE IS ANSWER
    if id in players and message.channel.id == players[id]['channel'] and players[id]['game']:
        if len(content.split()) > 1:
            return

        #* WRONG LENGTH
        elif len(content) != 5:
            msg = f'<@{message.author.id}>{config.msg_wrong_letters} {players[id]['length']}'
            await message.channel.send(msg)

        #* WRONG WORD
        elif content not in guesses_list:
            await message.channel.send('next one')


        #* GAMEPLAY
        else:
            guess = message.content.lower()
            players[id]['attempts']+=1
            ans = list(players[id]['word'])
            players[id]['guesses'].append([])
            correct_letters = []
            for letter in guess:
                if letter in ans:
                    correct_letters.append(letter)
                    ans.remove(letter)

                
            for i in range(5):

                if guess[i] in correct_letters:

                    if guess[i] == players[id]['word'][i]:
                        players[id]['guesses'][-1].append(config.emojis_letters[guess[i]]['green'])
                        correct_letters.remove(guess[i])

                    else:
                        players[id]['guesses'][-1].append(config.emojis_letters[guess[i]]['black'])

                else:
                    players[id]['guesses'][-1].append(config.emojis_letters[guess[i]]['black'])


            for i in range(5):

                if guess[i] in correct_letters:
                    players[id]['guesses'][-1][i] = config.emojis_letters[guess[i]]['yellow']
                    correct_letters.remove(guess[i])
                else: 
                    if players[id]['guesses'][-1][i] != config.emojis_letters[guess[i]]['green']:
                        players[id]['guesses'][-1][i] = config.emojis_letters[guess[i]]['black']


            players[id]['guesses'][-1].append('\n')
            guesses = '' 
            for g in players[id]['guesses']:

                guesses += ''.join(g)
            
            msg = f'''Attempt No: {players[id]['attempts']}/8

{guesses}

'''         
            if players[id]['attempts'] < 8 and guess != players[id]['word'] and '#' not in guess:
                embed = discord.Embed(
                title=f"{message.author}'s game",
                description=f"{msg}",
                color=discord.Color.blue(),
                )
                embed.set_footer(text="Type `w!stop` to give up | type `w!alphabet` to watch available letters.")

                await message.channel.send(embed = embed)


            #* WIN 
            if guess == players[id]['word'] or content == '#0002':
                msg = f'''Congrats, you find the word in **{players[id]['attempts']}** tries!

{guesses}

                '''

                players[id]['game'] = False
                players[id]['current_streak'] += 1
                players[id]['max_streak'] = max(players[id]['max_streak'], players[id]['current_streak'])
                players[id]['wins'] += 1
                players[id]['total_games'] += 1
                players[id]['win_rate'] = round(players[id]['wins']/players[id]['total_games'], 4)
                players[id]['word'] = ''
                players[id]['guesses'] = []
                
                # Save chaanging
                with open('dataBase.json', 'w', encoding='utf-8') as file:
                    json.dump({"players":players}, file, indent=8)


                embed = discord.Embed(
                title=f"{message.author}'s game",
                description=f"{msg}",
                color=discord.Color.green(),
                )
                embed.set_footer(text="Type `w!play` to start new game.")

                await message.channel.send(embed = embed)
                # await message.channel.send(msg )


            #* DEFEAT
            elif players[id]['attempts'] == 8 or content== '#0001':
                msg = f'''You lost. The word was **{players[id]['word']}**

{guesses}
 '''
                
                players[id]['game'] = False
                players[id]['current_streak'] = 0
                players[id]['total_games'] += 1
                players[id]['win_rate'] = round(players[id]['wins']/players[id]['total_games'], 4)
                players[id]['word'] = ''
                players[id]['guesses'] = []

                # Save chaanging
                with open('dataBase.json', 'w', encoding='utf-8') as file:
                    json.dump({"players":players}, file, indent=8)

                embed = discord.Embed(
                title=f"{message.author}'s game",
                description=f'''{msg}''',
                color=discord.Color.red(),
                
            )
                embed.set_footer(text="Type `w!play` to start new game.")
                await message.channel.send(embed=embed)


            #     embed.set_author(name=f"{id}", url="https://example.com", icon_url="https://example.com/icon.png")
            #     embed.set_footer(text="Футер эмбеда", icon_url="https://example.com/footer_icon.png")
            #     embed.set_thumbnail(url="https://example.com/thumbnail.png")
            #     embed.set_image(url="https://example.com/image.png")

            #     embed.add_field(name="Поле 1", value="Значение поля 1", inline=False)
            #     embed.add_field(name="Поле 2", value="Значение поля 2", inline=True)
            #     embed.add_field(name="Поле 3", value="Значение поля 3", inline=True)
            #     embed.add_field(name="Поле 4", value="Значение поля 4", inline=False)  # Пустое поле для отступа

            #     # Отправка embed в контексте команды
            #     await message.channel.send(embed=embed)
        



#* HELP command
@bot.command()
async def help(ctx):
    id = str(ctx.author.id)
    content = ctx.message.content
    msg = config.msg_help
    embed = discord.Embed(
        title="Available commands",
        description=f"{msg}",
        color=discord.Color.blue(),
        )
    await ctx.send(embed=embed)


#* ALPHABET command
@bot.command()
async def alphabet(ctx):
    msg = config.msg_alphabet
    embed = discord.Embed(
        title="Available letters",
        description=f"```{msg}```",
        color=discord.Color.blue(),
        )
    await ctx.send(embed=embed)


#* PLAY command
@bot.command()
async def play(ctx):
    id = str(ctx.author.id)
    content = ctx.message.content
    try:
        #* IF user in database and game wasn't started before
        if not players[id]['game']:

            players[id]['game'] = True
            players[id]['attempts'] = 0
            players[id]['word'] = random.choice(word_list)
            players[id]['channel'] = ctx.channel.id
            players[id]['guesses'] = []

            msg = f"Starting <@{id}>'s game with **5** letters, type your first guess!"
            await ctx.send(msg)
            # embed = discord.Embed(
            # title="Заголовок эмбеда",
            # description=f"starting <@{id}>'s game with **5** letters, type your first guess!",
            # color=discord.Color.blue(),
            
            # )
            # await ctx.send(embed=embed)







        #* Game was started before
        else:
            msg = f'Your game already started in the <#{players[id]['channel']}>. Type "w!stop" and then "w!play" to start a new game or continue the current one.'
            await ctx.send(msg)


    except:
        #* IF user is NOT in database
        players[id] = {'attempts': 0,
                            'word': random.choice(word_list),
                            'channel': ctx.channel.id,
                            'guesses': [],
                            'length': 5,
                            'game': True,
                            'total_games': 0,
                            'wins': 0,
                            'win_rate': 0,
                            'current_streak': 0,
                            'max_streak': 0, 
                            'list_of_attempts' : []
                            }
        msg = f"Starting <@{id}>'s game with **5** letters, type your first guess!"
        await ctx.send(msg)
        # embed = discord.Embed(
        # title="Заголовок эмбеда",
        # description=f"starting <@{id}>'s game with **5** letters, type your first guess!",
        # color=discord.Color.blue(),
        
        # )
        # await ctx.send(embed=embed)


#* STOP command
@bot.command()
async def stop(ctx):
    id = str(ctx.author.id)
    content = ctx.message.content
    try:
        #* IF user has active game
        if players[id]['game']:
                guesses = ''
                for guess in  players[id]['guesses']:
                    guesses+= ''.join(guess)
                msg = f'''The current game has stopped. The word was **{players[id]['word']}**

{guesses}
'''
            
                players[id]['game'] = False
                players[id]['current_streak'] = 0
                players[id]['total_games'] += 1
                players[id]['word'] = ''
                players[id]['guesses'] = []

                # msg = f'<@{id}>\'s game has stopped. The word was {word}.'
                with open('dataBase.json', 'w', encoding='utf-8') as file:
                    json.dump({"players":players}, file, indent=8)

                embed = discord.Embed(
                title=f"{ctx.author.global_name}'s game",
                description=msg,
                color=discord.Color.lighter_gray())

                embed.set_footer(text="Type `w!play` to start new game.")

                await ctx.send(embed = embed)


        else:
            #* IF user do NOT have active game
            msg = 'You don\'t have any active games. Type `w!play` to start new game.'
            await ctx.send(msg)


    except:
        msg = 'You don\'t have any active games. Type `w!play` to start new game. error'
        await ctx.send(msg)
        


@bot.command()
async def stats(ctx):
    id = str(ctx.author.id)
    content = ctx.message.content
    try:
        
        embed = discord.Embed(
        title=f"STATISTICS",

        color=discord.Color.blue(),)
        # embed.set_thumbnail(url=ctx.author.avatar.url)

        embed.set_author(name=f"{ctx.author.global_name}", icon_url=ctx.author.avatar.url)
        # embed.set_footer(text="Футер эмбеда", icon_url="https://example.com/footer_icon.png")
        # embed.set_image(url=ctx.author.avatar.url)

        embed.add_field(name="Games", value=f'**{players[id]['total_games']}**', inline=True)
        embed.add_field(name="Wins", value=f'**{players[id]['wins']}**', inline=True)
        embed.add_field(name="Win %", value=f'**{players[id]['win_rate']*100} %**', inline=True)
        embed.add_field(name="Max streak", value=f'**{players[id]['max_streak']}**', inline=True)
        embed.add_field(name='Streak', value=f'**{players[id]['current_streak']}**', inline=True )  # Пустое поле для отступа
        await ctx.send(embed=embed )

    except:
        embed = discord.Embed(
            description=f'<@{id}>, you\'ve never played before. Enter `w!play` to start your first game!',
            color= discord.Color.blue()
        )
        await ctx.send(embed = embed)


@bot.command()
async def reset(ctx, accepted:str ='no'):
    id = str(ctx.author.id)
    content = ctx.message.content
    if accepted == 'yes':

        players[id] = {'attempts': 0,
                            'word': '',
                            'channel': ctx.channel.id,
                            'guesses': [],
                            'length': 5,
                            'game': False,
                            'total_games': 0,
                            'wins': 0,
                            'win_rate': 0,
                            'current_streak': 0,
                            'max_streak': 0, 
                            'list_of_attempts' : []
                            }
        
        with open('dataBase.json', 'w', encoding='utf-8') as file:
                    json.dump({"players":players}, file, indent=8)
        
        msg = f'<@{id}>\'s score has been reseted. Now your stats are:'
        await ctx.send(msg)
        await stats(ctx)
        
    else:
        await ctx.send('Type `w!reset yes` to confirm resetting your score!')


@bot.command()
async def rules(ctx):
    msg = config.msg_rules
    embed = discord.Embed(
        title=f"The rules of the French Wordle",
        description=f'''{msg}''',
        color=discord.Color.blue(),)
    await ctx.send(embed = embed)




#* Starting
try:
    token = config.TOKEN or ""
    if token == "":
        raise Exception("Please add your token to the Secrets pane.")
    bot.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e
    