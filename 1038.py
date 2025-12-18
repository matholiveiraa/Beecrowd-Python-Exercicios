#Cachorro quente 4.00
#X-Salada 4.50
#X-Bacon 5.00
#Torrada simples 2.00
#Refrigerante 1.50

#ver quantos cada um pegou e quais pegou e fazer a conta

cachorroquente = 0
xsalada = 0
xbacon = 0
torradasimples = 0
refrigerante = 0

vcachorroquente = 4.00
vxsalada = 4.50
vxbacon = 5.00
vtorradasimples = 2.00
vrefrigerante = 1.50


print("Valor de cada item: ")
print("Cachorro quente 4.00")
print("X-Salada 4.50")
print("X-Bacon 5.00")
print("Torrada simples 2.00")
print("Refrigerante 1.50")

print("Passaremos a lista e você digitará 1 ou mais para o item desejado e 0 para não!")

cachorroq=int(input("Quer cachorro quente? "))
if cachorroq >= 1:
    cachorroquente = cachorroq
elif cachorroq == 0:
    cachorroquente = 0

xsaladaq=int(input("Quer x-salada? "))
if xsaladaq >= 1:
    xsalada = xsaladaq
elif xsaladaq == 0:
    xsalada = 0

xbaconq=int(input("Quer x-bacon? "))
if xbaconq >= 1:
    xbacon = xbaconq
elif xbaconq == 0:
    xbacon = 0

torradaq=int(input("Quer torrada? "))
if torradaq >= 1:
    torrada = torradaq
elif torradaq == 0:
    torrada = 0

refrigeranteq=int(input("Quer refrigerante? "))
if refrigeranteq >= 1:
    refrigerante = refrigeranteq
elif refrigeranteq == 0:
    refrigerante = 0

print(f"Itens desejados na seguinte ordem!")
print(f"cachorro-quente? quantidade: {cachorroquente}, valor: {cachorroquente*vcachorroquente}")
print(f"x-salada? quantidade: {xsalada}, valor: {xsalada*vxsalada}")
print(f"x-bacon? quantidade: {xbacon}, valor: {xbacon*vxbacon}")
print(f"torrada? quantidade: {torrada}, valor: {torrada*vtorradasimples}")
print(f"refrigerante? quantidade: {refrigerante}, valor: {refrigerante*vrefrigerante}")

total = (cachorroquente*vcachorroquente) + (xsalada*vxsalada) + (xbacon*vxbacon) + (torrada*vtorradasimples) + (refrigerante*vrefrigerante)

print(f"O total seria: {total}")

