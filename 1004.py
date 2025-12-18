#Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. 
#A seguir mostre a variável PROD com mensagem correspondente.   

#Entrada
#O arquivo de entrada contém 2 valores inteiros.

#Saída
#Imprima a mensagem "PROD" e a variável PROD conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade. 
#Não esqueça de imprimir o fim de linha após o produto, caso contrário seu programa apresentará a mensagem: “Presentation Error”.



A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

PROD = A * B

print(f"O valor de {A} * {B} é: {PROD}") #Por que uso de F? são f-stings usada para mencionar variveis dentro do print veio dps do py >3.6