#Leia 4 valores inteiros A, B, C e D.
# A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, 
# ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

#Entrada
#Quatro números inteiros A, B, C e D.

#Saída
#Mostre a respectiva mensagem após a validação dos valores.

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

#1° A seguir, se B for maior do que C e Se D for maior do que A
# B > (C e D) > A
# (C + D) > (A > B)
# (C e D) positovos 
# A deve ser par
# Valores positivos

if B > C and D > A and (C + D) > (A + B) and (C > 0 and D > 0) and A % 2 == 0:
    print("Valores aceitos!")
else:
    print("Valores não aceitos!")