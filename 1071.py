#Leia 2 valores inteiros X e Y. A seguir, 
# calcule e mostre a soma dos números impares entre eles.

#Entrada
#O arquivo de entrada contém dois valores inteiros.

#Saída
#O programa deve imprimir um valor inteiro. 
#Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

#exemplos de entrada:
#A 6
#B -5
#Dentre eles possui 5 numeros imparares.


#A 15
#B 12
#Dentre eles possui só o 13, ele quer o total de numeros impares dentre cada espaço

print("Veremos a quantidade de números ímpares obtidos entre cada 2 valores e iremos somar")

X = int(input("Digite o valor de X: "))
Y = int(input("Digite o valor de Y: "))

menor = min(X, Y) #estamos vendo quem é o menor entre x e y
maior = max(X, Y) #estamos vendo quem é o maior entre x e y

acumulador = 0 #Variável acumuladora vamos guardar a soma dos números ímpares encontrados.

for n in range(menor + 1, maior): # Para n num loop de menor percorrer até maior
    if n % 2 != 0: #enquanto N for numeros impares
        acumulador += n #aculador recebe mais n

print(acumulador)

#Ou seja a variavel n vai me gerar um loop do numero maior com +1,a até o numero  maior, IF ele for números impares
#Depois disso o a variavel acumuladora vai ganhar a soma dos numeros imparares