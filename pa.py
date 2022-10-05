indice=int(input("Digite a razão: "))
pritermo=int(input("Digite o primeiro termo: "))
decimo=pritermo + 9*indice
for c in range(pritermo,decimo+indice,indice):
    print(c)