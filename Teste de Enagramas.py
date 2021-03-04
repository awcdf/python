#By: WENDEL CABRAL

import os
os.system('cls')


print('####### TESTE DE ENAGRAMAS #########')
txt1=input('Digite a primeira palavra: ')
os.system('cls')
txt2=input('Digite a segunda palavra: ')
os.system('cls')

#CRIANDO A PRIMEIRA LIST DE LETRAS COM OS DADOS DA PRIMEIRA PALAVRA
lisx=[]
pos=0
for i in txt1:
    lisx.insert(pos, i)
    pos+=1

#CRIANDO A SEGUNDA LIST DE LETRAS COM OS DADOS DA SEGUNDA PALAVRA
lisx2=[]
pos=0
for i in txt2:
    lisx2.insert(pos, i)

#COMO JA TEMOS DUAS LISTAS COM AS LETRAS SEPARADAS, AGORA TEMOS APENAS QUE TESTAR SE SAO IGUAIS. 
#SERIA MAIS FACIL TESTAR USANDO O IF, POREM SEGUINDO AS OIRENTACOES DO EXERCICIO VAMOS USAR WHILE NOVAMENTE.
while(lisx==lisx2):
    result='Sim temos!'
    break
else:
    result='Nao temos!'
print('############### RESULTADO ##############')
print('Sua primeira palavra foi: ' + txt1)
print('Sua segunda palavra foi: ' + txt2)
print('Temos um anagrama? ' + result)
print('########################################')
