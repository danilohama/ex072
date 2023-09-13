"""
 Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
count = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez'
       'Onze', 'Doze', 'Treze', 'Quartorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito'
       'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre \033[33m0\033[0m e \033[33m20\033[0m: '))
    if 0 <= num <=20:
        break
        print(f'Tente novamente!', end='')
print(f'Você digitou o número: \033[32m{count[num]}')
