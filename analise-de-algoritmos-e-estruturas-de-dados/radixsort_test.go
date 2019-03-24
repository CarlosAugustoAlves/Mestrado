package main

import (
	"testing"
)

func TestRadixSort(t *testing.T) {

	vetor := []int{491, 348, 736, 653, 231, 492, 785, 111}

	RadixSort(vetor, 8, 3)

	if !CheckOrdem(vetor, 0, 7) {
		t.Errorf("Radix-Sort não funcionou")
	}
}
