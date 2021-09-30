# Faça um programa que imprima a soma de todos os números pares
# entre dois números da sua escolha.

listas = []
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro número: '))
i = 0
while (n1<=n2):
    if (n1 % 2) == 0:
        listas.append(n1)
    n1 = n1 + 1
    
somalista = sum(listas)
print(listas)
print(f'A soma de números pares é: {somalista}')

# enquanto  num  <=  num2 :
#     se  num  %  2  ==  0 :
#         pares . anexar ( num )
#     num  =  num  +  1

# por  par  em  Pares :
#     soma  + =  par