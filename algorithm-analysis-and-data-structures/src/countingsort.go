package main

// CountingSort is a sorting algorithm with linear time complexity
func CountingSort(inputArray []int, outputArray []int, numElements int, maxNumber int) {

	var auxiliaryArray []int

	// Initializing the auxiliary array
	for i := 0; i <= maxNumber; i++ {
		auxiliaryArray = append(auxiliaryArray, 0)
	}

	// Counting the occurrences of each element in the input array
	for i := 0; i < numElements; i++ {
		auxiliaryArray[inputArray[i]]++
	}

	// Accumulating values in the auxiliary array
	// Each element at index i will hold the sum of previous elements.
	// This determines the position of each element in the output array.
	for i := 1; i <= maxNumber; i++ {
		auxiliaryArray[i] += auxiliaryArray[i-1]
	}

	// Filling the output array with sorted elements.
	// The algorithm is stable because it preserves the order of duplicate elements.
	for i := numElements - 1; i >= 0; i-- {
		outputArray[auxiliaryArray[inputArray[i]]-1] = inputArray[i]
		auxiliaryArray[inputArray[i]]--
	}
}
