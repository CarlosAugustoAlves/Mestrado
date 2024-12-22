package main

// CheckOrder checks if the array is in ascending order
func CheckOrder(array []int, position int, finalPosition int) bool {

	if position+1 <= finalPosition {
		if array[position] <= array[position+1] {
			position++
			return CheckOrder(array, position, finalPosition)
		}

		return false
	}

	return true
}
