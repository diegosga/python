n1=int(input())
n2=int(input())
n3=int(input())
menor=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior= n3
print('o menor é {} e o maior é {} '.format(menor, maior))
