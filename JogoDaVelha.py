#By: WENDEL CABRAL

#IMPORTS
import os
import random
from colorama import Fore, Back, Style
os.system('cls')

#VARIAVEIS
jogarNovamente='s'
jogadas=0
quemJoga=2
maxJogadas=9
vit='n'
velha=[
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]
##TELA JOGO DA VELHA
def tela():
  global velha 
  global jogadas
  os.system('cls')
  print('    0   1   2')
  print('0:  ' + velha[0][0] + ' | ' + velha[0][1] + ' | ' + velha[0][2])
  print('   -----------')
  print('1:  ' + velha[1][0] + ' | ' + velha[1][1] + ' | ' + velha[1][2])
  print('   -----------')
  print('2:  ' + velha[2][0] + ' | ' + velha[2][1] + ' | ' + velha[2][2])
  print('Jogadas: ' + Fore.GREEN +  str(jogadas) + Fore.RESET)

#JOGADOR 1
def jogadorJoga1():
  global jogadas
  global quemJoga
  global maxJogadas

  if quemJoga==2 and jogadas<maxJogadas:
    try:
      print('### JOGADOR 1 ###')
      l=int(input('Linha....: '))
      c=int(input('Coluna...: '))  
      while velha[l][c]!= ' ':
        l=int(input('Linha....: '))
        c=int(input('Coluna...: '))
      velha[l][c]='X'
      quemJoga=1
      jogadas+=1
    except:
      print('Linha ou colunoe invalida')
      os.system('pause')

#JOGADOR 2
def jogadorJoga2():
  global jogadas
  global quemJoga
  global maxJogadas

  if quemJoga==1 and jogadas<maxJogadas:
    try:
      print('### JOGADOR 2 ###')
      l=int(input('Linha....: '))
      c=int(input('Coluna...: '))  
      while velha[l][c]!= ' ':
        l=int(input('Linha....: '))
        c=int(input('Coluna...: '))
      velha[l][c]='O'
      quemJoga=2
      jogadas+=1
    except:
      print('Linha ou colunoe invalida')
      os.system('pause')

#CPU JOGANDO AUTOMATICO, POREM NÃO TAO INTELIGENTE RSRS
def CpuJoga():
  global jogadas
  global quemJoga
  global maxJogadas
  if quemJoga==1 and jogadas<maxJogadas:
    l=random.randrange(0,3)
    c=random.randrange(0,3)
    while velha[l][c]!= ' ':
      l=random.randrange(0,3)
      c=random.randrange(0,3)
    velha[l][c]='O'
    quemJoga=2
    jogadas+=1

#TESTE DE VITORIA    
def VerificarVitoria():
  global velha
  vitoria='n'
  simbolos=['X','O']
  for s in simbolos:
    vitoria='n'
    #VERIFICAR LINHA HORIZONTAL
    il=0
    ic=0
    while il<3:
      soma=0
      ic=0
      while ic<3:
        if (velha[il][ic]==s):
          soma+=1
        ic+=1
      if(soma==3):
        vitoria=s
        break
      il+=1
    if(vitoria!='n'):  
      break
    #VERIFICAR LINHA VERTICAL 
    il=0
    ic=0
    while ic<3:
      soma=0
      il=0
      while il<3:
        if (velha[il][ic]==s):
          soma+=1
        il+=1
      if(soma==3):
        vitoria=s
        break
      ic+=1
    if(vitoria!='n'):  
      break
    #VERIFICA DIAGONAL DA ESQUERDA PARA DIREITA
    soma=0
    idiag=0
    while idiag<3:
      if(velha[idiag][idiag]==s):
        soma+=1
      idiag+=1
      if(soma==3):
        vitoria=s
        break
    if(vitoria!='n'):  
      break
    #VERIFICA DIGONAL DIREITA PRA ESQUERDA
    soma=0
    idiagl=0
    idiagc=2
    while idiagc>=0:
      if (velha[idiagl][idiagc]==s):
         soma+=1
      idiagl+=1
      idiagc-=1
      if(soma==3):
        vitoria=s
        break
    if(vitoria!='n'):  
      break
  return vitoria

#ZERA O JOGO
def Redefinir():
  global velha
  global jogadas
  global quemJoga
  global maxJogadas
  global vit
  jogadas=0
  quemJoga=2
  maxJogadas=9
  vit='n'
  velha=[
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
  ]

#ANALISAR VITORIA  
def vVitoria():
    if(vit!='n')or(jogadas>=maxJogadas):
      return 1
      

#INICIO DO JOGO
while(jogarNovamente=='s' or jogarNovamente=='S'):
  print("#### BEM VINDO(A) AO JOGO DA VELHA ####")
  print("Digite 1 para jogar com outro jogador")
  print("Digite 2 para jogar com a maquina")
  nJogadores=input("Opcao: ")
  #JOGADOR CONTRA JOGADOR
  if(nJogadores == "1"):
    while True:
      tela()
      jogadorJoga1()
      vit=VerificarVitoria()
      tela()
      if (vVitoria() == 1):
          break
      tela()
      jogadorJoga2()
      vit=VerificarVitoria()
      tela()
      if (vVitoria() == 1):
          tela()
          break
      else:
          continue
  #JOGADOR CONTRA MAQUINA      
  elif(nJogadores == "2"):
    while True:
      tela()
      jogadorJoga1()
      vit=VerificarVitoria()
      tela()
      if (vVitoria() == 1):
          break
      tela()
      CpuJoga()
      vit=VerificarVitoria()
      tela()
      if (vVitoria() == 1):
          tela()
          break
      else:
          continue
  #FIM DE JOGO E RESULTADOS      
  if(vit=='X' or vit=='O'):
    print(Fore.RED + 'FIM DE JOGO' + Fore.YELLOW)
    print('Resultado: Jogador ' + vit + ' Venceu' + Fore.RESET)
  else:
    print(Fore.BLUE + 'Resultado: Empate' + Fore.RESET)
  jogarNovamente=input(Fore.CYAN + 'jogar novamente? [s/n]: ' + Fore.RESET)
  if(jogarNovamente == "s".lower().strip()):
    os.system('cls')
  Redefinir()
print('FIM DO PROGRAMA')