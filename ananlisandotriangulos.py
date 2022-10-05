a=float(input())
b=float(input())
c=float(input())
t=0
if a<b+c and b<a+c and c<a+b:
    print('O triangulo é formado')
else:
    print("não é formado o triangulo")