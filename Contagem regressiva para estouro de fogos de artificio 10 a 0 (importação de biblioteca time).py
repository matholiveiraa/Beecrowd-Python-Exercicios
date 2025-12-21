#Faça um programa que mostre na tela uma contagem regressiva
#Para estouro de fogos de artifício
#Indo de 10 até 0
#Com uma pausa de 1 segundos entre eles
#Precisamos importar a biblioteca de Time em python

import time # esse é  o import da biblioteca time!

print("Preparado para contagem regressiva de fogos de artifício?")
time.sleep(3) # Espera por 3 segundos
print("Vamos então!!") #Exemplo


for temporizador in range(10, 0, -1): #Não se esqueça INICIO, FIM, PASSO!!!!!
    time.sleep(1)
    print(temporizador)
print("✨")