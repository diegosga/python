from random import randint
npc=randint(0,5)
print("Pensei em um numero entre 1 e 5, advinhe!")
nj=int(input("Digite o numero que advinhou:"))
if nj == npc:
    print("Parabens! Você acertou!")
else:
    print("Que pena, tente novamente.")