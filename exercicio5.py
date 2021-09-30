# Faça um programa, utilizando while, que mostre na tela de
# 0 até N, em que N é o limite inserido pelo usuário.

numero = 1
n = int(input('Digite o último número que será listado, começando do 0: '))

while numero <= n:
    print(numero)
    numero += 1