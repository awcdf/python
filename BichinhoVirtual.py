#By: WENDEL CABRAL

#IMPORTS
import os

#CRIANDO CLASS E FUNCOES
class Tamagushi():
    def __init__(self,nome,fome,saude,idade,humor):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = humor
    
    def altNome(self,novoNome):
        self.nome = novoNome
        self.fome-=20
        self.humor-=30
        self.altSaude()
    
    def altFome(self):
        self.fome+=20
        self.altSaude()
    
    def altSaude(self):
        if self.verHumor() == 'Feliz':
            self.saude=100
        elif self.verHumor() == 'Otimo':
            self.saude=80
        elif self.verHumor() == 'Tranquilo':
            self.saude=60
        elif self.verHumor() == 'Triste':
            self.saude=40
        elif self.verHumor() == 'Chorando':
            self.saude=20
        elif self.verHumor() == 'Morreu':
            self.saude=0

    def darRemedio(self):
        self.fome+=1
        self.humor+=1
        self.altSaude()

    def altIdade(self, newIdade):
        self.idade = newIdade
        self.fome-=20
        self.humor-=50
        self.altSaude()

    def brincar(self):
        self.fome-=5
        self.humor+=10
        self.altSaude()
    
    def verHumor(self):
        vrfome=0.0
        vrhumor=0.0
        if(self.fome<=0):
            vrfome = 100
            self.fome=0
        if(self.fome>=1 and self.fome<=25):
            vrfome= 75
        elif(self.fome>26 and self.fome<=50):
            vrfome= 50
        elif(self.fome>51 and self.fome<=75):
            vrfome= 25
        elif(self.fome>75):
            vrfome=0
        if(self.humor<=0):
            vrhumor = 100
            self.humor=0
        if(self.humor>=1 and self.humor<=25):
            vrhumor= 75
        elif(self.humor>26 and self.humor<=50):
            vrhumor= 50
        elif(self.humor>51 and self.humor<=75):
            vrhumor= 25
        elif(self.humor>75):
            vrhumor=0
        status=vrfome+vrhumor
        if(status==0):
            self.saude=100
            return 'Feliz'
        elif(status>=2 and status<=50):
            self.saude=80
            return 'Otimo'
        elif(status>=52 and status<=100):
            self.saude=60
            return 'Tranquilo'
        elif(status>=102 and status<=150):
            self.saude=40
            return 'Triste'
        elif(status>=152 and status<=198):
            self.saude=20
            return 'Chorando'
        elif(status>=200):
            self.saude=0
            return 'Morreu'

#Menu
def Menu():
    print("####### Tamagushi FIC ####### ")
    print("###### BORA BRINCAR?  #######")
    print("1 - Alterar o nome do bichinho")
    print("2 - Alimentar bichinho")
    print("3 - Dar remedio ao bichinho") #analisar
    print("4 - Alterar idade do bichinho")
    print("5 - Brincar com bichinho")
    print("6 - Veja os status do bichinho")
    print("0 - Sair")

#Iniciando MENU
os.system("cls")
Menu()

#Iniciando a bichinho padrao
bichinho=Tamagushi('NOVO',100,100,1,100)

#INCIANDO LOOP PROGRAMA
opc=input("Digirte a opcao: ")
while(opc!='0'):
    while ((opc=='0') or (opc=='1') or (opc=='2') or (opc=='3') or (opc=='4') or (opc=='5') or (opc=='6')):
        if(int(opc)==1):
            os.system('cls')
            novo=input("Digite o novo nome do seu bichinho: ")
            bichinho.altNome(novo)
            print("Nome alterado com sucesso!")
            os.system('pause')
            os.system('cls')
            Menu()
            opc=input("Digirte a opcao: ")
        elif (int(opc)==2):
            os.system('cls')
            print("Bichinho alimentado... ( *;* )")
            bichinho.altFome()
            bichinho.verHumor()
            os.system('pause')
            os.system('cls')
            Menu()
            opc=input("Digirte a opcao: ")
        elif (int(opc)==3):
            os.system('cls')
            print("Bichinho foi medicado!!! status de fome e humor almentados e saude reajustada...")
            bichinho.darRemedio()
            os.system('pause')
            os.system('cls')
            Menu()
            opc=input("Digirte a opcao: ")
        elif (int(opc)==4):
            os.system('cls')
            ida=input("Informe a nova idade do seu bichinho: ")
            if ida == "":
                print("Idade não alterada!")
            else:
                bichinho.altIdade(ida)
                print("Idade alterada com sucesso!")
            os.system('pause')
            os.system('cls')
            Menu()
            opc=input("Digirte a opcao: ")
        elif (int(opc)==5):
            os.system('cls')
            bichinho.brincar()
            bichinho.verHumor()
            print("Seu bicho brincou muito e seu Humor melhorou!!!")
            os.system('pause')
            os.system('cls')
            Menu()
            opc=input("Digirte a opcao: ")
        elif (int(opc)==6):
            os.system('cls')
            print(f"Nome do bichinho: {bichinho.nome} \nIdade: {bichinho.idade} ano \nFome: {bichinho.fome} \nSaude: {bichinho.saude} \nHumor: {bichinho.humor} \nStatus: {bichinho.verHumor()}" )
            os.system('pause')
            os.system('cls')
            Menu()
            opc=input("Digirte a opcao: ")
        elif (int(opc)==0):
            os.system('cls')
            break 
    else:
        print("Opcao invalida!")
        os.system('pause')
        os.system('cls')
        Menu()
        opc=input("Digirte a opcao: ")
else:
    os.system('cls')
    print("FIM PROGRAMA!!")








