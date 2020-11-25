def bubleSort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array) - i):
            if array[j + 1] < array[j]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux
    return array


array = [6, 5, 3, 1, 8, 7, 2, 4]
<<<<<<< HEAD
print(bubleSort(array))
=======
print(bubleSort(array))
>>>>>>> 1d2194390f923d2f9266198c083fba8b48d43bd9
