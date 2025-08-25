def find_min_max(arr):
    """
    Знаходить мінімальний і максимальний елементи в масиві,
    використовуючи метод "розділяй і володарюй".

    :param arr: Масив чисел довільної довжини.
    :return: Кортеж (мінімальний елемент, максимальний елемент).
    """

    n = len(arr)

    # Базовий випадок для одного елемента
    if n == 1:
        return (arr[0], arr[0])

    # Базовий випадок для двох елементів
    if n == 2:
        if arr[0] > arr[1]:
            return (arr[1], arr[0])
        else:
            return (arr[0], arr[1])

    # Рекурсивний випадок
    mid = n // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # Рекурсивний виклик для лівої та правої частини
    min1, max1 = find_min_max(left_arr)
    min2, max2 = find_min_max(right_arr)

    # Комбінування результатів
    return (min(min1, min2), max(max1, max2))