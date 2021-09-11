## Tabela de cores ANSI (Python) ##

# fonte #
Mblack = '\033[1;30m'   # Preto
Ired = '\033[1;31m'     # Vermelho
Dgreen = '\033[1;32m'   # Verde
Nyellow = '\033[1;33m'  # Amarelo
Iblue = '\033[1;34m'    # Azul
Gpurple = '\033[1;35m'  # Roxo
Hcyan = '\033[1;36m'    # Ciano
Twhite = '\033[1;37m'   # Branco
VRCRM = '\033[0;0m'     # Remover

import os
import instaloader

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

# LISTANDO SEGUIDORES INSTAGRAM
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def consultar():
    clear()
    print('')
    print(f'\n{Iblue}########## ################### ##########')
    print('######## ### INFO SEGUIDORES ### ########')
    print('########## ################### ##########')
    restart = 'S'
    while restart == 'S':
        # Informações #
        perfil = input(f'\n{Hcyan}Digite o nome do perfil que deseja \n[ respeite maiúsculas/números ] \n>>> ').strip()
    
        # Carrega a lib e faz login com a conta desejada #
        print('Buscando...')
        L = instaloader.Instaloader()
        L.login('mid_insta_bot', 'mid_pass')
    
        # Carrega os dados dos seguidores e seguindo do perfil escolhido #
        followers = instaloader.Profile.from_username(L.context, f'{perfil}').get_followers()
        followees = instaloader.Profile.from_username(L.context, f'{perfil}').get_followees()
    
        # Mostra resultados #
        print('\n\033[1;33m{:-^62}'.format(f' {Dgreen}==> PERFIL ENCONTRADO <=={Nyellow} '))
        print('\nSeguidores: ' + str(followers._data['count']))
        print('Seguindo: ' + str(followees._data['count']))
        print('\nLista e informações de seguidores:\n')
        print(followers._data['edges'])
        print('')
        print(f'\033[1;33m-' * 48)
        restart = str(input(
            f'\n{Hcyan}Deseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[
            0]
        clear()
