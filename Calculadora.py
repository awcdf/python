#By: WENDEL CABRAL

#IMPORTS
from tkinter import *
import keyboard
import string
from threading import *
import math

#Criando TK Travando Janela
app = Tk()
app.title("Calculadora")
app.resizable(width=False, height=False)

#CRIANDO VISOR (TELA)
fVisor = Frame(app)
fVisor.pack(side=TOP)
lbVisor = Label(fVisor,text="",width = 28,relief=RIDGE, font="Arial 12 bold", fg="blue")
lbVisor.pack(fill=Y)
lbVisor2 = Label(fVisor,text="",width = 28,relief=RIDGE, font="Arial 12 bold", fg="red")
lbVisor2.pack(fill=Y)


#CRIANDO BOTOES (TAMANHOS)
fButton = Frame(app)
fButton.pack(side=TOP)
bt0 = Button(fButton,text="0" ,bd=5,padx=1,pady=1, width=8, height=2)
bt1 = Button(fButton,text="1",bd=5,padx=1,pady=1, width=8, height=2)
bt2 = Button(fButton,text="2",bd=5,padx=1,pady=1, width=8, height=2)
bt3 = Button(fButton,text="3",bd=5,padx=1,pady=1, width=8, height=2)
bt4 = Button(fButton,text="4",bd=5,padx=1,pady=1, width=8, height=2)
bt5 = Button(fButton,text="5",bd=5,padx=1,pady=1, width=8, height=2)
bt6 = Button(fButton,text="6",bd=5,padx=1,pady=1, width=8, height=2)
bt7 = Button(fButton,text="7",bd=5,padx=1,pady=1, width=8, height=2)
bt8 = Button(fButton,text="8",bd=5,padx=1,pady=1, width=8, height=2)
bt9 = Button(fButton,text="9",bd=5,padx=1,pady=1, width=8, height=2)
btSoma = Button(fButton,text="+",bd=5,padx=1,pady=1, width=8, height=2)
btSubi = Button(fButton,text="-",bd=5,padx=1,pady=1, width=8, height=2)
btMult = Button(fButton,text="x",bd=5,padx=1,pady=1, width=8, height=2)
btDiv = Button(fButton,text="/",bd=5,padx=1,pady=1, width=8, height=2)
btIgual = Button(fButton,text="=",bd=5,padx=1,pady=1, width=8, height=2)
btPercert = Button(fButton,text="%",bd=5,padx=1,pady=1, width=8, height=2)
btPonto = Button(fButton,text=".",bd=5,padx=1,pady=1, width=8, height=2)
btLimpa = Button(fButton,text="C",bd=5,padx=1,pady=1, width=8, height=2)
btApaga = Button(fButton,text="<-",bd=5,padx=1,pady=1, width=8, height=2)
btRaiz = Button(fButton,text="√x",bd=5,padx=1,pady=1, width=8, height=2)
btPoten = Button(fButton,text="x^y",bd=5,padx=1,pady=1, width=8, height=2)
btFseno = Button(fButton,text="sin",bd=5,padx=1,pady=1, width=8, height=2)
btFcose = Button(fButton,text="cos",bd=5,padx=1,pady=1, width=8, height=2)
btFtang = Button(fButton,text="tan",bd=5,padx=1,pady=1, width=8, height=2)

#Organizando botoes com linhas e colunas no GRID.
bt7.grid(row=0,column=0)
bt8.grid(row=0,column=1)
bt9.grid(row=0,column=2)
btApaga.grid(row=0,column=3)
bt4.grid(row=1,column=0)
bt5.grid(row=1,column=1)
bt6.grid(row=1,column=2)
btSoma.grid(row=1,column=3)
bt1.grid(row=2,column=0)
bt2.grid(row=2,column=1)
bt3.grid(row=2,column=2)
btSubi.grid(row=2,column=3)
bt0.grid(row=3,column=0)
btPercert.grid(row=3,column=2)
btPonto.grid(row=3,column=1)
btDiv.grid(row=3,column=3)
btPoten.grid(row=4,column=0)
btFcose.grid(row=4,column=1)
btFseno.grid(row=4,column=2)
btFtang.grid(row=4,column=3)
btRaiz.grid(row=5,column=0)
btMult.grid(row=5,column=1)
btLimpa.grid(row=5,column=2)
btIgual.grid(row=5, column=3)

#VARIAVEL ONDE VAI FICAR O CALCULO
calc = ""
temp = ""
op = ""

