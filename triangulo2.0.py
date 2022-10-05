l1 = float(input("Digite o primeiro lado: "))
l2 = float(input("Digite o segundo lado: "))
l3 = float(input("Digite o terceiro lado: "))
if l1<l2+l3 and l2<l3+l1 and l3<l2+l1:
    if l1!=l2!=l3:
        print('Pode formar um triangulo escaleno')
    elif l1==l2==l3:
        print('Pode formar um triangulo equilatero')
    else:
        print('Pode formar um triangulo isoceles')
else:
    print("Não pode formar um triangulo")
