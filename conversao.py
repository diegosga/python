num=int(input("Digite o numero: "))
print("""Qual conversão você quer?
[1]binario  [2]octal [3]hexadecimal""")
altern=int(input("Sua escolha: "))
if altern == 1:
    print(bin(num)[2:])
if altern==2:
    print(oct(num)[2:])
if altern==3:
    print(hex(num)[2:])
