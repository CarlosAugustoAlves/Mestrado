package main

//QuickSort implementacao do algoritmo
func QuickSort(vetor []int, posicaoInicio int, posicaoFinal int) {

	if posicaoInicio < posicaoFinal {
		posicaoPivo := Particione(vetor, posicaoInicio, posicaoFinal)

		QuickSort(vetor, posicaoInicio, posicaoPivo-1)
		QuickSort(vetor, posicaoPivo+1, posicaoFinal)
	}
}

//Particione retorna a posição do pivô
func Particione(vetor []int, posicaoInicio int, posicaoFinal int) int {
	pivo := vetor[posicaoFinal]

	i := posicaoInicio - 1
	j := posicaoInicio

	for j < posicaoFinal {
		if vetor[j] > pivo {
			j++
		} else {
			i++
			vetor[i], vetor[j] = vetor[j], vetor[i]
			j++
		}
	}

	i++

	vetor[i], vetor[posicaoFinal] = vetor[posicaoFinal], vetor[i]

	return i
}
