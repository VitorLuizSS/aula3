# Ler em graus Celsius e converter para Fahrenheit. 
# A fórmula de conversão é F = (9 * C + 160) / 5, sendo F farenheit e C celsius.

import math 

print("Converta Celsius para Farenheit")

celsius = float(input("Digite uma Temperatura em Celsius: "))
fah = (9 * celsius + 160)/5
print(f"{celsius}°C convertido para Farenheit é: {fah}°F")
