package main

// QuickSort implements the QuickSort algorithm
func QuickSort(array []int, start int, end int) {
	if start < end {
		pivotPosition := Partition(array, start, end)

		QuickSort(array, start, pivotPosition-1)
		QuickSort(array, pivotPosition+1, end)
	}
}

// Partition rearranges the elements around the pivot and returns its position
func Partition(array []int, start int, end int) int {
	pivot := array[end]
	i := start - 1

	for j := start; j < end; j++ {
		if array[j] <= pivot {
			i++
			array[i], array[j] = array[j], array[i]
		}
	}

	// Place the pivot in its correct position
	i++
	array[i], array[end] = array[end], array[i]

	return i
}

// Partition2 (optional): Simplified pivoting logic
// This function swaps elements incorrectly and does not properly partition the array.
// It is left here for reference but should not be used.
func Partition2(array []int, start int, end int) int {
	for i := start + 1; i <= end; i++ {
		if array[start] > array[i] {
			array[start], array[i] = array[i], array[start]
		}
	}
	return start
}
