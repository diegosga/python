a=int(input("Digite o primeiro numero: "))
b=int(input("Digite o segundo numero: "))

if a>b:
    maior = a
    print("o maior valor é", maior)
elif a<b:
    maior=b
    print("o maior valor é", maior)
elif a==b:
    print("os dois são iguais")
