def binary_search(sorted_ids, target):
    low = 0
    high = len(sorted_ids) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_ids[mid] == target:
            return mid
        elif sorted_ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    # Example sorted list of book IDs
    book_ids = [101, 123, 145, 167, 189, 203, 220, 245, 267, 289]

    book_to_find = int(input("Enter book ID to search: "))

    index = binary_search(book_ids, book_to_find)
    if index != -1:
        print(f"Book ID {book_to_find} is available at position {index}.")
    else:
        print(f"Book ID {book_to_find} is not available.")


if __name__ == "__main__":
    main()
