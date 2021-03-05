import random
import os
import datetime 
os.system("cls")
#VARIAVEIS
#ALUNO: ALUISIO WENDEL CABRAL DA SILVA

#VARIAVEIS
senha=""
i=0
quebrador=random.randrange(0,999)

#GERANDO SENHA
while (i<3):
  gerador=random.randrange(0,9)
  senha=str(senha)+str(gerador)
  i+=1

#PAUSA PARA ANALISAR A SENHA  
print("Senha que vamos quebrar usando RANDOM: " + senha)
os.system("pause")
hinicial=datetime.datetime.now()

#QUEBRANDO A SENHA
while (int(senha) != quebrador):
  quebrador=random.randrange(000,999)
  print("Senha gerada: " + senha + " / Quebrando senha: " + str(quebrador) )

#FIM DE PROGRAMA  
hfinal=datetime.datetime.now()
print("Data e hora de inicio: " + str(hinicial))
print("Data e hora de Final: " + str(hfinal))
print(hfinal - hinicial)
