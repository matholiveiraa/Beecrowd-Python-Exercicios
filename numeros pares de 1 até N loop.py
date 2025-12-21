#Leia um número inteiro N

#Use um loop para imprimir somente os números pares de 1 até N, um por linha

print("Iremos imprimir todos os números pares de 1 até N, por linha:")

N = int(input("Digite o número N: "))

for C in range(0+1, N+1):  # C percorre todos os números de 1 até N
    if C % 2 == 0:        # verifica se o número é par
        print(C)          # imprime os números par

