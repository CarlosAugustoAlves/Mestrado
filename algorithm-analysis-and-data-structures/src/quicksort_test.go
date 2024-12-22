package main

import (
	"testing"
)

// TestQuickSort verifies that the QuickSort function sorts the array correctly
func TestQuickSort(t *testing.T) {
	start := 0
	end := 5
	array := []int{47, 22, 40, 56, 34, 42}

	QuickSort(array, start, end)

	if !CheckOrder(array, start, end) {
		t.Errorf("QuickSort failed: the array is not sorted")
	}
}

// TestPartition verifies that the Partition function correctly positions the pivot
func TestPartition(t *testing.T) {
	start := 0
	end := 5
	array := []int{47, 22, 40, 56, 34, 42}

	pivotPosition := Partition(array, start, end)

	if !checkPartitionRightSide(array, pivotPosition, end) ||
		!checkPartitionLeftSide(array, pivotPosition, start) {
		t.Errorf("Partition failed: the array is not partitioned correctly")
	}
}

// checkPartitionRightSide checks that all elements to the right of the pivot are greater or equal
func checkPartitionRightSide(array []int, pivotPosition int, end int) bool {
	if pivotPosition < end {
		if array[pivotPosition] <= array[end] {
			end--
			return checkPartitionRightSide(array, pivotPosition, end)
		}
		return false
	}
	return true
}

// checkPartitionLeftSide checks that all elements to the left of the pivot are less or equal
func checkPartitionLeftSide(array []int, pivotPosition int, start int) bool {
	if pivotPosition > start {
		if array[pivotPosition] >= array[start] {
			start++
			return checkPartitionLeftSide(array, pivotPosition, start)
		}
		return false
	}
	return true
}
