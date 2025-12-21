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

print("Veremos os valores dentro de numero A e B que sejam pares e faremos a soma de deles")
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

valormaximo = max(A,B)
valorminimo= min(A,B)

contador = 0

for c in range(valorminimo +1 ,valormaximo):
    if (c) % 2 == 0:
        contador += c

print(contador)

#O C serviu como uma variavel para guardar todos os valores pares dentro dele e fazer o loop de min adicionando +1 até o max 