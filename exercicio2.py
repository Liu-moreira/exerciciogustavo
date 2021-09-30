# Faça um Programa que leia três números inteiros e mostre o
# maior deles.

n1 = int(input('Informe um número: '))
n2 = int(input('Informe um segundo número: '))
n3 = int(input('Informe um terceiro número: '))  

maior = n1
if n2 > maior:
    maior = n2
elif n3 > maior:
    maior = n3
print('O maior número é: ', maior)



