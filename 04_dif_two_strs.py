def dif_two_strs(a, b):
    Hash_b = {}
    for i in b:
        if i in Hash_b:
            Hash_b[i] += 1
        else:
            Hash_b[i] = 1
    for i in a:
        if i in b:
            Hash_b[i] -= 1
    for i in Hash_b:
        if Hash_b[i] > 0:
            return i
    return ''
# Составляем хеш-таблицу(хеш-функция - кол-во вхождений) для бОльшей строки (то есть строки Б), 
# потом строка А уменьшает значения индексов хеш-таблицы, и в конце остается единственный символ с ненулевым значением 
