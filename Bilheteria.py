#By: WENDEL CABRAL

import os
os.system('cls')


qdvendido=0
despesa=200.00
valrec=0.00
lucro=0.00

ingresso=input('DIGITE O VALOR DO INGESSO: ')

while(float(ingresso)==5.00):
    qdvendido=120
    valrec=float(qdvendido)*float(ingresso)
    lucro=valrec-despesa
    break
while(float(ingresso)==4.50):
    qdvendido=146
    valrec=float(qdvendido)*float(ingresso)
    lucro=valrec-despesa
    break
while(float(ingresso)==4.00):
    qdvendido=172
    valrec=float(qdvendido)*float(ingresso)
    lucro=valrec-despesa
    break
while(float(ingresso)==3.50):
    qdvendido=198
    valrec=float(qdvendido)*float(ingresso)
    lucro=valrec-despesa
    break
while(float(ingresso)==3.00):
    qdvendido=224
    valrec=float(qdvendido)*float(ingresso)
    lucro=valrec-despesa
    break
while(float(ingresso)==2.50):
    qdvendido=250
    valrec=float(qdvendido)*float(ingresso)
    lucro=valrec-despesa
    break
while(float(ingresso)==2.00):
    qdvendido=276
    valrec=float(qdvendido)*float(ingresso)
    lucro=valrec-despesa
    break
while(float(ingresso)==1.50):
    qdvendido=302
    valrec=float(qdvendido)*float(ingresso)
    lucro=valrec-despesa
    break
while(float(ingresso)==1.00):
    qdvendido=328
    valrec=float(qdvendido)*float(ingresso)
    lucro=valrec-despesa
    break
while(float(ingresso)==0.50):
    qdvendido=354
    valrec=float(qdvendido)*float(ingresso)
    lucro=valrec-despesa
    break

print(f'Lucro do espetáculos: R${lucro}')
print(f'Valor total arrecado dos ingressos: R${valrec}')
print(f'Despesa total para o espetáculos: R${despesa}')
print(f'Numero de ingressos vendidos: {qdvendido}')
