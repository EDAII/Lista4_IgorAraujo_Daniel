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


arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)

print('Heap Sort é um algoritmo de ordenação popular e eficiente em programação de computadores. Aprender a escrever o '
      'algoritmo de classificação de pilha requer conhecimento de dois tipos de estruturas de dados - arrays e árvores.')
print('Seu funcionamento é fundamentado na visualização dos elementos do array em uma forma especial, '
      'chamada heap.', end='\n\n')

print('Entendendo uma árvore binária:', end='\n\n')
print('Uma árvore binária é uma estrutura de dados em que cada pai (um nó da árvore) pode ter no máximo dois filhos. '
      'Na imagem, cada elemento possui 2 filhos ')
print('IMAGEM 1', end='\n\n')

print('Árvore binária cheia:', end='\n\n')
print('Uma árvore binária cheia (full binary tree) é um tipo especial de árvore binária, '
      'em que todos os pais tem dois filhos ou nenhum.')
print('IMAGEM 2', end='\n\n')

print('Árvore binária completa:', end='\n\n')
print('Uma árvore binária completa (Complete binary tree) é como uma árvore binária cheia,'
      ' mas com duas grandes diferenças:')
print('1. Cada nível deve ser completamente preenchido')
print('2. Todos os elementos da folha devem inclinar-se para a esquerda.')
print('2. O último elemento de folha não pode ter um certo irmão, isto é, uma árvore binária '
      'completa não precisa ser uma árvore binária cheia.')

print('IMAGEM 3', end='\n\n')

n = len(arr)
print("Sorted array is")
print(arr)
