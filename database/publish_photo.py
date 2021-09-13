## Tabela de cores ANSI (Python) ##

# fonte #
Mblack = '\033[1;30m'  # Preto
Ired = '\033[1;31m'  # Vermelho
Dgreen = '\033[1;32m'  # Verde
Nyellow = '\033[1;33m'  # Amarelo
Iblue = '\033[1;34m'  # Azul
Gpurple = '\033[1;35m'  # Roxo
Hcyan = '\033[1;36m'  # Ciano
Twhite = '\033[1;37m'  # Branco
VRCRM = '\033[0;0m'  # Remover

import os
from instabot import Bot


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()


# PUBLICAR FOTO INSTAGRAM
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--

def start():
    clear()
    print('')
    print(f'\n{Iblue}########## ################### ##########')
    print('######### ### PUBLICAR FOTO ### #########')
    print('########## ################### ##########')
    restart = 'S'
    while restart == 'S':
        # Informações
        bot = Bot()
        user = input('Digite seu user do instagram: ')
        passw = input('Digite sua senha do instagram: ')
    
        # Seu usuário e senha do instagram
        clear()
        print('\nLogando... Aguarde')
        bot.login(username=f'{user}', password=f'{passw}')
        clear()
    
        # Post
        clear()
        print('Login realizado!\n')
        foto = input('Digite o nome da foto [Ex: foto.jpg]: ')
        legenda = input('Digite a legenda para a foto: ')
    
        # Upload de imagem e legenda da sua publicação
        print('\n\033[1;33m{:-^62}'.format(f' {Dgreen}==> FOTO PUBLICADA <=={Nyellow} '))
        bot.upload_photo(f'{foto}', caption=f'{legenda}')
        print('')
        print(f'\033[1;33m-' * 48)
        restart = str(input(
            f'\n{Hcyan}Deseja postar outra foto S/N?{VRCRM} ')).strip().upper()[
            0]
        clear()
    
# Digite seu user do instagram: mid_insta_bot
# Digite sua senha do instagram: mid_pass

