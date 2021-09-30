# # Faça um programa que pergunta a idade do usuário e informe se 
# # ele está apto a votar ou não.

idade = int(input('Qual a sua idade?: '))

if idade < 16:
    print('Voto inválido!')

elif idade >= 16 and idade < 18:
    print('Voto opcional!')

elif idade >= 18 and idade <= 70:
    print('Voto Obrigatório!')

else:
    if idade > 70:
        print('Voto opcional!')
