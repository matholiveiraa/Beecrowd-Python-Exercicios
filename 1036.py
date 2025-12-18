#Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
# Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
# caso haja uma divisão por 0 ou raiz de numero negativo.

#Entrada
#Leia três valores de ponto flutuante (double) A, B e C.

#Saída
#Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, 
# imprima o resultado das raízes com 5 dígitos após o ponto,
#  com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

#A B C terá ser float
#Formula

#a=1, b=8, c=-9.

#formula delta
#Δ = b² - 4ac

#Δ = 8² - 4(1)(-9) = 64 + 36 = 100.

#formula raizes 

# x = (-b ± √Δ) / 2a.

#x = (-8 ± √100) / 2(1) = (-8 ± 10) / 2.
#x' = (-8 + 10) / 2 = 2 / 2 = 1.
#x'' = (-8 - 10) / 2 = -18 / 2 = -9.
#As raízes são 1 e -9. 

print("Iremos calcular a formula de bhaskara de lhe apresentar as raizes")
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C "))

delta = B ** 2 -4*A*C

raiz1 = (-B + delta ** 0.5) / (2*A)
raiz2 = (-B - delta ** 0.5) / (2*A)


print(F"O valor de A era: {A}")
print(F"O valor de B era: {B}")
print(F"O valor de C era: {C}")
print(F"O valor de Δ delta: {delta}")

if A == 0: #apenas um = é atribuir valor, dois == é sinal de compação ou igualdade
    print("Não existe bhaskara")

elif delta < 0:
    print("Impossível calcular as raízes")

if A != 0 and (delta > 0):
    print(f"O delta era: {delta}")
    print(f"A raiz I é: {raiz1:.5f}")
    print(f"A raiz II é: {raiz2:.5f}")
