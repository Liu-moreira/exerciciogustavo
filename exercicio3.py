# Faça um Programa que leia três números inteiros, em seguida
# mostre o maior e o menor deles.

n1 = int(input('Informe um número: '))
n2 = int(input('Informe um segundo número: '))
n3 = int(input('Informe um terceiro número: '))  

maior = n1
if n2 > maior:
    maior = n2
elif n3 > maior:
    maior = n3
print('O maior número é: ', maior)

if n1 < n2 and n1 < n3:
    print('O menor número é: ', n1)
elif n2 < n1 and n2 < n3:
    print('O menor número é: ', n2)
else: 
    print('O menor número é: ', n3)