import discord
from discord.ext import commands
from datetime import datetime
import ast
import operator
import random

OPERADORES = {             # operadores matematico 
     ast.Add: operator.add,
     ast.Sub: operator.sub,
     ast.Mult: operator.mul,
     ast.Div: operator.truediv,
     ast.USub: operator.neg,
}

intents = discord.Intents.all()
bot = commands.Bot('.', intents=intents)



@bot.event       #evento de disparação do bot (inicialização) 1
async def on_ready():
    print('estou funcionando chefe')


@bot.event 
async def on_reaction_add(reacao: discord.Reaction, membro: discord.Member):
    canal_privado = bot.get_channel(1381058585571885216)  # canal de log privado
    mensagem = reacao.message  # mensagem que recebeu a reação

    await canal_privado.send(
    f'{membro.name} reagiu com {reacao.emoji} na mensagem no canal #{mensagem.channel.name}'
    )


@bot.event         #evento de verificação de menssagem do usuario 2
async def on_message(msg:discord.Message):
    if msg.author.bot:
        return  #verificação se a menssagem vem de algum bot (se for de bot o 'return' cancela)
    
    canal = bot.get_channel(1381058585571885216) # mostra a menssagem que eu mandei em um canal privado
    await canal.send(f'{msg.author} falou no canal {msg.channel.name}: {msg.content}')
    await bot.process_commands(msg)


@bot.event  # aviso de membro novo 3
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(1381062135823728701)
    await canal.send(f'{membro.mention} entrou no serve')


@bot.event
async def on_member_remove(membro:discord.Member): #evento que aciona qua do um membro sai
    canal = bot.get_channel(1381094314846851144)  #canal expecifico, para ir a menssagem que o mebro saiu
    await canal.send(f'{membro.mention} la se vai mais um membro...  ')  #menciona o membro que saiu, aviso o serv no canal expecifico

@bot.command()
async def anomalia(ctx:commands.Context): # aqui pega o nome do usuario que chamou
    nome = ctx.author.name
    respostas = [      #respsota que a gente escolheu, cada resposta vai ir com nome do usuario
        f'já bebeu agua hoje {nome}? caso não, va beber agua.',
        f'está me chamando pra que {nome}?',
        f'ja fez um calculo na minha calculadora ? caso não, coloca ai .calculadora',
        f'{nome}, já olhou que dia e hoje ? da uma olhada ai .data',
        f' estou com preguiça de falar com voce, por favor não tente novamente',
        f'ainda estou em desenvolvimento, meu criador mal mal sabe da um input :)',
        f'{nome}, me fala ai, mais quias funçoes eu deveria ter ?',
    ]   
    respostas = random.choice(respostas) # radom pra escolher uma resposta
    await ctx.reply(respostas) #envia a resposta es
    
@bot.command()    #APAGAOR DE MENSSAGEM
async def apagar(ctx, quantidade: int = 10):
    if not ctx.author.guild_permissions.manage_messages:
        return await ctx.reply("Você não tem permissão para apagar mensagens.")

    if quantidade > 100:
        return await ctx.reply("Não é possível apagar mais de 100 mensagens de uma vez.")

    if quantidade <= 0:
        return await ctx.reply("Informe um número positivo.")

    deletadas = await ctx.channel.purge(limit=quantidade + 1)  # +1 para incluir o comando

    await ctx.send(f"{len(deletadas) - 1} mensagens foram apagadas por {ctx.author.name}.", delete_after=5)


@bot.command()
async def sorteio(ctx: commands.Context, *, nomes):
    vetor = [nome.strip() for nome in nomes.split(',') if nome.strip()]

    if len(vetor) <2:
     await ctx.reply('Informe ao menos um nome separado por vírgula, exemplo: .sorteio breno, pedro, renzo, valeria')
     return

    matriz = [vetor[i:i+2] for i in range(0, len(vetor), 2)]

    escolhido = random.choice(vetor)
    await ctx.reply(f'Lista:\n{matriz}\n\nPessoa sorteada: {escolhido}')


@bot.command()
async def ajuda(ctx):
    comandos = """
    **Comandos disponíveis:**
    `.anomalia` - Resposta aleatória engraçada
    `.apagar [número]` - Apaga mensagens
    `.sorteio nome1, nome2,...` - Faz um sorteio
    `.falar` - Saudação
    `.data` - Mostra a data e hora
    `.calcular expressão` - Calculadora
    """
    await ctx.reply(comandos)


@bot.command()
async def falar(ctx:commands.Context):
    nome = ctx.author.name 
    await ctx.reply(f'ola tudo bem, {nome}, vamos começar?')


@bot.command()
async def data(ctx:commands.Context):
    agora = datetime.now()
    data_formatada = agora.strftime('%d/%m/%Y %H:%M:%S')
    await ctx.reply(f'A data e hora atual é: {data_formatada}')
    await ctx.reply (f'{ctx.author}. e isso ai meu nobre.')


def avaliar (node):

    if isinstance(node, ast.Expression):
     return avaliar(node.body)
    elif isinstance(node, ast.Num):  # número puro
        return node.n
    elif isinstance(node, ast.BinOp):  # operação binária
        return OPERADORES[type(node.op)](avaliar(node.left), avaliar(node.right))
    elif isinstance(node, ast.UnaryOp):  # -n
        return OPERADORES[type(node.op)](avaliar(node.operand))
    else:
        raise TypeError('expressão invalida')


@bot.command()
async def calcular(ctx:commands.Context, *, expressao ): #calculadora
    try:
       expressao = expressao.replace(',', '.')

       node = ast.parse(expressao, mode='eval')
       resultado = avaliar(node.body)
       await ctx.reply(f'resultado: {resultado}')
    except ZeroDivisionError:
        await ctx.reply('Erro: divisão por zero.')
    except Exception as e:
        await ctx.reply(f'Erro ao calcular: {e}')
        
@calcular.error
async def calcular_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('Por favor, informe a expressão para calcular.\nExemplo: .calcular 10+5')
    else:
        await ctx.reply(f'Ocorreu um erro inesperado: {error}')  

bot.run('')  # token do bot, sempre em ultimo para ler todo o codigo quando iniciar