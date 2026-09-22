"""Find the most valuable combination of items within a budget.

- Approach comparison:
        - Brute force checks every subset, so it guarantees the optimum but takes
            O(2**n) time.
        - Greedy is faster, but it does not guarantee the optimum for arbitrary
            item prices and values.
        - Dynamic programming guarantees the optimum for this 0/1 knapsack problem
            in O(n * budget) time and O(budget * n) space with the selected-item
            tracking used below.

Dynamic programming is selected because each item can be chosen at most once
and the budget is an integer.

A simple starting solution is to try every subset and keep the best valid one.
For larger inputs, memory can be reduced by storing only reachable budgets in a
dictionary, or the budget can be scaled to larger currency units. If the number
of items is small but prices are very large, meet-in-the-middle can be used
instead of a budget-sized DP table.
"""

items = [
    ("Laptop", 60000),
    ("Phone", 30000),
    ("Tablet", 20000),
    ("Watch", 10000),
    ("Headphones", 5000)
]


def best_combination(items, budget):
    """Return the maximum total price and the items used to reach it."""

    if budget < 0:
        raise ValueError("budget must be non-negative")

    # dp[i] = maximum value possible with budget i
    dp = [0] * (budget + 1)

    # Track selected items
    selected = [[] for _ in range(budget + 1)]

    for name, price in items:
        # Traverse backwards so each item is used only once
        for b in range(budget, price - 1, -1):

            if dp[b - price] + price > dp[b]:
                dp[b] = dp[b - price] + price
                selected[b] = selected[b - price] + [name]

    return dp[budget], selected[budget]


def display_results(items, budgets):
    """Print the result for each test budget."""

    for budget in budgets:
        total, combination = best_combination(items, budget)

        print("Budget:", budget)
        print("Selected Items:", combination)
        print("Total Price:", total)
        print("Remaining Budget:", budget - total)
        print("-" * 40)


if __name__ == "__main__":
    # Test with three different budgets.
    display_results(items, [50000, 70000, 100000])