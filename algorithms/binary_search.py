def binary_search(arr, target):
	start = 0
	end = len(arr) - 1

	while start < end:
		mid = (start + end) // 2
		guess = arr[mid] 

		if target == guess: 
			return mid
		elif guess < target:
			start = mid + 1
		else:
			end = mid - 1

	return None

print(binary_search([1,2,3,4,5,6], 3))