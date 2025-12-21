#Leia um número inteiro N

#Use um while para imprimir todos os números pares de 1 até N, um por linha

print("Iremos imprimir todos os números pares de 1 até n por linha")
N = int(input("Digite o valor de N: "))
C = 0
contador = 0 
while C <= N:
    if C % 2 == 0:
        print(N)
        C += 1
# Ainda a finalizar!!