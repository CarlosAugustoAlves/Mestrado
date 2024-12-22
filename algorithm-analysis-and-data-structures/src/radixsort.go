package main

import (
	"strconv"
)

// RadixSort performs linear sorting based on the number of digits in the elements of the array
func RadixSort(array []int, numElements int, numDigits int) {
	digitArray := make([]int, numElements)

	for digitPosition := numDigits - 1; digitPosition >= 0; digitPosition-- {

		fillDigitArray(array, digitArray, 0, numElements, digitPosition) // O(numDigits * Θ(n))

		maxValue := findMax(digitArray, 0, numElements, 0) // O(numDigits * Θ(n))

		positionInfo := stableSort(digitArray, numElements, maxValue) // O(numDigits * Θ(n))

		auxArray := make([]int, numElements)
		copy(auxArray, array) // O(numDigits * Θ(n))

		// Rearrange the original array using position info
		for i := 0; i < numElements; i++ { // O(numDigits * Θ(n))
			array[positionInfo[i]] = auxArray[i]
		}
	}
}

// fillDigitArray extracts the digit at the specified position for each element
func fillDigitArray(array []int, digitArray []int, start int, numElements int, digitPosition int) {
	if start < numElements {
		digitStr := strconv.Itoa(array[start]) // Convert the number to string

		// Ensure the string is padded to avoid out-of-range errors
		if digitPosition >= len(digitStr) {
			digitArray[start] = 0
		} else {
			digitValue, err := strconv.Atoi(string(digitStr[digitPosition])) // Get the character as an integer
			if err != nil {
				panic(err)
			}
			digitArray[start] = digitValue
		}

		fillDigitArray(array, digitArray, start+1, numElements, digitPosition)
	}
}

// findMax finds the maximum value in an array
func findMax(array []int, start int, end int, maxValue int) int {
	if start < end {
		if maxValue < array[start] {
			maxValue = array[start]
		}
		return findMax(array, start+1, end, maxValue)
	}
	return maxValue
}

// stableSort performs a stable sorting of the array based on the current digit
func stableSort(digitArray []int, numElements int, maxValue int) []int {
	positionInfo := make([]int, numElements)
	countArray := make([]int, maxValue+1)

	// Count occurrences of each digit
	for i := 0; i < numElements; i++ {
		countArray[digitArray[i]]++
	}

	// Accumulate counts to determine positions
	for i := 1; i <= maxValue; i++ {
		countArray[i] += countArray[i-1]
	}

	// Populate the position info array
	for i := numElements - 1; i >= 0; i-- {
		positionInfo[i] = countArray[digitArray[i]] - 1
		countArray[digitArray[i]]--
	}

	return positionInfo
}
