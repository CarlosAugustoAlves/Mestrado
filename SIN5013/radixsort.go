package main

import "strconv"

//RadixSort algoritmo de ordenação linear baseada  na quantidade de digitos dos elementos do vetor
func RadixSort(vetor []int, numeroElementos int, numeroDigito int) {

	vetorDigito := make([]int, numeroElementos)

	for i := (numeroDigito - 1); i >= 0; i-- {

		preencherVetorDigito(vetor, vetorDigito, numeroElementos, i) //análise assintótica: numeroDigito*Theta(n)

		var maiorNumero int
		maiorNumero = obterMaximo(vetorDigito, 0, numeroElementos, maiorNumero) //análise assintótica: numeroDigito*Theta(n)

		vetorInfoPosicaoTrocada := ordenarLinear(vetorDigito, numeroElementos, maiorNumero) //análise assintótica: numeroDigito*Theta(n)

		vetorAuxiliar := make([]int, numeroElementos)
		copy(vetorAuxiliar, vetor) //análise assintótica: numeroDigito*Theta(n)

		for j := 0; j < numeroElementos; j++ { //análise assintótica: numeroDigito*Theta(n)
			vetor[vetorInfoPosicaoTrocada[j]] = vetorAuxiliar[j]
		}
	}
}

func preencherVetorDigito(vetor []int, vetorDigito []int, numeroElementos int, posicaoDigito int) {

	for i := 0; i < numeroElementos; i++ {
		valorDigitoString := strconv.Itoa(vetor[i])                          //converte o número para string
		valorDigitoString = string([]rune(valorDigitoString)[posicaoDigito]) //obtem caracter por posição
		valorDigito, err := strconv.Atoi(valorDigitoString)                  //convertendo a caracter para int

		if err != nil {
			panic(err)
		}

		vetorDigito[i] = valorDigito
	}
}

func obterMaximo(vetor []int, posicaoInicio int, posicaoFim int, valorMaximo int) int {

	if posicaoInicio < posicaoFim {

		if valorMaximo < vetor[posicaoInicio] {
			valorMaximo = vetor[posicaoInicio]
		}

		posicaoInicio++
		valorMaximo = obterMaximo(vetor, posicaoInicio, posicaoFim, valorMaximo)
	}

	return valorMaximo
}

func ordenarLinear(vetorEntrada []int, numeroElementos int, maiorNumero int) []int {

	vetorInfoPosicaoTrocada := make([]int, numeroElementos)
	var vetorAuxiliar []int

	//Carregando vetor auxiliar
	for i := 0; i <= maiorNumero; i++ {
		vetorAuxiliar = append(vetorAuxiliar, 0)
	}

	//Preencher a quantidade de vezes que o elemento I aparece no vetor de entrada
	for i := 0; i < numeroElementos; i++ {
		vetorAuxiliar[vetorEntrada[i]] = vetorAuxiliar[vetorEntrada[i]] + 1
	}

	//acumulando os valores do vetor onde elemelento I será a soma dos anteriores
	//como resultado teremos a posição de cada elemenot no vetor de saida
	for i := 1; i <= maiorNumero; i++ {
		vetorAuxiliar[i] = vetorAuxiliar[i] + vetorAuxiliar[i-1]
	}

	//Preenchendo o vetor de saída com os itens na ordem do vetor de entrada,
	//isto faz com que o altoritmo seja estável
	for i := (numeroElementos - 1); i >= 0; i-- {

		vetorInfoPosicaoTrocada[i] = vetorAuxiliar[vetorEntrada[i]] - 1
		vetorAuxiliar[vetorEntrada[i]] = vetorAuxiliar[vetorEntrada[i]] - 1
	}

	return vetorInfoPosicaoTrocada
}
