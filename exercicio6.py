# Faça um programa, utilizando while e listas, que permita o
# usuário escrever o nome de cinco pessoas e os mostre na tela.

contador = 1
listanomes = []

while contador < 6:
    listanomes.append(input(f'Informe o {contador}º nome: '))
    contador += 1

print(f'Nomes: {listanomes}')
