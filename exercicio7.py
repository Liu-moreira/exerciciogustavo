# Faça um programa, utilizando while, que permita o usuário fazer 
# contas de adição enquanto quiser.

print('\nOperação - Adição!\n')

while True:
    n1 = int(input('Digite um númerco: '))
    n2 = int(input('Digite um númerco: '))
    soma = int(n1 + n2)
    print(f'{n1} + {n2} = {soma}')
    resp = str(print(input('\nDeseja realizar mais uma soma? [S ou N]\nResposta: ')))
    if resp == 'S' or resp == 's':
        continue
    elif resp == 'N' or resp == 'n':
        break
    
    


            
print('Fim')


