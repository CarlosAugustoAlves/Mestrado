package main

import (
	"testing"
)

func TestQuickSort(t *testing.T) {

	posicaoInicio := 0
	posicaoFinal := 5
	vetor := []int{47, 22, 40, 56, 34, 42}

	QuickSort(vetor, posicaoInicio, posicaoFinal)

	if !CheckOrdem(vetor, posicaoInicio, posicaoFinal) {
		t.Errorf("Heap-Sort não funcionou")
	}
}

func TestParticione(t *testing.T) {

	posicaoInicio := 0
	posicaoFinal := 5
	vetor := []int{47, 22, 40, 56, 34, 42}

	posicaoPivo := Particione(vetor, posicaoInicio, posicaoFinal)

	if !CheckParticioneLadoDireito(vetor, posicaoPivo, posicaoFinal) ||
		!CheckParticioneLadoEsquerdo(vetor, posicaoPivo, posicaoInicio) {
		t.Errorf("Particione não funcionou")
	}
}

func CheckParticioneLadoDireito(vetor []int, posicaoPivo int, posicaoFinal int) bool {

	if posicaoPivo < posicaoFinal {
		if vetor[posicaoPivo] < vetor[posicaoFinal] {
			posicaoFinal--
			return CheckParticioneLadoDireito(vetor, posicaoPivo, posicaoFinal)
		}

		return false
	}

	return true
}

func CheckParticioneLadoEsquerdo(vetor []int, posicaoPivo int, posicaoInicio int) bool {

	if posicaoPivo > posicaoInicio {
		if vetor[posicaoPivo] > vetor[posicaoInicio] {
			posicaoInicio++
			return CheckParticioneLadoDireito(vetor, posicaoPivo, posicaoInicio)
		}
		return false
	}

	return true
}
