package main

import (
	"testing"
)

func TestCountingSort(t *testing.T) {
	// Use descriptive variable names in English for consistency
	numElements := 7
	inputArray := []int{4, 3, 4, 3, 1, 0, 3}
	outputArray := make([]int, numElements)
	maxValue := 4

	// Call the CountingSort function
	CountingSort(inputArray, outputArray, numElements, maxValue)

	// Validate the output array is sorted
	if !CheckOrder(outputArray, 0, numElements-1) {
		t.Errorf("CountingSort failed: output array is not sorted")
	}
}
