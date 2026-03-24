#Prestação em Atraso

valor = float(input("Digite o valor: "))
taxa = float(input("Digite a taxa (%): "))
tempo = float(input("Digite o tempo do atraso: "))

prestação = valor + (valor * (taxa /100) * tempo)

print(f"Valor da prestação: R${prestação}")
