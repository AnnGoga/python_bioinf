from random import choice


def insertion_sort(arr):
    """Функция, реализующая алгоритм сортирвки вставками"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    n = 10
    generated_sequence = list("".join(choice(['A', 'C', 'G', 'T']) for i in range(n)))
    print("Исходная последовательность:\n" + str(generated_sequence))
    print("Сортировка с помощью стандартной функции 'sorted':\n" + str(sorted(generated_sequence)))
    print("Сортировка с помощью вставок:\n" + str(insertion_sort(generated_sequence)))
# Вывод:
# Исходная последовательность:
# ['C', 'G', 'G', 'C', 'T', 'T', 'T', 'A', 'T', 'C']
# Сортировка с помощью стандартной функции 'sorted':
# ['A', 'C', 'C', 'C', 'G', 'G', 'T', 'T', 'T', 'T']
# Сортировка с помощью вставок:
# ['A', 'C', 'C', 'C', 'G', 'G', 'T', 'T', 'T', 'T']
