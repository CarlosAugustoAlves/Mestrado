package main

import (
	"fmt"
	"math"
)

func MaxHEAPFY(vetor []int, numeroElementos int, posicaoItem int) {
	posicaoFilhoEsquerdo := posicaoItem * 2
	posicaoFilhoDireito := ((posicaoItem * 2) + 1)
	var posicaoItemMaior int

	if posicaoFilhoEsquerdo <= numeroElementos && vetor[posicaoFilhoEsquerdo] > vetor[posicaoItem] {
		posicaoItemMaior = posicaoFilhoEsquerdo
	} else {
		posicaoItemMaior = posicaoItem
	}

	if posicaoFilhoDireito <= numeroElementos && vetor[posicaoFilhoDireito] > vetor[posicaoItemMaior] {

		posicaoItemMaior = posicaoFilhoDireito
	}

	if posicaoItem != posicaoItemMaior {

		//Invertendo os valores no vetor
		vetor[posicaoItem], vetor[posicaoItemMaior] = vetor[posicaoItemMaior], vetor[posicaoItem]

		MaxHEAPFY(vetor, numeroElementos, posicaoItemMaior)
	}
}

func BuildMaxHEAP(vetor []int, numeroElementos int) {

	for indexElemento := int(math.Floor(float64(numeroElementos / 2))); indexElemento >= 1; indexElemento-- {
		MaxHEAPFY(vetor, numeroElementos, indexElemento)
	}
}

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

func HeapSort(vetor []int, numeroElementos int) []int {

	var vetorOrdenado []int

	for numeroElementos > 1 {
		BuildMaxHEAP(vetor, numeroElementos)
		vetorOrdenado = append(vetorOrdenado, vetor[1])
		vetor = append(vetor[:1], vetor[2:]...)
		numeroElementos--
	}

	vetorOrdenado = append(vetorOrdenado, vetor[1])

	return vetorOrdenado
}

func main() {
	fmt.Println("Hello Max Heap")
}
