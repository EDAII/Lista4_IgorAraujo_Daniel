import random
import time


# Preenchendo Vetor Desordenado
def fill_vector_disorder(total_numbers):
    vector = list(range(0, total_numbers + 1))
    random.shuffle(vector)
    return vector


def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n, 0, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        # swap
        arr[i], arr[0] = arr[0], arr[i]

        # heapify root element
        heapify(arr, i, 0)



# total_number = int(input('Digite a quantidade de elementos do vetor: '))
# arr = fill_vector_disorder(total_number)

# before = time.time()
# heap_sort(arr)
# after = time.time()

# total = (after - before) * 1000  # Segundos multiplicados em 10000

# print("O tempo gasto para ordenar o vetor foi: {:6f} mili-segundos". format(total))
