#By: WENDEL CABRAL

import os
os.system('cls')

list = ['Telefonou para a vítima?: ', 'Esteve no local do crime?: ', 'Mora perto da vítima?: ', 'Tinha dívidas com a vítima?: ', 'Já trabalhou com a vítima?: ']
cont=0

print('########################################################')
print('BEM VINDO A INVESTIGACAO PYTHON')
print('RESPONDA AS PERGUNTAS, DIGITE SIM OU NAO')
print('########################################################')
pergunta=input(list[0])
while(pergunta=='sim'):
    cont+=1
    break
pergunta=input(list[1])
while(pergunta=='sim'):
    cont+=1
    break
pergunta=input(list[2])
while(pergunta=='sim'):
    cont+=1
    break
pergunta=input(list[3])
while(pergunta=='sim'):
    cont+=1
    break
pergunta=input(list[4])
while(pergunta=='sim'):
    cont+=1
    break

while(cont<=1):
    print('Voce é Inocente')
    break
while(cont==2):
    print('Voce é Suspeita')
    break
while(cont==3 or cont==4):
    print('Voce é Cúmplice')
    break
while(cont==5):
    print('Voce é Assassino')
    break
print('######## FIM DA INVESTIGACAO ########')
