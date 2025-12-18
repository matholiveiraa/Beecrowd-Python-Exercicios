#Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos
# ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, 
# deverá ser impressa a mensagem “Fora de intervalo”.

#O símbolo ( representa "maior que". Por exemplo:
#[0,25]  indica valores entre 0 e 25.0000, inclusive eles.
#(25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

#Entrada
#O arquivo de entrada contém um número com ponto flutuante qualquer.

#Saída
#A saída deve ser uma mensagem conforme exemplo abaixo.

print("Existem 4 intervalos: ")
print("[0,25]")
print("(25,50]")
print("(50,75]")
print("(75,100])")


valor = float(input("Qual o valor desejado? "))

if 0 <= valor <= 25:
    print(f"O valor que era: {valor}, encontra-se no intervalo 1!")
elif 25.00001 <= valor <= 50:
    print(f"O valor que era: {valor}, encontra-se no intervalo 2!")
elif 50.00001 <= valor <= 75:
    print(f"O valor que era: {valor}, encontra-se no intervalo 3!")
elif 75.00001 <= valor <= 100:
    print(f"O valor que era: {valor}, encontra-se no intervalo 4!")

elif valor < 0 or valor > 100.00001:
    print("Fora de intervalo!")