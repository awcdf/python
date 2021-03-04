#By: WENDEL CABRAL

import os
os.system('cls')

contdisc=1
dicc={}


print('########################################################')
print('######### BRINCADO COM DICIONARIO #########')
print('########################################################')
print('DIGITE 1 PARA CADASTRAR TEXTOS NO DICIONARIO')
print('DIGITE 2 PARA LISTAR O DICIONARIO')
print('DIGITE 3 PARA CONTA CARACTERES DE UM ITEM DO DICIONARIO')
print('DIGITE 4 PARA EXCLUIR UM TEXTO DO DICIONARIO')
print('DIGITE 0 PARA SAIR')
opc=input('Digite a opcao: ')
while(opc !=str(0)):
    while(opc==str(1)):
        txt=input('Informe o texto que deseja guardar no dicionario: ')
        dicc[contdisc] = txt
        contdisc+=1
        os.system('cls')
        print('Texto guardado com sucesso!')
        break
        print('######################################################################################')
        print('DIGITE 1 PARA CADASTRAR TEXTOS NO DICIONARIO')
        print('DIGITE 2 PARA LISTAR O DICIONARIO')
        print('DIGITE 3 PARA CONTA CARACTERES DE UM ITEM DO DICIONARIO')
        print('DIGITE 4 PARA EXCLUIR UM TEXTO DO DICIONARIO')
        print('DIGITE 0 PARA SAIR')
        opc=input('Digite a opcao: ')
    while(opc==str(2)):
        os.system('cls')
        print('######## LISTA DE TEXTOS DO DICIONARIO ########')
        for d in dicc:
            print(f'posição: {d} = {dicc[d]}')
        break
    while(opc==str(3)):
        texto=input('Digite a posição do texto que se encontra no dicionario: ')
        cont=0
        ctr=input('Digite quais caracteres deseja buscar: ')
        #PRIMEIRA FORMA DE CONTAR
        for caracter in dicc[int(texto)]:
            if caracter in 'abcdefghijklmnopqrstuvwxyz':
                cont+=1
        print(f'O numero total caracter é: {cont}')
        #SEGUNDA FORMA DE CONTAR
        print('O numero de caracter é de acordo com sua escolha e: ' + str(str(dicc[int(texto)]).count(ctr)))
        break
    while(opc==str(4)):
        de=input('Digite o numero da posição que deja excluir: ')
        dicc.pop(int(de))
        break
    print('######################################################################################')
    print('DIGITE 1 PARA CADASTRAR TEXTOS NO DICIONARIO')
    print('DIGITE 2 PARA LISTAR O DICIONARIO')
    print('DIGITE 3 PARA CONTA CARACTERES DE UM ITEM DO DICIONARIO')
    print('DIGITE 4 PARA EXCLUIR UM TEXTO DO DICIONARIO')
    print('DIGITE 0 PARA SAIR')
    opc=input('Digite a opcao: ')
        
        
