#By: WENDEL CABRAL

import os
os.system('cls')


#variaveis
marcos=0
pedro=0
jose=0
raimundo=0
nulo=0
branco=0
votos=0



('###########################################################################')
print('####### BEM VINDO A URNA ELETRONICA #########')
print('DIGITE 1 PARA VOTAR EM MARCOS')
print('DIGITE 2 PARA VOTAR EM PEDRO')
print('DIGITE 3 PARA VOTAR EM JOSE')
print('DIGITE 4 PARA VOTAR EM RAIMUNDO')
print('DIGITE 5 PARA VOTAR NULO')
print('DIGITE 6 PARA VOTAR EM BRANCO')
print('###########################################################################')
opc=input('DIGITE O NUMERO DO SEU CANDIDATO OU 0 PARA SAIR: ')

while opc!=str(0):
    while opc==str(1):
        print('voto marcos')
        marcos+=1
        votos+=1
        opc=input('SE DESEJA CONTINUAR VOTANDO DIGITE O NUMERO DO SEU CANDIDATO OU 0 PARA SAIR: ')
        break
    while opc==str(2):
        print('voto pedro')
        pedro+=1
        votos+=1
        opc=input('SE DESEJA CONTINUAR VOTANDO DIGITE O NUMERO DO SEU CANDIDATO OU 0 PARA SAIR: ')
        break
    while opc==str(3):
        print('voto jose')
        jose+=1
        votos+=1
        opc=input('SE DESEJA CONTINUAR VOTANDO DIGITE O NUMERO DO SEU CANDIDATO OU 0 PARA SAIR: ')
        break
    while opc==str(4):
        print('voto raimundo')
        raimundo+=1
        votos+=1
        opc=input('SE DESEJA CONTINUAR VOTANDO DIGITE O NUMERO DO SEU CANDIDATO OU 0 PARA SAIR: ')
        break
    while opc==str(5):
        print('voto nulo')
        nulo+=1
        votos+=1
        opc=input('SE DESEJA CONTINUAR VOTANDO DIGITE O NUMERO DO SEU CANDIDATO OU 0 PARA SAIR: ')
        break
    while opc==str(6):
        print('voto branco')
        branco+=1
        votos+=1
        opc=input('SE DESEJA CONTINUAR VOTANDO DIGITE O NUMERO DO SEU CANDIDATO OU 0 PARA SAIR: ')
        break
    while (int(opc)>6 or int(opc)<0):
        print('NUMERO INVALIDO')
        opc=input('SE DESEJA CONTINUAR VOTANDO DIGITE O NUMERO DO SEU CANDIDATO OU 0 PARA SAIR: ')
        break
penulos=100-(((votos-nulo)/votos)*100)
pebrancos=100-(((votos-branco)/votos)*100)
pebranul=100-(((votos-(nulo+branco))/votos)*100)
print('###########################################################################')
print('FIM DA VOTACAO')
print('Processando resultados')
print('Canditado Marcos esta com ' + str(marcos) + ' votos')
print('Canditado Pedro esta com ' + str(pedro) + ' votos')
print('Canditado Jose esta com ' + str(jose) + ' votos')
print('Canditado Raimundo esta com ' + str(raimundo) + ' votos')
print('Tivemos um total de ' + str(nulo) + ' votos Nulos')
print('Tivemos um total de ' + str(branco) + ' votos Brancos')
print('Tivemos um total de ' + str(votos) + ' Eleitores neste votacao')
print(f'Tivemos um percentual de {penulos:.0f}% Nulos sobre o valor total de votos')
print(f'Tivemos um percentual de {pebrancos:.0f}% Brancos sobre o valor total de votos')
print(f'Tivemos um percentual de {pebranul:.0f}% Somando Nulos e Brancos, sobre o valor total de votos')
