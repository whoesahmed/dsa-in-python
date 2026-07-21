def selection_sort(items):
    """
    Sort a list using the selection sort algorithm.
    
    Args:
        items: A list of items to sort
        
    Returns:
        The sorted list (modified in-place)
    """
    n = len(items)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if items[j] < items[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first unsorted element
        # Only swap if the minimum element is not already in the correct position
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]
    
    return items


if __name__ == '__main__':
    # Test case 1: Unsorted list
    test1 = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", test1)
    selection_sort(test1)
    print("Sorted list:", test1)
    
    # Test case 2: Already sorted list
    test2 = [1, 2, 3, 4, 5]
    print("\nOriginal list:", test2)
    selection_sort(test2)
    print("Sorted list:", test2)
    
    # Test case 3: Reverse sorted list
    test3 = [5, 4, 3, 2, 1]
    print("\nOriginal list:", test3)
    selection_sort(test3)
    print("Sorted list:", test3)
    
    # Test case 4: List with duplicates
    test4 = [3, 1, 4, 1, 5, 9, 2, 6]
    print("\nOriginal list:", test4)
    selection_sort(test4)
    print("Sorted list:", test4)
