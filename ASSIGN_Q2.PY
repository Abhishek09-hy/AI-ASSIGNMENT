"""Q2: Compare Linear Search and Binary Search."""


def linear_search(numbers, target):
    """Return (index, comparisons) after scanning from left to right."""
    comparisons = 0
    for index, number in enumerate(numbers):
        comparisons += 1
        if number == target:
            return index, comparisons
    return -1, comparisons


def binary_search(numbers, target):
    """Return (index, comparisons) using binary search on sorted data."""
    left = 0
    right = len(numbers) - 1
    comparisons = 0

    while left <= right:
        middle = (left + right) // 2
        comparisons += 1

        if numbers[middle] == target:
            return middle, comparisons
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1, comparisons


def optimized_binary_search(numbers, target):
    """Use sorted range checks before running binary search."""
    if not numbers or target < numbers[0] or target > numbers[-1]:
        return -1, 0
    return binary_search(numbers, target)


def display_result(numbers, target):
    linear_result = linear_search(numbers, target)
    binary_result = binary_search(numbers, target)
    optimized_result = optimized_binary_search(numbers, target)

    print(f"Target {target}:")
    print(
        f"  Linear:    index={linear_result[0]}, "
        f"comparisons={linear_result[1]}"
    )
    print(
        f"  Binary:    index={binary_result[0]}, "
        f"comparisons={binary_result[1]}"
    )
    print(
        f"  Optimized: index={optimized_result[0]}, "
        f"comparisons={optimized_result[1]}"
    )


if __name__ == "__main__":
    numbers = [5, 12, 18, 23, 31, 45, 56, 72, 89]

    print("Why binary search needs sorted data:")
    print(
        "After checking the middle value, binary search discards half the list. "
        "That is valid only when the remaining values are ordered."
    )
    print("\nSearch results:")

    test_targets = [numbers[0], numbers[len(numbers) // 2], numbers[-1], 50, 100]
    for target in test_targets:
        display_result(numbers, target)

    print("\nUse cases:")
    print("Linear Search works on unsorted data and is suitable for small or changing lists.")
    print("Binary Search is suitable for large, sorted data when many searches are needed.")
    print("Optimization: sorted range checks immediately reject targets below the minimum or above the maximum.")
