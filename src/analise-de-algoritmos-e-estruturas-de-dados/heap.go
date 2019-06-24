package main

import (
	"fmt"
	"math"
)

//MaxHEAPFY função que ajusta o heap a partir do elemento "posicaoItem"
func MaxHEAPFY(vetor []int, numeroElementos int, posicaoItem int) {
	posicaoFilhoEsquerdo := posicaoItem * 2
	posicaoFilhoDireito := ((posicaoItem * 2) + 1)
	var posicaoItemMaior int

	if posicaoFilhoEsquerdo <= numeroElementos && vetor[posicaoFilhoEsquerdo] > vetor[posicaoItem] {
		posicaoItemMaior = posicaoFilhoEsquerdo
	} else {
		posicaoItemMaior = posicaoItem
	}

	if posicaoFilhoDireito <= numeroElementos &&
		vetor[posicaoFilhoDireito] > vetor[posicaoItemMaior] {

		posicaoItemMaior = posicaoFilhoDireito
	}

	if posicaoItem != posicaoItemMaior {

		//Invertendo os valores no vetor
		vetor[posicaoItem], vetor[posicaoItemMaior] = vetor[posicaoItemMaior], vetor[posicaoItem]

		MaxHEAPFY(vetor, numeroElementos, posicaoItemMaior)
	}
}

//BuildMaxHEAP função que torna o vetor um Max Heap
func BuildMaxHEAP(vetor []int, numeroElementos int) {

	for indexElemento := int(math.Floor(float64(numeroElementos / 2))); indexElemento >= 1; indexElemento-- {
		MaxHEAPFY(vetor, numeroElementos, indexElemento)
	}
}

//CheckIsHeap veriricar se o vetor é um heap
func CheckIsHeap(vetor []int, numeroElementosHeap int) bool {

	indexItemVerificacao := 1

	for (indexItemVerificacao * 2) <= numeroElementosHeap {
		indexFilhoEsquerdo := indexItemVerificacao * 2

		if vetor[indexItemVerificacao] < vetor[indexFilhoEsquerdo] {
			return false
		}

		indexFilhoDireito := indexFilhoEsquerdo + 1

		if numeroElementosHeap >= indexFilhoDireito && vetor[indexItemVerificacao] < vetor[indexFilhoDireito] {
			return false
		}

		indexItemVerificacao++
	}

	return true
}

//HeapSort ordena um vetor utilizando o heap
func HeapSort(vetor []int, numeroElementos int) {

	BuildMaxHEAP(vetor, numeroElementos)

	var numeroElementosAuxiliar int
	numeroElementosAuxiliar = numeroElementos

	for numeroElementos > 1 {
		//Invertendo os valores no vetor
		vetor[1], vetor[numeroElementos] = vetor[numeroElementos], vetor[1]

		numeroElementosAuxiliar--

		MaxHEAPFY(vetor, numeroElementosAuxiliar, 1)

		numeroElementos--
	}
}

func main() {
	fmt.Println("Hello Max Heap")
}
