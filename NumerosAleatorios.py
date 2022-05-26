import random
import time


print("Numeros Aleatorios de 1 a 50")
numeroAleatorio =list(range(1,50))

random.shuffle(numeroAleatorio)
print("\n", numeroAleatorio)



print("\nOrdenando os Numeros pelo metodo Bubblesort\n")

def shortBubbleSort(numeroAleatorio):
    trocas = True
    passnum = len(numeroAleatorio)-1
    while passnum > 0 and trocas:
       trocas = False
       for i in range(passnum):
           if numeroAleatorio[i]>numeroAleatorio[i+1]:
               trocas = True
               temp = numeroAleatorio[i]
               numeroAleatorio[i] = numeroAleatorio[i+1]
               numeroAleatorio[i+1] = temp
       passnum = passnum-1

lista = numeroAleatorio
shortBubbleSort(numeroAleatorio)
print(lista)



print("\nOrdenando  os numeros pelo metodo quicksort\n")



def quickSort(lista):
   quickSortHelper(lista,0,len(lista)-1)

def quickSortHelper(lista,primeiro,ultimo):
   if primeiro<ultimo:

       splitpoint = partition(lista,primeiro,ultimo)

       quickSortHelper(lista,primeiro,splitpoint-1)
       quickSortHelper(lista,splitpoint+1,ultimo)


def partition(lista,primeiro,ultimo):
   pivotvalue = lista[primeiro]

   marcaEsquerda = primeiro+1
   marcaDireita = ultimo

   done = False
   while not done:

       while marcaEsquerda <= marcaDireita and lista[marcaEsquerda] <= pivotvalue:
           marcaEsquerda = marcaEsquerda + 1

       while lista[marcaDireita] >= pivotvalue and marcaDireita >= marcaEsquerda:
           marcaDireita = marcaDireita -1

       if marcaDireita < marcaEsquerda:
           done = True
       else:
           temp = lista[marcaEsquerda]
           lista[marcaEsquerda] = lista[marcaDireita]
           lista[marcaDireita] = temp

   temp = lista[primeiro]
   lista[primeiro] = lista[marcaDireita]
   lista[marcaDireita] = temp


   return marcaDireita


lista = numeroAleatorio
quickSort(lista)
print(lista)


antes = time.time()
shortBubbleSort(numeroAleatorio)
depois = time.time()

total = (depois - antes)*1000 

print("\nbubbleSort o Tempo de Execucao em MS: %0.2f" % total)




antes = time.time()
quickSort(lista)
depois = time.time()

totalemMs =(depois - antes)*1000

print("QuickSort o Tempo de Execucao em MS : %0.2f" % totalemMs)

