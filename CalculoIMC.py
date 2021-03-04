#By: WENDEL CABRAL

#IMPORTS
import os
import time

os.system('cls')
print('########################################################')
print('#################### CALCULE SEU IMC ###################')
print('########################################################')

peso=input('Informe o seu peso: ')
altura=input('Informe a sua altura: ')

print('Calculando aguarde')
time.sleep(1)
print('Calculando aguarde.')
time.sleep(1)
print('Calculando aguarde..')
time.sleep(1)
print('Calculando aguarde...')
time.sleep(1)
print('Calculando finalizado!')
time.sleep(3)

imc= float(peso) / (float(altura)*float(altura))
print(imc)
if imc < 17:
    msg='Muito abaixo do peso'
elif imc >= 17 and  imc <=18.49:
    msg='Abaixo do peso'
elif imc >= 18.50 and  imc <=24.99:
    msg='Peso normal'
elif imc >= 25 and  imc <=29.99:
    msg='Excesso de peso'
elif imc >= 30 and  imc <=34.99:
    msg='Obesidade Grau 1'
elif imc >= 35 and  imc <=39.99:
    msg='Obesidade Grau 2'
else:
    msg='Obesidade Grau 3'

os.system('cls')
print('########################################################')
print('###### Resultado: ' + msg + ' ###### seu IMC: ' + '%.2f' % imc)
print('########################################################')