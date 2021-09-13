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


# BAIXAR POSTS DO INSTAGRAM
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def start():
    clear()
    print('')
    print(f'\n{Iblue}########## ################## ##########')
    print('######## ### DOWNLOAD POSTS ### ########')
    print('########## ################## ##########')
    restart = 'S'
    while restart == 'S':
        # Informações
        perfil = input(f'\n{Hcyan}Digite o nome do perfil que deseja \n[ respeite maiúsculas/números ] \n>>> ').strip()

        # Carrega a lib e faz login com a conta desejada #
        print('Buscando...')
        L = instaloader.Instaloader()
        L.login('mid_insta_bot', 'mid_pass')

        # Carrega todos os posts do perfil escolhido #
        posts = instaloader.Profile.from_username(L.context, f"{perfil}").get_posts()

        # Percorre os posts e baixa todos #
        print('\n\033[1;33m{:-^62}'.format(f' {Dgreen}==> BAIXANDO POSTS <=={Nyellow} '))
        print('')
        for post in posts:
            print(f'Save {post.date} in "insta-posts-downloads"')
            L.download_post(post, "insta-posts-downloads")
        print('')
        print(f'\033[1;33m-' * 48)
        restart = str(input(
            f'\n{Hcyan}Deseja selecionar outra conta S/N?{VRCRM} ')).strip().upper()[0]
        clear()

# SINCE = datetime(2021, 1, 16)
