# Faça um programa que imprima a quantidade de números pares
# entre dois números da sua escolha.



n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro número: '))
i = 0
while n1<=n2:
    if (n1 % 2) == 0:
        i = i + 1
    n1 = n1 + 1
print(i)
