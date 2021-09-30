# Faça um programa, utilizando while e listas, que permita o 
# usuário realizar o cadastro de um número indeterminado de 
# pessoas enquanto quiser e os mostre na tela ao finalizar.


print('\nCADASTRO - PYTHON JOBS\n')
print('Digite 0 para para terminar o cadastro!\n')
listapessoa = []

while True:
    pessoa = input('Insira o nome do funcionário: ')
    listapessoa.append(pessoa)
    if pessoa == '0':
        listapessoa.remove('0')
        print((f'\nFuncionários: {listapessoa}'))
        break

