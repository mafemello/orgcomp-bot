# orgcomp-bot

## Organização dos arquivos:
- bot_server.py
  - Inicializa o servidor e instancia Bot().
  - Escuta mensagens, verifica se elas são comandos e fazem com que Bot() as executem se forem.
- bot.py
  - Define a classe do Bot(), que herda a classe Commands() e Users()
  - Bot() executa as funções lidadas por Commands()
- commands.py
  - Guarda os dicionários de relação 'comando':'função' para despoluir Bot()
  - Guarda MENU, o dicionário com todos os comandos
    - MENU é a junção de HELP_MENU, TEORIA_MENU e QUIZZ_MENU
- users.py
  - Cria um banco de usuários na Stack, evitando que as respostas do quizz de um usuário interfiram no do outro
  - É dinâmico: Se o servidor morrer, as informações são perdidas.
## Instruções: 

### Primeira Instalação:
```
pip install virtualenv                  # Instala biblioteca de venvs
virtualenv -p $(which python3)          # Cria a venv
source env/bin/activate # Entra na venv # Entra na venv
pip install -r requirements.txt         # Instala dependencias na venv
```
### Rodar o programa
Após entrar na venv:
```
python bot_server.py
```
### Se precisar entrar / sair da venv:
```
source env/bin/activate                 #entra na venv
deactivate                              #sai da venv
```

- Só é preciso usar pip install uma vez
- É preciso estar na venv para rodar o projeto
- Uma vez dentro da venv, pode-se rodar o projeto quantas vezes quiser
- É necessário rodar o programa a cada atualização para testá-lo
- Testar em https://web.telegram.org/#/im?p=@orgcomp_bot