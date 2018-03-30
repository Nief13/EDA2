import matplotlib.pyplot as plt
from random import randint
import timeit


def particiona(array, inicio, fim):
    pivo = array[fim]
    esquerda = inicio - 1
    direita = fim

    feito = 0
    while not feito:

        while not feito:
            esquerda = esquerda + 1

            if esquerda == direita:
                feito = 1
                break

            if array[esquerda] > pivo:
                array[direita] = array[esquerda]
                break

        while not feito:
            direita = direita-1

            if direita == esquerda:
                feito = 1
                break

            if array[direita] < pivo:
                array[esquerda] = array[direita]
                break

    array[direita] = pivo
    return direita


def quickSort(array, inicio, fim):
    if inicio < fim:
        pivo = particiona(array, inicio, fim)
        quickSort(array, inicio, pivo - 1)
        quickSort(array, pivo + 1, fim)
    else:
        return array

def gerarArrayAleatorio(inicio, fim, tamanho):
    array = []
    for i in range(0, tamanho):
        array.append(randint(inicio, fim))
    return array

tamanhosArray = []
tempoGasto = []

for i in range(1, 10):
    x = i * 100000
    print x
    tamanhosArray.append(x)
    array = gerarArrayAleatorio(0, x, x)
    
    tempo = timeit.timeit('quickSort(array, 0, len(array) - 1)', setup='from __main__ import quickSort, array', number=1)
    tempoGasto.append(tempo)

plt.plot(tamanhosArray, tempoGasto)
plt.xlabel('tamanho do vetor')
plt.ylabel('tempo(s)')
plt.show()