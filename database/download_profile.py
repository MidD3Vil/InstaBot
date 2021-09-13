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
import instaloader

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()


# BAIXAR FOTO PERFIL DO INSTAGRAM
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def start():
    clear()
    print('')
    print(f'\n{Iblue}########## ################## ##########')
    print('####### ### DOWNLOAD PROFILE ### #######')
    print('########## ################## ##########')
    restart = 'S'
    while restart == 'S':
        # Informações
        perfil = input(f'\n{Hcyan}Digite o nome do perfil que deseja \n[ respeite maiúsculas/números ] \n>>> ').strip()
    
        # Carrega a classe principal da lib #
        bot = instaloader.Instaloader()
    
        # Define perfil do Insta que deseja baixar os dados #
        username = f"{perfil}"
    
        # Baixa os dados do perfil do Insta #
        print('\n\033[1;33m{:-^62}'.format(f' {Dgreen}==> BAIXANDO PROFILE <=={Nyellow} '))
        print('')
        print(bot.download_profile(username, profile_pic_only=True))
        print('')
        print(f'\033[1;33m-' * 48)
        restart = str(input(
            f'\n{Hcyan}Deseja selecionar outra conta S/N?{VRCRM} ')).strip().upper()[0]
        clear()
