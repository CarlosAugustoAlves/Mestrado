package main

import "fmt"

func MaxHEAPFY(vetor []int, numeroElementos int, posicaoItem int) {
	posicaoFilhoEsquerdo := posicaoItem * 2
	posicaoFilhoDireito := ((posicaoItem * 2) + 1)

	trocarPosicao := false
	var indiceTroca int
	valorItemAtual := vetor[posicaoItem]

	if posicaoFilhoEsquerdo <= numeroElementos && vetor[posicaoFilhoEsquerdo] > vetor[posicaoItem] {
		trocarPosicao = true
		indiceTroca = posicaoFilhoEsquerdo
	}

	if posicaoFilhoDireito <= numeroElementos && vetor[posicaoFilhoDireito] > vetor[posicaoItem] {
		trocarPosicao = true
		indiceTroca = posicaoFilhoDireito
	}

	if trocarPosicao {
		vetor[posicaoItem] = vetor[indiceTroca]
		vetor[indiceTroca] = valorItemAtual

		MaxHEAPFY(vetor, numeroElementos, indiceTroca)
	}
}

func main() {
	fmt.Println("Hello World")
}
