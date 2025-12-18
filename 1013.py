#“Entre A e B, quem ganha?”
#“Agora o vencedor luta com C.”
#“Quem sobrar é o campeão.” 🏆


print("Veremos quem é que quem entre A e B e depois este número ira lutar com C")
print("Ou seja quem quem é maior que quem, primeiro a e b, depois C")
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D1 = 0 # se eu tivesse coloca int não teria apontado o valor e daria erro na questao!!!


if A > B:
    print(F"A ganhou de B, sendo seu valor: {A}")
    D1 = A

elif A < B:
    print(F"B ganhou de A, sendo seu valor: {B}")
    D1 = B



if D1 > C:
    print(F"{D1} é maior que C")
else:
    print(f"O C é maior: {C}")
