# Discord Multi-Tool Bot 🤖

## 📋 Sobre o Projeto
Este repositório contém um bot para o Discord desenvolvido em **Python** utilizando a biblioteca `discord.py`. O bot conta com sistemas automatizados de logs (mensagens, reações), monitoramento de membros e uma coleção de comandos utilitários, incluindo uma calculadora matemática segura que interpreta a árvore de sintaxe abstrata (`ast`).

## ⚙️ Funcionalidades principais

### 👁️ Sistema de Logs e Monitoramento (Eventos)
* **Log de Reações:** Registra em um canal privado quem reagiu, qual foi o emoji utilizado e em qual canal isso aconteceu.
* **Espelhamento de Conversas:** Envia uma cópia de todas as mensagens enviadas no servidor para um canal de administração privado.
* **Boas-vindas e Saídas:** Envia alertas automáticos em canais específicos quando um usuário entra ou sai do servidor.

### 🛠️ Comandos Disponíveis (Prefixo: `.`)
* `.ajuda` - Exibe a lista interativa de comandos.
* `.anomalia` - Retorna uma resposta aleatória e descontraída mencionando o usuário.
* `.apagar [quantidade]` - Limpa o chat (restrito a moderadores, limite de 100 mensagens).
* `.sorteio nome1, nome2, ...` - Realiza o sorteio de um nome a partir de uma lista separada por vírgulas.
* `.falar` - Saudação simples do bot.
* `.data` - Exibe a data e a hora atual em tempo real.
* `.calcular [expressão]` - Executa cálculos matemáticos básicos de forma totalmente segura.

---

## 🧠 Destaque Técnico: Calculadora Segura
Ao contrário de bots comuns que utilizam a função nativa `eval()` (o que gera graves vulnerabilidades de execução de código malicioso), este bot foi construído utilizando o módulo **`ast` (Abstract Syntax Tree)** do Python. 

O script analisa a estrutura do texto e a mapeia em nós matemáticos puros, permitindo apenas operações legítimas (`+`, `-`, `*`, `/`) e tratando erros como divisão por zero.

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o Python 3.8+ instalado e a biblioteca do Discord:

`pip install discord.py`

### 2. Configuração dos Canais
Antes de ligar o bot, você deve substituir os IDs numéricos dos canais (`bot.get_channel(ID)`) no código pelos IDs correspondentes aos canais do seu próprio servidor de Discord:
* Linhas de log de mensagens e reações.
* Linhas de entrada e saída de membros.

### 3. Inserindo o Token
No final do arquivo, insira o token do seu bot gerado no [Discord Developer Portal](https://discord.com/developers/applications):

`bot.run('SEU_TOKEN_AQUI')`

### 4. Inicialização
Execute o arquivo principal:

`python seu_arquivo.py`

## 🤝 Contribuições
Sinta-se à vontade para clonar, abrir issues ou enviar pull requests com novos comandos e melhorias!
