# Discord Multi-Tool Bot

Bot de estudos feito em Python com `discord.py`. Reúne comandos simples, avisos de entrada e saída de membros, logs de reações e uma calculadora com avaliação aritmética limitada.

## Funcionalidades

- `.ajuda` — mostra os comandos disponíveis.
- `.anomalia` — responde com uma frase aleatória.
- `.apagar [quantidade]` — apaga até 100 mensagens; exige a permissão `Manage Messages`.
- `.sorteio nome1, nome2, ...` — sorteia um nome da lista.
- `.falar` — envia uma saudação.
- `.data` — mostra data e hora locais do processo.
- `.calcular expressão` — calcula usando `+`, `-`, `*`, `/`, parênteses e sinal unário.

O bot também registra reações, mensagens e eventos de entrada e saída nos canais configurados no código.

## Requisitos

- Python 3.8 ou superior
- `discord.py`
- Uma aplicação e um bot criados no [Discord Developer Portal](https://discord.com/developers/applications)

Instale a dependência:

```bash
python -m pip install discord.py
```

## Configuração

1. No Discord Developer Portal, habilite **Message Content Intent** e **Server Members Intent** para o bot. Esses intents são usados pelos comandos com prefixo, leitura de mensagens e avisos de entrada e saída.
2. Substitua no arquivo `bot discord.py` os IDs de canal pelos IDs do seu servidor.
3. Defina o token em uma variável de ambiente antes de iniciar. Não coloque o token no código nem em commits.

No PowerShell:

```powershell
$env:DISCORD_BOT_TOKEN = "seu-token-do-bot"
python ".\bot discord.py"
```

No macOS ou Linux:

```bash
export DISCORD_BOT_TOKEN="seu-token-do-bot"
python "bot discord.py"
```

Se a variável não estiver definida, o bot encerra com uma orientação de configuração.

## Logs e privacidade

O evento `on_message` encaminha o conteúdo de todas as mensagens recebidas para o canal de log configurado, e as reações também são registradas. Avise os membros antes de ativar esse comportamento, limite o acesso ao canal de log e defina uma política adequada de retenção. Revise ou remova esses eventos se o registro integral não for necessário para o seu servidor.

## Calculadora

A calculadora interpreta a expressão com a árvore sintática do Python, sem usar `eval`. Aceita somente números e operações aritméticas básicas. Para limitar consumo de recursos, restringe a expressão a 200 caracteres, 64 nós de sintaxe, 20 níveis de aninhamento e resultados com módulo de até `10^100`. Vírgula decimal também é aceita.

## Testes

Os testes da calculadora usam apenas a biblioteca padrão do Python:

```bash
python -m unittest discover -s tests -v
```
