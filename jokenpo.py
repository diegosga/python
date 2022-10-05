from random import randint

print('''[0] pedra
[1] papel
[2] tesoura''')
opcoes=('pedra','papel','tesoura')
escolha=int(input('escolha: '))
pcescolha= randint(0, 2)
print('Jogador jogou ',opcoes[escolha])
print('Computador jogou',opcoes[pcescolha])
if escolha==0:
    if pcescolha==0:
        print('Jogada invalida')
    elif pcescolha==1:
        print('Você perdeu')
    else:
        print('Você ganhou')
if escolha==1:
    if pcescolha==0:
        print('Você ganhou')
    elif pcescolha==1:
        print('Jogada invalida')
    else:
        print('Você perdeu')
if escolha==2:
    if pcescolha==0:
        print('Você perdeu')
    elif pcescolha==1:
        print('Você ganhou')
    else:
        print('Jogada invalida')
