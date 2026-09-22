"""Q3: Compare Bubble Sort, Selection Sort, and Insertion Sort."""


def bubble_sort(numbers):
    """Return (sorted list, comparisons, swaps)."""
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


def selection_sort(numbers):
    """Return (sorted list, comparisons, swaps)."""
    result = numbers.copy()
    comparisons = 0
    swaps = 0

    for position in range(len(result) - 1):
        smallest = position
        for index in range(position + 1, len(result)):
            comparisons += 1
            if result[index] < result[smallest]:
                smallest = index
        if smallest != position:
            result[position], result[smallest] = result[smallest], result[position]
            swaps += 1

    return result, comparisons, swaps


def insertion_sort(numbers):
    """Return (sorted list, comparisons, shifts)."""
    result = numbers.copy()
    comparisons = 0
    shifts = 0

    for position in range(1, len(result)):
        current = result[position]
        index = position - 1

        while index >= 0:
            comparisons += 1
            if result[index] <= current:
                break
            result[index + 1] = result[index]
            shifts += 1
            index -= 1
        result[index + 1] = current

    return result, comparisons, shifts


def display_result(name, result):
    sorted_data, comparisons, movements = result
    movement_name = "shifts" if name == "Insertion Sort" else "swaps"
    print(
        f"{name}: sorted={sorted_data}, comparisons={comparisons}, "
        f"{movement_name}={movements}"
    )


if __name__ == "__main__":
    data = [45, 12, 78, 34, 23, 89, 5, 67, 10, 56]
    expected = sorted(data)

    results = {
        "Bubble Sort": bubble_sort(data),
        "Selection Sort": selection_sort(data),
        "Insertion Sort": insertion_sort(data),
    }

    print(f"Original data: {data}")
    print("\nExperimental results using the same input:")
    for name, result in results.items():
        display_result(name, result)
        assert result[0] == expected

    print("\nStrengths and weaknesses:")
    print("Bubble Sort is simple and can stop early, but it usually performs many swaps.")
    print("Selection Sort uses few swaps, but it still makes quadratic comparisons.")
    print("Insertion Sort is simple and efficient for nearly sorted data, but shifts many values in a reversed list.")
    print("\nBest choice for nearly sorted data: Insertion Sort, because it can approach linear time.")

    print("\nTheoretical complexity:")
    print("Bubble Sort: best O(n) with early exit, average/worst O(n^2), space O(1).")
    print("Selection Sort: best/average/worst O(n^2), space O(1).")
    print("Insertion Sort: best O(n), average/worst O(n^2), space O(1).")
    print("The measured counts show the expected quadratic behavior for this small unsorted input.")
