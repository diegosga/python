vcasa=float(input("Qual o valor da casa? "))
salario=float(input("Qual é o seu salário? "))
anos=int(input("Em quantos anos vai pagar?"))
prestacao=vcasa/(anos*12)
if prestacao<=0.3*salario:
    print("Emprestimo aprovado")
else:
    print("Emprestimo negado")
