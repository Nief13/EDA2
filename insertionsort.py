import numpy as np
import random
import matplotlib as plt

tamanho=10
tempos=[]
tamanhos=[]
#def quicksort (vetor):
	
#	return tempo;
	
while(tamanho<=100000):
	vetor = []
	for _ in range(tamanho):
		vetor.append(random.randint(0, 100))
	#tempo=quicksort(vetor)
	del vetor [ 00:len(vetor) ] 
	#tamanhos.append(tamanho)
	#tempos.append(tempo)
	print(tamanho)
	if(tamanho>=1000):
		tamanho=tamanho+1000
	else:
		tamanho=tamanho*10

#plt.plot(tamanhos, tempos, 'k', color='red')
#plt.axis([10, 100000, 0, 11])
#plt.title("Tempo de execução da ordenação em função do tamanho do Array")

#plt.grid(True)
#plt.xlabel("Tamanho do array")
#plt.ylabel("Tempo")
#plt.show()


