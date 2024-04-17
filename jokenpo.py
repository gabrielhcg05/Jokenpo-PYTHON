from random import randint
from time import sleep
pc = randint(0,2)

print('Select the game language: ')
print('''
[ 0 ] ES_US
[ 1 ] PT_BR''')
lang= int(input('> '))
if lang == 1:
    if pc == 0:
        pcj = str('Pedra')
    elif pc == 1:
        pcj = str('Papel')
    else:
        pcj = str('Tesoura')
    print('Suas opções:')
    print('''
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    lista = [0,1,2]
    jogada = 20
    while jogada not in lista:
        jogada=int(input('Qual é a sua jogada? '))

    if jogada == 0:
        j1 = str('Pedra')
    elif jogada == 1:
        j1 = str('Papel')
    else:
        j1 = str('Tesoura')

    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)

    print('-='*10)
    print('Computador jogou {}'.format(pcj))
    print('Jogador jogou {}'.format(j1))
    print('-='*10)

    if pc == jogada:
        print('Empate! :)')
    elif pc == 0:
        if jogada == 1:
            print('Papel ganha de pedra, você \033[32mVENCEU\033[m :D')
        else:
            print('Pedra quebra tesoura, você \033[31mPERDEU!\033[m xD')
    elif pc == 1:
        if jogada == 0:
            print('Papel ganha de pedra, você \033[31mPERDEU!\033[m xD')
        else:
            print('Tesoura corta o papel, você \033[32mVENCEU\033[m :D')
    else:
        if jogada == 0:
            print('Pedra quebra tesoura, você \033[32mVENCEU\033[m :D')
        else:
            print('Tesoura corta o papel, você \033[31mPERDEU!\033[m xD')
if lang == 0:
    if pc == 0:
        pcj = str('Rock')
    elif pc == 1:
        pcj = str('Paper')
    else:
        pcj = str('Scissors')
    print('Your options:')
    print('''
    [ 0 ] ROCK
    [ 1 ] PAPER
    [ 2 ] Scissors''')
    lista = [0,1,2]
    jogada = 20
    while jogada not in lista:
        jogada=int(input('What is your move? '))

    if jogada == 0:
        j1 = str('Rock')
    elif jogada == 1:
        j1 = str('Paper')
    else:
        j1 = str('Scissors')

    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)

    print('-='*10)
    print('PC Played {}'.format(pcj))
    print('Player played {}'.format(j1))
    print('-='*10)

    if pc == jogada:
        print('Draw! :)')
    elif pc == 0:
        if jogada == 1:
            print('Paper beats stone, you \033[32mWON!\033[m :D')
        else:
            print('Rock beats scissors, you \033[31mLOST!\033[m xD')
    elif pc == 1:
        if jogada == 0:
            print('Paper beats rock, you \033[31mLOST!\033[m xD')
        else:
            print('Scissors beats paper, you \033[32mWON!\033[m :D')
    else:
        if jogada == 0:
            print('Rock beats scissors, you \033[32mWON!\033[m :D')
        else:
            print('Scissors beats paper, you \033[31mLOST!\033[m xD')
