package main

import (
	"testing"
)

/*
	A posição 0 está sendo ignorada para que o código reflita exatmente o conteúdo descrito
	A após a execusão o heap deve estar correto. Onde o 100 assumirá a posição 1
	e o 36 passará para a posição 3
*/
func TestMaxHEAPFY(t *testing.T) {

	vetor := []int{0, 36, 19, 100, 17, 3, 25, 1, 2, 7}

	MaxHEAPFY(vetor, 9, 1)

	if vetor[1] != 100 || vetor[3] != 36 {
		t.Errorf("Vetor não esta no formato heap")
	}
}
