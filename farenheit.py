# Ler em graus Fahrenheit e converter para Celsius. 
# A fórmula de conversão é C = ((F -32)*5) / 9, sendo F farenheit e C celsius.

import math 

print("Converta Farenheit para Celsius")

fah = float(input("Digite uma Temperatura em Farenheit: "))
celsius = ((fah - 32) * 5) / 9
print(f"{fah}°F convertido para Celsius é: {celsius}°C")
