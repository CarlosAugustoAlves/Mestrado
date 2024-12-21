package main

import (
	"testing"
)

func TestCountingSort(t *testing.T) {

	numeroElementos := 7
	vetorEntrada := []int{4, 3, 4, 3, 1, 0, 3}
	vetorSaida := make([]int, numeroElementos)
	maiorNumero := 4

	CountingSort(vetorEntrada, vetorSaida, numeroElementos, maiorNumero)

	if !CheckOrdem(vetorSaida, 0, numeroElementos-1) {
		t.Errorf("Counting-Sort não funcionou")
	}
}
