anonasc= int(input("em que ano nasceu? "))
idade = 2022 - anonasc
if idade==18:
    print("Esse ano deve se alistar pro serviço militar")
elif idade <18:
    afalta=18-idade
    print("faltam {} anos para se alistar".format(afalta))
elif idade>18:
    print("Ja passou do prazo do alistamento")