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


print('Heap Sort', end='\n\n')
print('Heap Sort é um algoritmo de ordenação popular e eficiente em programação de computadores. Aprender a escrever o '
      'algoritmo de classificação de pilha requer conhecimento de dois tipos de estruturas de dados - arrays e árvores.')
print('Seu funcionamento é fundamentado na visualização dos elementos do array em uma forma especial, '
      'chamada heap.', end='\n\n')

print('Entendendo uma árvore binária', end='\n\n')
print('Uma árvore binária é uma estrutura de dados em que cada pai (um nó da árvore) pode ter no máximo dois filhos. '
      'Na imagem, cada elemento possui 2 filhos ')
print('IMAGEM 1', end='\n\n')

print('Árvore binária cheia', end='\n\n')
print('Uma árvore binária cheia (full binary tree) é um tipo especial de árvore binária, '
      'em que todos os pais tem dois filhos ou nenhum.')
print('IMAGEM 2', end='\n\n')

print('Árvore binária completa', end='\n\n')
print('Uma árvore binária completa (Complete binary tree) é como uma árvore binária cheia,'
      ' mas com duas grandes diferenças:')
print('1. Cada nível deve ser completamente preenchido')
print('2. Todos os elementos da folha devem inclinar-se para a esquerda.')
print('2. O último elemento de folha não pode ter um certo irmão, isto é, uma árvore binária '
      'completa não precisa ser uma árvore binária cheia.')

print('IMAGEM 3', end='\n\n')

print('Como criar uma árvore binária completa de uma lista não-ordenada (array)?', end='\n\n')
print('1.Selecione o primeiro elemento da lista para ser o nó raiz. (Primeiro nível - 1 elemento) ')
print('2.Coloque o segundo elemento como um filho à esquerda do nó raiz e o terceiro elemento como um filho a direita. '
      '(Segundo nível - 2 elementos) ')
print('3. Colocar em seguida dois elementos como filhos do nó esquerdo do segundo nível. Mais uma vez,'
      'colocar os dois próximos elementos como filhos do nó direito do segundo nível (nível 3 - 4 elementos).')
print('4. Continue repetindo até chegar o último elemento.')
print('IMAGEM 4', end='\n\n')

print('Relação entre índices do array e elementos da árvore', end='\n\n')
print('Árvore binária completa tem uma propriedade interessante que podemos usar para '
      'encontrar os filhos e os pais de qualquer nó.')
print('Se o índice de qualquer elemento do array é i, o elemento do índice 2i + 1 vai se tornar a criança esquerda '
      'enquanto que o elemento do índice a direita se dará por 2i + 2. Além disso, o pai de qualquer elemento no '
      'índice é dada pelo limite inferior de (i-1) / 2.')
print('IMAGEM 5', end='\n\n')

print('A estrutura do heap', end='\n\n')
print('Heap é uma estrutura de dados baseados em árvores especiais. Uma árvore binária é dito a seguir '
      'uma estrutura de dados heap se:')
print('Deve ser uma árvore binária completa.')
print('Todos os nós na árvore seguem a propriedade que eles são superiores a seus filhos, ou seja, '
      'o elemento maior é a raiz e ambos os seus filhos assumem lugar de nós, ligados a elementos menores que a raiz '
      'e assim por diante. Esse processo é um heap chamado max-heap. Se em vez disso, todos os nós são menores do que '
      'seus filhos, é chamado de min-heap.')
print('A imagem a seguir mostra bem o max-heap e o min-heap')
print('IMAGEM 6', end='\n\n')

print('Como fazer o processo de heapify', end='\n\n')
print('A partir de uma árvore binária completa, nós podemos modificá-lo para se tornar um Max-Heap, executando uma '
      'função chamada heapify sobre todos os elementos não-folha do heap.')
print('Na imagem executamos o heapify em uma árvore com apenas três elementos.')
print('IMAGEM 7', end='\n')

print('O exemplo acima mostra dois cenários - um em que a raiz é o elemento maior e não precisamos fazer nada.'
      'E outra na qual raiz tinha o maior elemento como um filho e precisava trocar para manter a propriedade de '
      'max-heap.')
print('Agora vamos pensar em outro cenário a partir da imagem a seguir')
print('IMAGEM 8', end='\n')

print('O elemento superior não é um max-heap, mas todas as sub-árvores são max-heaps.')
print('Para manter a propriedade de max-heap para a árvore inteira, temos que continuar puxando 2 posições para '
      'baixo até que ele atinja sua posição correta.')
print('IMAGEM 9', end='\n')

print('Assim, para manter a propriedade de max-heap em uma árvore, onde ambas as sub-árvores são max-heaps, '
      'precisamos executar o heapify no elemento raiz, repetidamente, até que o mesmo seja maior do que seus '
      'filhos ou se torne um nó folha.')

print('Construindo o max-heap', end='\n\n')
print('Para construir um max-heap de qualquer árvore, podemos começar aplicar o processo de heapify para cada '
      'sub-árvore de baixo a cima e finalizar com um max-heap depois que a função é aplicada em todos os elementos, '
      'incluindo o elemento raiz.')
print('No caso de uma árvore completa, o primeiro índice do nó não-folha é dada por n/2 - 1.'
      ' Todos os outros nós depois que são nós de folha não precisam passar pelo heapify.')
print('A imagem a seguir representa a construção do max-heap')
print('IMAGEM 10', end='\n')

print('Como mostra no diagrama acima, começamos por heapifying as árvores das menores para os mais baixas e '
      'mover-las gradualmente até chegarmos ao elemento raiz.')


print('Enfim, o heap sort', end='\n\n')
print('Etapas para execução do heap sort: ')
print('1. Desde que a árvore satisfaça a propriedade de Max-Heap, então, o maior item é armazenado no nó raiz.')
print('2. Remover o elemento raiz e colocar no final do array (n-ésima posição. Colocar o último item da árvore (heap) '
      'no lugar vago.')
print('3. Reduzir o tamanho do heap por 1 e aplicar o heapify no elemento raiz novamente para que possamos ter '
      'o maior elemento como raiz.')
print('4. O processo é repetido até que todos os itens da lista é classificada.')
print('IMAGEM 11', end='\n\n')


total_number = int(input('Digite a quantidade de elementos do vetor: '))
arr = fill_vector_disorder(total_number)

before = time.time()
heap_sort(arr)
after = time.time()

total = (after - before) * 1000  # Segundos multiplicados em 10000

print("O tempo gasto para ordenar o vetor foi: {:6f} mili-segundos". format(total))
