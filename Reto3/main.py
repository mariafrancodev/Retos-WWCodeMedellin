def linealSearch(array, number):
    resp = 0
    for i in array:
        if i == number:
            return resp
        resp += 1
    return -1

x = [1,9,2,8,3,7,4,6,7]
y = 4
print(linealSearch(x, y))