#ENTRADA DE DADOS
def entrada(rec):
    global calc,lbVisor,temp,op,lbVisor2
    if len(calc) > 1 and calc[1].isdigit():
        calc = calc.lstrip('0')
        lbVisor.config(text=calc)
    #ENTRADA VIA BOTAO
    try:
        if rec.widget==bt0:
            calc+="0"
            lbVisor.config(text=calc)
        elif rec.widget==bt1:
            calc+="1"
            lbVisor.config(text=calc)        
        elif rec.widget==bt2:
            calc+="2"
            lbVisor.config(text=calc)
        elif rec.widget==bt3:
            calc+="3"
            lbVisor.config(text=calc)
        elif rec.widget==bt4:
            calc+="4"
            lbVisor.config(text=calc)
        elif rec.widget==bt5:
            calc+="5"
            lbVisor.config(text=calc)
        elif rec.widget==bt6:
            calc+="6"
            lbVisor.config(text=calc)
        elif rec.widget==bt7:
            calc+="7"
            lbVisor.config(text=calc)
        elif rec.widget==bt8:
            calc+="8"
            lbVisor.config(text=calc)
        elif rec.widget==bt9:
            calc+="9"
            lbVisor.config(text=calc)
        elif rec.widget==btPonto:
            calc+="."
            lbVisor.config(text=calc)
        elif rec.widget==btPercert:
            i=0
            pos=0
            while i < len(calc):
                l = calc[i]
                if (l=="+" or (l=="-") or (l=="*") or (l=="/")):
                    pos = i
                i+=1
            op=calc[pos]
            i=0
            nCalc=""
            while i < pos:
                l = calc[i]
                nCalc+=l
                i+=1
            i=0
            pos=pos+1
            rest=""
            while pos < len(calc):
                l = calc[pos]
                rest+=l
                pos+=1
            res = eval(nCalc)  
            if op == "+":
                    rs=float(res)/100*float(rest)
                    calc=float(res)+rs
            elif op == "-":
                    rs=float(res)/100*float(rest)
                    calc=float(res)-rs
            elif op == "*":
                    rs=float(res)/100*float(rest)
                    calc=rs
            elif op == "/":
                    rs=float(res)/100*float(rest)
                    calc=float(res)/rs
            calc=str(calc)
            lbVisor2.config(text=calc)
        elif rec.widget==btSoma:
            calc+="+"
            lbVisor.config(text=calc)
        elif rec.widget==btSubi:
            calc+="-"
            lbVisor.config(text=calc)
        elif rec.widget==btMult:
            calc+="*"
            lbVisor.config(text=calc)
        elif rec.widget==btDiv:
            calc+="/"
            lbVisor.config(text=calc)
        elif rec.widget==btRaiz:
            try:
                res = eval(calc)  
                raiz = math.sqrt(res)
                calc = str(raiz)
                lbVisor2.config(text=calc)
            except:
                lbVisor2.config(text="erro!")
        elif rec.widget==btPoten:
            res = eval(calc) 
            if temp == "":
                temp=res
                temp=str(temp)
                calc=""
                lbVisor.config(text=calc)
                lbVisor2.config(text=temp+"^")
            else:
                n1=float(temp)
                n2=float(res)
                calc=(n1 ** n2)
                temp=""
                calc= str(calc)
                lbVisor.config(text=str(res))
                lbVisor2.config(text=calc)
                teste=(2.1 ** 5.1)
                print(teste)
        elif rec.widget==btFseno:
            try:
                res = eval(calc)
                calc= str(res)
                lbVisor.config(text= calc)        
                res=float(res)
                rd = math.radians(res)
                seno= math.sin(rd)
                calc= str(seno)
                lbVisor2.config(text= calc)  
            except:
                lbVisor2.config(text="erro!")
        elif rec.widget==btFcose:
            try:
                res = eval(calc)
                calc= str(res)
                lbVisor.config(text= calc)        
                res=float(res)
                rd = math.radians(res)
                cose= math.cos(rd)
                calc= str(cose)
                lbVisor2.config(text= calc)  
            except:
                lbVisor2.config(text="erro!")
        elif rec.widget==btFtang:
            try:
                res = eval(calc)
                calc= str(res)
                lbVisor.config(text= calc)        
                res=float(res)
                rd = math.radians(res)
                tam= math.tan(rd)
                calc= str(tam)
                lbVisor2.config(text= calc)  
            except:
                lbVisor2.config(text="erro!")
        elif rec.widget==btLimpa:
            calc = ""
            lbVisor.config(text=calc)
            lbVisor2.config(text=calc)
        elif rec.widget==btApaga:
            calc = calc[:-1]
            lbVisor.config(text=calc)
        elif rec.widget==btIgual:
            try:
                res = eval(calc)  
                calc= str(res)
                lbVisor2.config(text= calc)       
            except:
                lbVisor2.config(text="erro!")
    #ENTRA VIA TELCADO 
    except:
        if rec=="0":
            calc+="0"
            lbVisor.config(text=calc)
        elif rec=="1":
            calc+="1"
            lbVisor.config(text=calc)
        elif rec=="2":
            calc+="2"
            lbVisor.config(text=calc)
        elif rec=="3":
            calc+="3"
            lbVisor.config(text=calc)
        elif rec=="4":
            calc+="4"
            lbVisor.config(text=calc)
        elif rec=="5":
            calc+="5"
            lbVisor.config(text=calc)
        elif rec=="6":
            calc+="6"
            lbVisor.config(text=calc)
        elif rec=="7":
            calc+="7"
            lbVisor.config(text=calc)
        elif rec=="8":
            calc+="8"
            lbVisor.config(text=calc)
        elif rec=="9":
            calc+="9"
            lbVisor.config(text=calc)
        elif rec==".":
            calc+="."
            lbVisor.config(text=calc)
        elif rec=="shift+5":
            i=0
            pos=0
            while i < len(calc):
                l = calc[i]
                if (l=="+" or (l=="-") or (l=="*") or (l=="/")):
                    pos = i
                i+=1
            op=calc[pos]
            i=0
            nCalc=""
            while i < pos:
                l = calc[i]
                nCalc+=l
                i+=1
            i=0
            pos=pos+1
            rest=""
            while pos < len(calc):
                l = calc[pos]
                rest+=l
                pos+=1
            res = eval(nCalc)  
            if op == "+":
                    rs=float(res)/100*float(rest)
                    calc=float(res)+rs
            elif op == "-":
                    rs=float(res)/100*float(rest)
                    calc=float(res)-rs
            elif op == "*":
                    rs=float(res)/100*float(rest)
                    calc=rs
            elif op == "/":
                    rs=float(res)/100*float(rest)
                    calc=float(res)/rs
            calc=str(calc)
            lbVisor2.config(text=calc)
        elif rec=="+":
            calc+="+"
            lbVisor.config(text=calc)
        elif rec=="-":
            calc+="-"
            lbVisor.config(text=calc)
        elif rec=="*":
            calc+="*"
            lbVisor.config(text=calc)
        elif rec=="/":
            calc+="/"
            lbVisor.config(text=calc)
        elif rec=="esc":
            calc= ""
            lbVisor.config(text=calc)
            lbVisor2.config(text=calc)
        elif rec=="backspace":
            calc = calc[:-1]
            lbVisor.config(text=calc)
        elif rec=="enter":
            try:
                res = eval(calc)  
                calc= str(res)
                lbVisor2.config(text= calc)       
            except:
                lbVisor2.config(text="erro!")


