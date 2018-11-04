package main

import (
	"testing"
)

/*
	A posição 0 está sendo ignorada para que o código reflita exatamente o conteúdo do artigo.
	Após a execucão do algoritmo o vetor deve ser um heap, pois o 100 assumirá a posição 1 e o 36 passará para a posição 3.
*/
func TestMaxHEAPFY(t *testing.T) {

	vetor := []int{0, 36, 19, 100, 17, 3, 25, 1, 2, 7}

	MaxHEAPFY(vetor, 9, 1)

	if !CheckIsHeap(vetor, 9) {
		t.Errorf("MAX-HEAPFY não funcionou")
	}
}

/*
	A posição 0 está sendo ignorada para que o código reflita exatamente o conteúdo do artigo.
	Após a execucão do algoritmo o vetor deve ser um heap
*/
func TestBuildMaxHEAP(t *testing.T) {

	vetor := []int{0, 17, 19, 2, 36, 25, 3, 1, 100, 7}

	BuildMaxHEAP(vetor, 9)

	if !CheckIsHeap(vetor, 9) {
		t.Errorf("BUILD-MAX-HEAPFY não funcionou")
	}
}

func TestHeapSort(t *testing.T) {

	vetor := []int{0, 17, 19, 2, 36, 25, 3, 1, 100, 7}

	HeapSort(vetor, 9)

	if !CheckOrdem(vetor, 1, 9) {
		t.Errorf("Heap-Sort não funcionou")
	}
}
