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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear()
    (fr'''{Ired}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░┛
    ░░┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ ░░░░░░░░░░{Hcyan}▄▄▄▄▄▄▄{Ired}░░░░░░░░░░                    
    ░░┃         {Nyellow}[{Twhite} STALKER INSTAGRAM{Nyellow} ]{Ired}         ┃ ░░░░░░{Hcyan}▄▄▀▀{Ired}░░░░░░░{Hcyan}▀▀▄▄{Ired}░░░░░░
    ░░┃                                       ┃ ░░░░{Hcyan}▄▀{Ired}░░░░░░░░░░░░░░░{Hcyan}▀▄{Ired}░░░░
    ░░┣┫{Nyellow}[01]{Twhite} BAIXAR FOTO PERFIL DO INSTAGRAM{Ired}  ┃ ░░░{Hcyan}▄▀{Ired}░░░{Hcyan}▄▄▄▄▄▄▄▄▄▄▄{Ired}░░░░{Hcyan}█{Ired}░░░
    ░░┃                                       ┃ ░░{Hcyan}█{Ired}░░{Hcyan}▄███████████████▄{Ired}░░{Hcyan}█{Ired}░░
    ░░┣┫{Nyellow}[02]{Twhite} EXPLORANDO PERFIS DO INSTAGRAM{Ired}   ┃ ░{Hcyan}█{Ired}░░{Hcyan}▄██▀{Ired}░{Hcyan}▄▄▀███▀▄▄{Ired}░{Hcyan}▀███{Ired}░░{Hcyan}█{Ired}░
    ░░┃                                       ┃ ░{Hcyan}█{Ired}░░{Hcyan}▀█████████████████▀{Ired}░░{Hcyan}█{Ired}░
    ░░┣┫{Nyellow}[03]{Twhite} LISTANDO SEGUIDORES INSTAGRAM{Ired}    ┃ ░{Hcyan}█{Ired}░░░░{Hcyan}▀▀████████████▀{Ired}░░░░{Hcyan}█{Ired}░
    ░░┃                                       ┃ ░░{Hcyan}█{Ired}░░░░░░░░{Hcyan}▀▀▀▀▀{Ired}░░░░░░░{Hcyan}▄▀{Ired}░░
    ░░┣┫{Nyellow}[04]{Twhite} BAIXAR POSTS DO INSTAGRAM{Ired}        ┃ ░░░{Hcyan}▀▀▄▄▄▄{Ired}░░░░░░░░░{Hcyan}▄▄▄▀▀{Ired}░░░░
    ░░┃                                       ┃ ░░{Hcyan}▄██▀▄▄▄█▀▀▀▀▀▀▀█▄▄▄▀██▄{Ired}░░
    ░░┣┫{Nyellow}[05]{Twhite} PUBLICAR FOTO INSTAGRAM{Ired}          ┃ ░{Hcyan}▄▀██{Ired}░░░░░{Hcyan}▀▀▀▀▀▀▀{Ired}░░░░░{Hcyan}██▀▄{Ired}░
    ░░┃                                       ┃ {Hcyan}█{Ired}░░{Hcyan}██{Ired}░░░░░░░░░░░░░░░░░{Hcyan}██{Ired}░░{Hcyan}█{Ired}
    ░░┣┫{Nyellow}[06]{Twhite} INSTA STALKER{Ired}                    ┃ {Hcyan}█{Ired}░░{Hcyan}██{Ired}░░░░░░░░░░░░░░░░░{Hcyan}██{Ired}░░{Hcyan}█{Ired}
    ░░┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ {Hcyan}█{Ired}░░{Hcyan}██{Ired}░░░░░░░░░░░░░░░░░{Hcyan}██{Ired}░░{Hcyan}█{Ired}
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{Hcyan}█{Ired}░░{Hcyan}██{Ired}░░░░░░░░░░░░░░░░░{Hcyan}██{Ired}░░{Hcyan}█{Ired}
    ░░░░░░{Hcyan}!LEMBRANDO QUE O USO CONSTANTE!{Ired}░░░░░░░{Hcyan}█{Ired}░░{Hcyan}██{Ired}░░░░░░░░░░░░░░░░░{Hcyan}██{Ired}░░{Hcyan}█{Ired}
    ░░░░░░░░░░{Hcyan}!PODE RESULTAR EM BAN!{Ired}░░░░░░░░░░░░{Hcyan}█{Ired}░░{Hcyan}██▄{Ired}░░░░░░░░░░░░░░░{Hcyan}▄██{Ired}░░{Hcyan}█{Ired}
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ {Hcyan}▀▀▄█{Ired}░{Hcyan}█▄▄▄▄{Ired}░░░░░░░{Hcyan}▄▄▄▄█{Ired}░{Hcyan}█▄▀▀{Ired}
    ░░░░░!USE A TOOL POR SUA CONTA E RISCO!░░░░░░░░░░░░░░{Hcyan}█▄▄▄▄▄▄▄█{Ired}░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ┏░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░┓
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
