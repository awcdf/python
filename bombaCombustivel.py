#By: WENDEL CABRAL

#IMPORTS
import os

#CLASS
class BombaCombustível:
    #INICIALIZACAO
    def __init__(self,numeroBomba,tipoCombustivel,valorLitro,quantidadeCombustivel = 0):
        self.numeroBomba=numeroBomba
        self.tipoCombustivel=tipoCombustivel 
        self.valorLitro=valorLitro 
        self.quantidadeCombustivel=quantidadeCombustivel 




#FUNCOES    
    def abastecerPorValor(self, valor):
        total=float(valor)/self.valorLitro
        self.AlterarQuantidadeCombustivel(int(total))
        return str(total)

    def abastecerPorLitro(self, litros):
        total=self.valorLitro*float(litros)
        self.AlterarQuantidadeCombustivel(int(litros))
        return str(total)
    
    def alterarValor(self, valor):
        self.valorLitro=valor

    def alterarCombustivel(self,nome):
        self.tipoCombustivel=nome
    
    def AlterarQuantidadeCombustivel(self,qtd):
        self.quantidadeCombustivel-=qtd  
   
    def AbasteceBombaCombustivel(self,qtd):
        self.quantidadeCombustivel+=qtd

#Menu
def Menu():
    print("####### POSTO DE GASOLINA FIC####### ")
    print("#########  FIC E ABASTECA! #########")
    print("Antes de abstecer vamos adcionar")
    print("1 - Abastecer veiculo por valor $")
    print("2 - Abastecer veiculo por quandtidade de litros")
    print("3 - Altera valor do combustivel")
    print("4 - Alterar tipo de combustivel")
    print("5 - Recarrega Bomba de Combustivel")
    print("6 - Relatorio de Bomba")
    print("0 - Sair")

#Iniciando MENU
os.system("cls")
Menu()

#Iniciando a bomba
bomba=BombaCombustível(1,"Gasolina", 4.50, 100)

#INCIANDO LOOP PROGRAMA
opc=input("Digirte a opcao: ")
while(opc!='0'):
    while ((opc=='0') or (opc=='1') or (opc=='2') or (opc=='3') or (opc=='4') or (opc=='5') or (opc=='6')):
        if(int(opc)==1):
            os.system('cls')
            valor=input("Informe o valor em reais que deseja abastecer: R$")
            tCombustivel=bomba.quantidadeCombustivel*bomba.valorLitro
            if tCombustivel < float(valor):
                print("Não existe combustivel suficiente")
            else:
                litros=bomba.abastecerPorValor(valor)
                print(f"Total em litros abastecido {litros}")
            os.system('pause')
            os.system('cls')
            Menu()
            opc=input("Digirte a opcao: ")

        elif (int(opc)==2):
            os.system('cls')
            litros=input("Informe a quantidade de litros que deseja abastecer: ")
            tCombustivel=bomba.quantidadeCombustivel
            if tCombustivel < float(litros):
                print("Não existe combustivel suficiente")
            else:
                valor=bomba.abastecerPorLitro(litros)
                print(f"O valor total a ser pago é: R$ {valor}")
            os.system('pause')
            os.system('cls')
            Menu()
            opc=input("Digirte a opcao: ")
        elif (int(opc)==3):
            os.system('cls')
            valor=input("Informe o novo valor do combustivel: ")
            bomba.alterarValor(float(valor))
            print("Valor alterado!")
            os.system('pause')
            os.system('cls')
            Menu()
            opc=input("Digirte a opcao: ")

        elif (int(opc)==4):
            os.system('cls')
            nome=input("Informe qual tipo de combustivel deseja adcionar a esta bomba: ")
            bomba.alterarCombustivel(nome)
            print("Tipo de combustivel alterado!")
            os.system('pause')
            os.system('cls')
            Menu()
            opc=input("Digirte a opcao: ")
            
        elif (int(opc)==5):
            os.system('cls')
            rec=input("Informa a quantidade em litros que a bomba recebera: ")
            bomba.AbasteceBombaCombustivel(int(rec))
            print("Bomba Recarregada!")
            os.system('pause')
            os.system('cls')
            Menu()
            opc=input("Digirte a opcao: ")
        elif (int(opc)==6):
            os.system('cls')
            print(f"Bomba de Nº {bomba.numeroBomba}, com combustivel a {bomba.tipoCombustivel} e quantidade {bomba.quantidadeCombustivel} litros, esta com preco R${bomba.valorLitro} por litro")
            os.system('pause')
            os.system('cls')
            Menu()
            opc=input("Digirte a opcao: ")
        elif (int(opc)==0):
            break  
    else:
        print("Opcao invalida!")
        os.system('pause')
        os.system('cls')
        Menu()
        opc=input("Digirte a opcao: ")
else:
    print("FIM PROGRAMA!!")
    


            
    
        

        
            
    




