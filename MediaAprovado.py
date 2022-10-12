n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
media = (n2+n1)/2
if media < 5.0:
    print("Reprovado")
elif media>=7:
    print("Aprovado")
else:
    print("Precisa de recuperação")
