package main

// MaxHeapify adjusts the heap from the given item position
func MaxHeapify(array []int, numElements int, itemPosition int) {
	leftChild := itemPosition * 2
	rightChild := (itemPosition * 2) + 1
	var largestPosition int

	if leftChild <= numElements && array[leftChild] > array[itemPosition] {
		largestPosition = leftChild
	} else {
		largestPosition = itemPosition
	}

	if rightChild <= numElements && array[rightChild] > array[largestPosition] {
		largestPosition = rightChild
	}

	if itemPosition != largestPosition {
		// Swap the values in the array
		array[itemPosition], array[largestPosition] = array[largestPosition], array[itemPosition]

		// Recursively adjust the heap
		MaxHeapify(array, numElements, largestPosition)
	}
}

// BuildMaxHeap converts the array into a Max Heap
func BuildMaxHeap(array []int, numElements int) {
	for i := numElements / 2; i >= 1; i-- {
		MaxHeapify(array, numElements, i)
	}
}

// CheckIsHeap verifies if the array is a heap
func CheckIsHeap(array []int, numElements int) bool {
	checkIndex := 1

	for (checkIndex * 2) <= numElements {
		leftChild := checkIndex * 2

		if array[checkIndex] < array[leftChild] {
			return false
		}

		rightChild := leftChild + 1

		if numElements >= rightChild && array[checkIndex] < array[rightChild] {
			return false
		}

		checkIndex++
	}

	return true
}

// HeapSort sorts an array using the heap sort algorithm
func HeapSort(array []int, numElements int) {
	BuildMaxHeap(array, numElements)

	auxNumElements := numElements

	for numElements > 1 {
		// Swap the root with the last element
		array[1], array[numElements] = array[numElements], array[1]

		auxNumElements--

		// Rebuild the heap
		MaxHeapify(array, auxNumElements, 1)

		numElements--
	}
}
