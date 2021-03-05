#By: WENDEL CABRAL

import timeit

lista = [0]*1000000

for i in range(len(lista)):
    lista[i] = i*3

def buscas(lista, chave):
    for i in range(len(lista)):
        if lista[i] == chave:
            print(i)
            return i
    return -1



inicio = timeit.default_timer()
print(buscas(lista, 999999))
fim = timeit.default_timer()

print(' %f' % (fim - inicio))