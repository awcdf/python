#By: WENDEL CABRAL

#import
import os
os.system('cls')

######### JOGO DA FORCA #########
#criando variaves
nErros = 0
lAcertadas = []
lChutadas = []
print("####### BEM VINDO(A) AO JOGO DA FORCA #######")
pAdvinha = input('Informe o nome da palavra para ser adivinhada: ').strip().lower()
os.system('cls')

#Adcionando * onde não tem letra certa
def relatorio():
    palavra = ""
    for l in pAdvinha:
        if l in lChutadas:
            palavra += l
        else:
            palavra += "*"
    return palavra

#Perguntando palavra para testar
print("####### O JOGO COMECOU! ####### ")
while (nErros < 10):
    chute = input("Digite uma letra: ").strip().lower()
    if chute in lChutadas: 
        print("Já foi digitado essa letra, tente outra: ")
    else:
        lChutadas += chute
        if chute in pAdvinha:
            lAcertadas += chute
            print("Letra correta, acertou!")
            print(relatorio())
            if relatorio() == pAdvinha:
                print("FIM DE JOGO, VOCE GANHOU !")
                break
        else:
            nErros += 1
            print("Letra não existe, errou!")
            print(f'Voce tem {10-nErros} tentativas')
            print(relatorio())
            #imprimindo a forca
            if (nErros > 0 and nErros <=2):
                print("____")
                print("| |")
            elif (nErros > 2 and nErros <=4):
                print("____")
                print("| |")
                print("| O ")
            elif (nErros > 4 and nErros <=6):
                print("____")
                print("| |")
                print("| O ")
                print("| /|\ ")
            elif (nErros > 6 and nErros <=9):
                print("____")
                print("| |")
                print("| O ")
                print("| /|\ ")
                print("| / \ ")
            elif (nErros > 9 and nErros <= 10):
                print("____")
                print("| |")
                print("| O ")
                print("| /|\ ")
                print("| / \ ")
                print("|")
                print("Voce foi enforcado!")
                print("FIM DE JOGO")
                break


