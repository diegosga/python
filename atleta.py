idade=int(input("Digite a idade do atleta: "))
if idade<=9:
    print("O atleta é mirim")
elif idade>9 and idade<=14:
    print("O atleta é infantil")
elif idade>14 and idade<=19:
    print("O atleta é junior")
elif idade>19 and idade<=25:
    print("O atleta é sênior")
else:
    print("O atleta é master")


