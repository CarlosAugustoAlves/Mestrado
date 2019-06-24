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
		t.Errorf("Quuick Sort não funcionou")
	}
}

func TestParticione(t *testing.T) {

	posicaoInicio := 0
	posicaoFinal := 5
	vetor := []int{47, 22, 40, 56, 34, 42}

	posicaoPivo := Particione(vetor, posicaoInicio, posicaoFinal)

	if !checkParticioneLadoDireito(vetor, posicaoPivo, posicaoFinal) ||
		!checkParticioneLadoEsquerdo(vetor, posicaoPivo, posicaoInicio) {
		t.Errorf("Particione não funcionou")
	}
}

func checkParticioneLadoDireito(vetor []int, posicaoPivo int, posicaoFinal int) bool {

	if posicaoPivo < posicaoFinal {
		if vetor[posicaoPivo] < vetor[posicaoFinal] {
			posicaoFinal--
			return checkParticioneLadoDireito(vetor, posicaoPivo, posicaoFinal)
		}

		return false
	}

	return true
}

func checkParticioneLadoEsquerdo(vetor []int, posicaoPivo int, posicaoInicio int) bool {

	if posicaoPivo > posicaoInicio {
		if vetor[posicaoPivo] > vetor[posicaoInicio] {
			posicaoInicio++
			return checkParticioneLadoDireito(vetor, posicaoPivo, posicaoInicio)
		}
		return false
	}

	return true
}
