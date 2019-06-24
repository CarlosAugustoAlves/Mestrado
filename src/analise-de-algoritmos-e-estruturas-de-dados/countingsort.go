package main

//CountingSort algoritmo de ordenação com tempo linear
func CountingSort(vetorEntrada []int, vetorSaida []int, numeroElementos int, maiorNumero int) {

	var vetorAuxiliar []int

	//Carregando vetor auxiliar
	for i := 0; i <= maiorNumero; i++ {
		vetorAuxiliar = append(vetorAuxiliar, 0)
	}

	//Preenche a quantidade de vezes que o elemento I aparece no vetor de entrada
	for i := 0; i < numeroElementos; i++ {
		vetorAuxiliar[vetorEntrada[i]] = vetorAuxiliar[vetorEntrada[i]] + 1
	}

	//acumulando os valores do vetor onde o elemento I será a soma dos anteriores
	//como resultado teremos a posição de cada elemento no vetor de saida
	for i := 1; i <= maiorNumero; i++ {
		vetorAuxiliar[i] = vetorAuxiliar[i] + vetorAuxiliar[i-1]
	}

	//Preenchendo o vetor de saída com os elementos
	//o algoritmo é estável porque mantém a ordem dos elementos da entrada
	for i := (numeroElementos - 1); i >= 0; i-- {
		vetorSaida[vetorAuxiliar[vetorEntrada[i]]-1] = vetorEntrada[i]
		vetorAuxiliar[vetorEntrada[i]] = vetorAuxiliar[vetorEntrada[i]] - 1
	}
}
