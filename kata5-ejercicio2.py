print( "Programa para obtener la distancia entre dos planetas, basado en su distancia al sol: ")
print("-"*80)
planeta1= input("Distancia del sol al primer planeta en KM: ")
planeta2 = input("Distancia del sol al segundo planeta en KM: ")
planeta1= int(planeta1)
planeta2= int(planeta2)

distancia = planeta1-planeta2

distance_mi = distancia / 1.609344


print(abs(distance_mi), "Millas")
print(abs(distancia), "KM")