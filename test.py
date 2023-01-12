from time import time
from random import randrange


def sortirovka(spisok: list):
    '''Сортировка по аналогии с бинарным поиском.
    Берём каждый элемент списка(строки\кортежа) и вставляем в новый по принципу бинарного поиска.
    Главная особенность, перечень должен состоять из однотипных эелементов, все числа, или все строки\буквы.'''
    if len(spisok) < 2:
        return spisok
        # Это иф не смог обойти, что если список будет состоять менее чем из 2 элементов.
        # По времени от 0.005 до 0.01 секунды съедает этот иф у меня.
    elem1 = spisok[0]
    elem2 = spisok[1]
    n_spisok = [min(elem1, elem2), max(elem1, elem2)]

    for elem in spisok[2:]:
        centr_index = len(n_spisok) // 2
        l_index = 0
        r_index = len(n_spisok) - 1
        # Узнаём крайнии индексы нового списка и центральный индекс.

        while True:
            # не стоит тут боятся вайл тру, так как цикл только при сбои может дойти до 1000 повторений.
            # 2**32 = 4 294 967 296 - это примерно столько элементов в новом списке при стольких то повторений.

            if elem > n_spisok[centr_index]:
                l_index = centr_index
                centr_index = (r_index + l_index) // 2

            elif elem < n_spisok[centr_index]:
                r_index = centr_index
                centr_index = (r_index + l_index) // 2
            # этими условиями коректируем область в которой ищем индекс.

            if elem <= n_spisok[l_index]:
                # n_spisok = n_spisok[:l_index] + [elem] + n_spisok[l_index:] - такой вариант оказался хуже по времени.
                n_spisok.insert(l_index, elem)
                break

            elif elem >= n_spisok[r_index]:
                n_spisok.insert(r_index + 1, elem)
                break

            elif r_index - l_index == 1 and n_spisok[l_index] < elem < n_spisok[r_index] or elem == n_spisok[
                centr_index]:
                # В ситуации r_index - l_index == 1 l_index всегда равен centr_index (проверил на практике).
                n_spisok.insert(centr_index + 1, elem)
                break

    return n_spisok


sred = []

for _ in range(100):
    LS = []

    for i in range(100000):
        # Формирую рандомный список
        LS.append(randrange(0, 100000))

    start = time()
    _sortirovka = sortirovka(LS)
    sred.append(time() - start)
print(sum(sred) / len(sred))

# 1.5850847029685975 - это если popИем два элемента и без среза идём по списку.
# 1.574343023300171 - это берём первые 2 элемента и потом идём по срезу списка
# Нельзя считать правильным сравнение, т.к. сравнивались разные списки, но переписывать вторую функцию мне лень.
# Да и выборка из 100 рандомных списков думаю даёт какой не какой а средний результат.

# start = time()
# for elem in LS:
#     a = elem
# print(time() - start)
# Выше оказалось самым быстрым. В добавок у меня нет повторно присвоения elem, так что ещё быстрее выходит.

# start = time()
# for elem in range(len(LS)):
#     d = LS[elem]
# print(time() - start)

# start = time()
# while LS:
#      elem = LS.pop()
# print(time() - start)

# start = time()
# while True:
#     elem = LS.pop()
#     if not LS:
#         break
# print(time() - start)
# ----------------------------------------------------------------------------------------------------------------------
# start = time()
# count = 0
# while True:
#     count += 1
#     if count == 100000:
#         break
# print(time() - start)

# start = time()
# for _ in range(1000000): - Этот вариант хоть и быстрее того что выше, на деле в sortirovka медленнее.
#     if _ -- 100000:
#         break
# print(time() - start)
