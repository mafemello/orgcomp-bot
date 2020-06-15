# orgcomp-bot

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
python bot.py
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