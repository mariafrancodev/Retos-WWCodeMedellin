def bubleSort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array) - i):
            if array[j + 1] < array[j]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux
    return array


array = [6, 5, 3, 1, 8, 7, 2, 4]
print(bubleSort(array))
print("hola")

