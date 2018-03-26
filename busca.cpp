#include <bits/stdc++.h>

using namespace std;

int busca_sequencial(vector<int> vetor, int numero){
	int k=1,i=0;
	vetor.push_back(numero);
	while (numero!=vetor[i]) i++;
	if (i<(vetor.size()-1)) return i;
	else return -1;
}

int main() {
	int n, posicao, numero_pesquisado=1,i=0,auxiliar,alcance_rand;
	vector <int> vetor_aleatorio;
	cout << "Digite o tamanho do Vetor desejado:" <<endl;
	cin >> n;
    cout << "Digite o valor aleatório limite:" <<endl;
    cin >> alcance_rand;
	cout <<endl;
	for(int i=0;i<n;i++){
		vetor_aleatorio.push_back(rand() % alcance_rand);
	}
	while(numero_pesquisado>0){
		cout << "Digite o número que vc procura:" <<endl;
		cout << "(Caso queira encerrar o programa digite qualquer número negativo)" <<endl;
		cin >> numero_pesquisado;
		cout <<endl;
		if(numero_pesquisado<0) return 0;
		posicao = busca_sequencial(vetor_aleatorio, numero_pesquisado);
		if(posicao<0) cout << "Número não enconrado" <<endl;
		else {
			cout << "Número encontrado na posição: " << posicao <<" e movido para o inicio" <<endl<<endl;
			/*for(int i=0;i<n;i++){
				cout << i << " | " <<vetor_aleatorio[i] <<endl;
			}*/
			auxiliar=vetor_aleatorio.front();
			vetor_aleatorio.front()=vetor_aleatorio[posicao];
			for(i=posicao;i>0;i--){
				vetor_aleatorio[i]=vetor_aleatorio[i-1];
			}
			vetor_aleatorio[1]=auxiliar;
			for(int i=0;i<n;i++){
				cout << i << " | " << vetor_aleatorio[i] <<endl;
			}
		}		
	}
	return 0;
}
