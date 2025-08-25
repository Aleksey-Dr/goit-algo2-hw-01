def partition(arr, left, right):
    """
    Допоміжна функція для розбиття масиву.
    Повертає індекс опорного елемента після розбиття.
    """
    pivot_value = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def quick_select(arr, k):
    """
    Знаходить k-й найменший елемент у масиві, використовуючи Quick Select.

    :param arr: Масив чисел.
    :param k: Позиція шуканого елемента (1-based).
    :return: k-й найменший елемент.
    """
    if not 1 <= k <= len(arr):
        raise ValueError("k має бути в межах від 1 до довжини масиву")

    left, right = 0, len(arr) - 1

    while left <= right:
        pivot_index = partition(arr, left, right)
        # Позиція опорного елемента, враховуючи, що k - 1-based
        pivot_position = pivot_index + 1

        if pivot_position == k:
            return arr[pivot_index]
        elif pivot_position > k:
            # Шуканий елемент знаходиться в лівій частині
            right = pivot_index - 1
        else:
            # Шуканий елемент знаходиться в правій частині
            left = pivot_index + 1
    
    return None # Цей рядок недосяжний, якщо k коректне