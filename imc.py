# script simples para calculo do IMC

print('-' * 30)
print(f'{" Calculadora IMC ":-^30}')
print('-' * 30)

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura**2)
print('\n')
print(f'IMC: {imc:.2f}')
'''IMC	            CLASSIFICAÇÃO	OBESIDADE (GRAU)
MENOR QUE 18,5	        MAGREZA	            0
ENTRE 18,5 E 24,9	    NORMAL	            0
ENTRE 25,0 E 29,9	    SOBREPESO	        I
ENTRE 30,0 E 39,9	    OBESIDADE	        II
MAIOR QUE 40,0	        OBESIDADE GRAVE	    III

'''
if imc < 18.5:
    print('''Classificação: Magreza
Obesidade (grau) = 0''')
elif imc >= 18.5 and imc <=24.9:
    print('''Classificação: Normal
Obesidade (grau) = 0''')
elif imc >= 25 and imc <=29.9:
    print('''Classificação: Sobrepeso
Obesidade (grau) = 1''')
elif imc >= 30 and imc <= 39.9:
    print('''Classificação: Obesidade
Obesidade (grau) = 2''')
else:
    print('''Classificação: Obesidade grave
Obesidade (grau) = 3''')