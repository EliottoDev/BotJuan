from discord.ext import commands
import json
import datetime

with open('data.json') as f, open('commands.json') as f1, open('games.json') as f2, open('partidas.json') as f3:
    data           = json.load(f)
    comandos       = json.load(f1)
    games          = json.load(f2)
    partidas       = json.load(f3)


AMONGUS = games[0]
GARTICPHONE = games[1]

bot = commands.Bot(command_prefix=data['prefix'])

"""
Función checkNumber, pasa texto a numero -> Devuelve lista
--------------------------------------------------------------------------
Argumentos de la lista:
    list[0] -> Numero convertido, en caso de no poder convertirse sera None
    list[1] -> Errores encontrados, en caso de no haber sera None
--------------------------------------------------------------------------
Argumentos de la funcion:
    :argument string -> Texto a pasar
"""
def checkNumber(string: str) -> list:
    error: Exception = None
    num: int = None

    try:
        num = int(string)
    except Exception as e:
        error = e

    return [num, error]

@bot.command(name='me')
async def me(ctx, arg):
    if not (arg in comandos):
        pass
    if not ("return" in comandos[arg]):
        pass

    await ctx.send(comandos[arg]['return'])


@bot.command(name='partida')
async def partida(ctx, juego: str, *args):

    if not(juego in games):
        await ctx.send('Debes introducir un juego permitido: amongus, garticphone')
        pass

    hora: datetime.datetime = datetime.datetime.strptime(args[0], '%H:%M')

    if juego == AMONGUS:
        impostors, error = checkNumber(args[1])
        if error != None


