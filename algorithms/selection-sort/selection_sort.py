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
    # Test case
    test = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", test)
    selection_sort(test)
    print("Sorted list:", test)