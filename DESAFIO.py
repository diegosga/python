km=float(input('Digite a quilometragem: '))
if km>80:
    a=km-80
    p=a*7
    print('você foi multado em: R$ {}'.format(p))
else:
    print('não tem multa pra pagar!')