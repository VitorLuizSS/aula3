#Consumo de combústivel

tempo = float(input("Tempo da viagem (h): "))
velocidade = float(input("Velocidade média (km/h): "))

distancia = tempo * velocidade
litros_usados = distancia / 12

print(f"Tempo da viagem: {tempo} horas")
print(f"Velocidade média: {velocidade} km/h")
print(f"Distância: {distancia} km")
print(f"Livros usados: {litros_usados} litros de combustível")
