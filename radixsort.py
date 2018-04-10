import numpy as np
import random
import matplotlib.pyplot as plt
import time

# Declaração de variáveis

tamanho=10
tempos=[]
tamanhos=[]

# Implementação da função de ordenação

def countingsort (vetor,divisor):
	contadores = []
	for i in range(0,10):	
		contadores.append(0)
	for i in range(0,len(vetor)):
		aux=(vetor[i]//divisor)%10
		contadores[aux]=contadores[aux]+1
	for i in range(1,10):
			contadores[i]=contadores[i]+contadores[i-1]
	x=len(vetor)
	vetor_aux = []
	for i in range(0,len(vetor)):
		vetor_aux.append(vetor[i])
		vetor[i]=0
	while (x>0):
		aux=(vetor_aux[x-1]//divisor)%10
		vetor[contadores[aux]-1]=vetor_aux[x-1]
		contadores[aux]=contadores[aux]-1
		x=x-1
	return vetor

def radixsort (vetor):
	divisor=1
	for _ in range (3):
		countingsort(vetor,divisor)
		divisor=divisor*10
	return vetor
	
while(tamanho<=10000):

	# Geração o Array aleatório
	vetor = []
	for _ in range(tamanho):
		vetor.append(random.randint(0, 999))
	print(vetor)
	# Execução da ordenação medindo o tempo gasto
	inicio = time.time()
	radixsort(vetor)
	fim = time.time()
	tempo=fim-inicio
	print(vetor)
	# Limpando o Array

	del vetor [ 00:len(vetor) ] 

	# Adição os dados aos arrays que servirão de base para a plotagem
	tamanhos.append(tamanho)
	tempos.append(tempo)
	
	# Incremento do tamanho do Array	

	if(tamanho>=1000):
		tamanho=tamanho+250
	else:
		tamanho=tamanho*10
	
# Plotagem do gráfico

plt.plot(tamanhos, tempos,'k')
plt.xlabel('tamanho do vetor')
plt.ylabel('tempo(s)')
plt.show()
