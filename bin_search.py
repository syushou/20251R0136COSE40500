#Binary Search in Python
def binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    
    Parameters:
    arr (list): The sorted list to search through
    target (int): The number to search for
    
    Returns:
    int: The index of the target if found, else -1
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage
numbers = [1, 3, 5, 7, 9, 11]
target_number = 7
result = binary_search(numbers, target_number)

if result != -1:
    print(f"Found {target_number} at index {result}")
else:
    print(f"{target_number} not found in the list")
