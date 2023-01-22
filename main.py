def clone_sorted(spisok: list):
    '''Реализация быстрой сортировки.
    Проверял скорость работы выполненой сортировки в пайтон,
    для будущей сверки по времени уже со своей сортировкой.'''
    if len(spisok) > 1:
        elem = [spisok[len(spisok)//2]]
        men = []
        big = []
        for i in spisok:
            if i > elem[0]:
                big.append(i)
            elif i < elem[0]:
                men.append(i)
            else:
                elem.append(i)

        return clone_sorted(men) + elem + clone_sorted(big)
    else:
        return spisok


def sortirovka(spisok: list):
    '''Сортировка по аналогии с бинарным поиском.
    Берём каждый элемент списка(строки\кортежа) и вставляем в новый по принципу бинарного поиска.
    Главная особенность, перечень должен состоять из однотипных эелементов, все числа, или все строки\буквы.
    Возвращает список.'''
    if len(spisok) < 2:
        return spisok
        # Это иф не смог обойти, что если список будет состоять менее чем из 2 элементов.
        # По времени от 0.005 до 0.01 секунды съедает этот иф у меня.
    elem1 = spisok[0]
    elem2 = spisok[1]
    n_spisok = [min(elem1, elem2), max(elem1, elem2)]

    for elem in tuple(spisok[2:]):
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
