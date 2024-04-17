#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
pc = randint(0,2)
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