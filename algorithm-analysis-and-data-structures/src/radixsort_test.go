package main

import (
	"testing"
)

func TestRadixSort(t *testing.T) {
	array := []int{491, 348, 736, 653, 231, 492, 785, 111}

	RadixSort(array, len(array), 3)

	if !CheckOrder(array, 0, len(array)-1) {
		t.Errorf("RadixSort failed: the array is not sorted")
	}
}
