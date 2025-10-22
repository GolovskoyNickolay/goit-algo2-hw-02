def find_min_max(arr):
    """
    Знаходить мінімальний та максимальний елементи в масиві
    за допомогою підходу «розділяй і володарюй»
    """
    if len(arr) == 1:
        return arr[0], arr[0]
    
    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])
    
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])
    
    overall_min = min(left_min, right_min)
    overall_max = max(left_max, right_max)
    
    return overall_min, overall_max


if __name__ == "__main__":
    test_arr = [5, 2, 9, 1, 7, 3, 8]
    result = find_min_max(test_arr)
    print(f"Мінімум: {result[0]}, Максимум: {result[1]}")