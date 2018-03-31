import numpy as np
import random
import matplotlib.pyplot as plt
import time

tamanho=10
tempos=[]
tamanhos=[]
def insertionsort (vetor):
	for i in range(1,len(vetor)):
		aux = vetor[i]
		j = i-1
		while(j>=0) and aux < vetor[j]:
			vetor[j+1]=vetor[j]
			j=j-1
		vetor[j+1]=aux
	return vetor
	
while(tamanho<=7000):
	vetor = []
	for _ in range(tamanho):
		vetor.append(random.randint(0, 100))
	inicio = time.time()
	insertionsort(vetor)
	fim = time.time()
	tempo=fim-inicio
	print(tempo)
	del vetor [ 00:len(vetor) ] 
	tamanhos.append(tamanho)
	tempos.append(tempo)
	print(tamanho)
	if(tamanho>=1000):
		tamanho=tamanho+250
	else:
		tamanho=tamanho*10

plt.plot(tamanhos, tempos,'k')
plt.xlabel('tamanho do vetor')
plt.ylabel('tempo(s)')
plt.show()
