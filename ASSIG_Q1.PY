"""Q1: AI-assisted Bubble Sort analysis."""


def bubble_sort(numbers):
	"""Sort numbers with basic Bubble Sort and return (list, comparisons, swaps)."""
	result = numbers.copy()
	comparisons = 0
	swaps = 0

	for pass_number in range(len(result) - 1):
		for index in range(len(result) - 1 - pass_number):
			comparisons += 1
			if result[index] > result[index + 1]:
				result[index], result[index + 1] = result[index + 1], result[index]
				swaps += 1

	return result, comparisons, swaps


def bubble_sort_early_exit(numbers):
	"""Bubble Sort that stops when a complete pass makes no swaps."""
	result = numbers.copy()
	comparisons = 0
	swaps = 0

	for pass_number in range(len(result) - 1):
		swapped = False
		for index in range(len(result) - 1 - pass_number):
			comparisons += 1
			if result[index] > result[index + 1]:
				result[index], result[index + 1] = result[index + 1], result[index]
				swaps += 1
				swapped = True

		if not swapped:
			break

	return result, comparisons, swaps


def explain_first_pass(numbers):
	"""Print the adjacent comparisons and swaps in the first pass."""
	working = numbers.copy()
	print("First pass explanation:")
	for index in range(len(working) - 1):
		left = working[index]
		right = working[index + 1]
		if left > right:
			working[index], working[index + 1] = right, left
			action = f"swap -> {working}"
		else:
			action = "no swap"
		print(f"Compare {left} and {right}: {action}")
	print(f"After pass 1: {working}")


def display_results(numbers):
	"""Display results for one input using both Bubble Sort versions."""
	basic = bubble_sort(numbers)
	improved = bubble_sort_early_exit(numbers)
	print(f"\nInput: {numbers}")
	print(f"Basic:    sorted={basic[0]}, comparisons={basic[1]}, swaps={basic[2]}")
	print(
		f"Improved: sorted={improved[0]}, "
		f"comparisons={improved[1]}, swaps={improved[2]}"
	)


if __name__ == "__main__":
	starter_list = [64, 34, 25, 12, 22, 11, 90]
	explain_first_pass(starter_list)

	test_lists = [
		starter_list,
		[1, 2, 3, 4, 5],
		[5, 4, 3, 2, 1],
	]
	for test_list in test_lists:
		display_results(test_list)





