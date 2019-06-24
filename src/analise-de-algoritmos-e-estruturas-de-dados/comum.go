package main

//CheckOrdem verifica se o vetor está em ordem crescente
func CheckOrdem(vetor []int, posicao int, posicaoFinal int) bool {

	if posicao+1 <= posicaoFinal {
		if vetor[posicao] <= vetor[posicao+1] {
			posicao++
			return CheckOrdem(vetor, posicao, posicaoFinal)
		}

		return false
	}

	return true
}
