package main

//QuickSort implementacao do algoritmo
func QuickSort(vetor []int, posicaoInicio int, posicaoFinal int) {

	if posicaoInicio < posicaoFinal {
		posicaoPivo := Particione2(vetor, posicaoInicio, posicaoFinal)

		QuickSort(vetor, posicaoInicio, posicaoPivo-1)
		QuickSort(vetor, posicaoPivo+1, posicaoFinal)
	}
}

//Particione2 retorna a posição do pivô
func Particione2(v []int, p int, r int) int {
	var t int
	for i := p + 1; i <= r; i++ {
		if v[p] > v[i] {
			t = v[p]
			v[p] = v[i]
			v[i] = t
		}
	}

	return p
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
