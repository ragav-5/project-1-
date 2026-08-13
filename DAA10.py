import random
import sys
import time

sys.setrecursionlimit(25000)

comparison_counter = 0


def divide_array(items, start, end):
    global comparison_counter
    pivot_val = items[end]
    split_idx = start - 1

    for curr in range(start, end):
        comparison_counter += 1
        if items[curr] <= pivot_val:
            split_idx += 1
            items[split_idx], items[curr] = items[curr], items[split_idx]

    items[split_idx + 1], items[end] = items[end], items[split_idx + 1]
    return split_idx + 1


def standard_quicksort(items, start, end):
    if start < end:
        p_idx = divide_array(items, start, end)
        standard_quicksort(items, start, p_idx - 1)
        standard_quicksort(items, p_idx + 1, end)


def randomized_quicksort(items, start, end):
    if start < end:
        rand_pivot = random.randint(start, end)
        items[rand_pivot], items[end] = items[end], items[rand_pivot]

        p_idx = divide_array(items, start, end)
        randomized_quicksort(items, start, p_idx - 1)
        randomized_quicksort(items, p_idx + 1, end)


def benchmark_sort(sort_routine, data):
    global comparison_counter
    array_copy = list(data)
    comparison_counter = 0

    t_start = time.perf_counter()
    sort_routine(array_copy, 0, len(array_copy) - 1)
    t_end = time.perf_counter()

    duration_ms = (t_end - t_start) * 1000
    return comparison_counter, duration_ms


# --- Main Driver ---
if __name__ == "__main__":
    ARRAY_SIZE = 4000

    # Build nearly-sorted data via step swaps instead of full random indexing
    partially_ordered = list(range(1, ARRAY_SIZE + 1))
    for idx in range(0, ARRAY_SIZE - 2, 10):
        partially_ordered[idx], partially_ordered[idx + 2] = (
            partially_ordered[idx + 2],
            partially_ordered[idx],
        )

    benchmarks = {
        "Unsorted": [random.randint(10, 500000) for _ in range(ARRAY_SIZE)],
        "Ascending": list(range(1, ARRAY_SIZE + 1)),
        "Descending": list(range(ARRAY_SIZE, 0, -1)),
        "Semi-Sorted": partially_ordered,
    }

    # Formatting table output
    header = (
        f"{'Category':<15} | {'Std Comps':>12} | {'Std Time(ms)':>13} | "
        f"{'Rand Comps':>12} | {'Rand Time(ms)':>13}"
    )
    print(header)
    print("-" * len(header))

    for label, arr_data in benchmarks.items():
        std_c, std_t = benchmark_sort(standard_quicksort, arr_data)
        rnd_c, rnd_t = benchmark_sort(randomized_quicksort, arr_data)

        print(
            f"{label:<15} | {std_c:>12d} | {std_t:>13.2f} | "
            f"{rnd_c:>12d} | {rnd_t:>13.2f}"
        )