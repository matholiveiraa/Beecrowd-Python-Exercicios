#Saída
#O programa deve imprimir um valor inteiro. 
#Este valor é a soma dos valores pares estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

#exemplos de entrada:
#A 6
#B -5
#Dentre eles possui 6 numeros pares


#A 15
#B 12
#Dentre eles possui só o 12 o 14 numeros pares dentre cada espaço

print("Iremos fazer um programa que calcula o total de numero pares entre A e B")
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

contador = 0

maximo = max(A,B)
minimo = min(A,B)

for C in range(minimo +1, maximo):
    if C % 2 == 0:
        contador += C

print(contador)