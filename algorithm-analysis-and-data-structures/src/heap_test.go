package main

import (
	"testing"
)

/*
	The 0th position is ignored to reflect the exact content of the article.
	After the execution of the algorithm, the array should be a max heap.
	Specifically, 100 will move to position 1, and 36 will move to position 3.
*/
func TestMaxHeapify(t *testing.T) {
	array := []int{0, 36, 19, 100, 17, 3, 25, 1, 2, 7}

	MaxHeapify(array, 9, 1)

	if !CheckIsHeap(array, 9) {
		t.Errorf("MaxHeapify failed: the array is not a max heap")
	}
}

/*
	The 0th position is ignored to reflect the exact content of the article.
	After the execution of the algorithm, the array should be a max heap.
*/
func TestBuildMaxHeap(t *testing.T) {
	array := []int{0, 17, 19, 2, 36, 25, 3, 1, 100, 7}

	BuildMaxHeap(array, 9)

	if !CheckIsHeap(array, 9) {
		t.Errorf("BuildMaxHeap failed: the array is not a max heap")
	}
}

/*
	TestHeapSort verifies that the heap sort algorithm sorts the array correctly.
*/
func TestHeapSort(t *testing.T) {
	array := []int{0, 17, 19, 2, 36, 25, 3, 1, 100, 7}

	HeapSort(array, 9)

	if !CheckOrder(array, 1, 9) {
		t.Errorf("HeapSort failed: the array is not sorted")
	}
}
