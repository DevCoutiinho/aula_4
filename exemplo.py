n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = 0

for i in range (n1,n2):
    if i % 2 ==0:
        soma += i

if soma > 0:
    print(f'O resultado da soma dos números pares é {soma}')
else:
    print(f'Não existe números pares nesses intervalos')