#Binds BOTAO
bt0.bind("<Button-1>",entrada)
bt1.bind("<Button-1>",entrada)
bt2.bind("<Button-1>",entrada)
bt3.bind("<Button-1>",entrada)
bt4.bind("<Button-1>",entrada)
bt5.bind("<Button-1>",entrada)
bt6.bind("<Button-1>",entrada)
bt7.bind("<Button-1>",entrada)
bt8.bind("<Button-1>",entrada)
bt9.bind("<Button-1>",entrada)
btApaga.bind("<Button-1>",entrada)
btLimpa.bind("<Button-1>",entrada)
btPonto.bind("<Button-1>",entrada)
btPercert.bind("<Button-1>",entrada)
btIgual.bind("<Button-1>",entrada)
btSoma.bind("<Button-1>",entrada)
btSubi.bind("<Button-1>",entrada)
btDiv.bind("<Button-1>",entrada)
btMult.bind("<Button-1>",entrada)
btPoten.bind("<Button-1>",entrada)
btFcose.bind("<Button-1>",entrada)
btFseno.bind("<Button-1>",entrada)
btFtang.bind("<Button-1>",entrada)
btRaiz.bind("<Button-1>",entrada)

#MAPEAMENTO DE TECLAS
listTeclas = ["1","2","3","4","5","6","7","8","9","0",".",",","*","+","-","/","enter","esc","backspace","shift+5"]
teclas = list(listTeclas)

#FUNCAO DE ENTRADA DE TECLAS
def listen(tecla):
    while True:
        keyboard.wait(tecla)
        entrada(tecla)
        print("- Tecla pressionada: ",tecla)
        
threads = [Thread(target=listen, kwargs={"tecla":tecla}) for tecla in teclas]

for thread in threads:
    thread.start()


#INICIALIZANDO CALCULADORA
app.mainloop()
