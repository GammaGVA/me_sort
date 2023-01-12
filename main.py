from time import time
from random import randrange


def clone_sorted(spisok: list):
    '''Реализация быстрой сортировки.
    Проверял скорость работы выполненой сортировки в пайтон,
    для будущей сверки по времени уже со своей сортировкой.'''
    if len(spisok) > 1:
        centr = len(spisok) // 2
        elem = [spisok.pop(centr)]
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


def statistics(len_list=100000, max_elem=100000):
    LS = []

    for i in range(len_list):
        # Формирую рандомный список
        LS.append(randrange(0, max_elem))

    start = time()
    _sorted = sorted(LS)
    time_sorted = (time() - start)

    start = time()
    _sortirovka = sortirovka(LS)
    time_sortirovka = (time() - start)

    start = time()
    _clone_sorted = clone_sorted(LS)
    time_clone_sorted = (time() - start)

    with open(f'statistics/{len_list}.txt', 'a') as file:
        file.write(f'''\nДлинна списка {len_list}
Элемент принимает значение от 0 до {max_elem}.
sorted выполнил сортровку за {time_sorted}
sortirovka выполнил сортровку за {time_sortirovka}
clone_sorted выполнил сортровку за {time_clone_sorted}
sorted быстрее sortirovka в {time_sortirovka / time_sorted}
sorted быстрее clone_sorted в {time_clone_sorted / time_sorted}
clone_sorted быстрее sortirovka в {time_sortirovka / time_clone_sorted}\n''')
        file.write('_' * 20)


LS = [10, 100, 1000, 10000, 100000, 200000, 300000, 400000, 500000]
LE = [10, 100, 1000, 10000, 100000]

for i in LS:
    for j in LE:
        for _ in range(3):
            statistics(len_list=i, max_elem=j)
        with open(f'statistics/{i}.txt', 'a') as file:
            file.write('\nСледующая размерность=========================!\n')

'''У меня xeon3440 и опереатива частотой 1600. Будь всё пошустрее время было бы пошустрее.
Вывод: при увелечение списка на порядок при размере списка до 100.000 включительно, скорость уменьшалась на порядок,
порой на порядок с коэфицентом.
Принцип замедления скорости у всех одинаков, до 100.000 у всех падает скорость на порядок.
200.000-400.000 увеличивается в 2-3 раза(если округлить).
если сравнивать 400 и 500 тысяч то замедление произошло на 1/3 у всех эта зависимость(повторюсь) одинаковая.
sortirovka при увеличение разброса велечины значения элемента скорость теряла но не значительно. Если сравнивать
в пропорциях но меньше всего, даже почти без изменений.
Вывод сделать не могу, данных мало, желательно бы запустить более дитальную проверку, начиная от 100.000 увеличивать
на 10.000, также проводить тест не 3 раза а 1000. Удобнее будет смотреть в графике, это сделать можно но я не умею пока.
Проверку выполнить хотя бы до 10_000_000. Возможности моего пк будут это делать год. Жопой чую что в Другом языке даст
результат гораздо лучше, но на сколько не понимаю.
Обнадёживает закономерность падения скорости, она у всех одинаковая при увелечение размерности списка,
а при увелечение размерности элемента и вовсе почти не замедляется по сравнению с другими.
Ещё бы попробовать реализовать это в Си.
Чуть поменял ифы. Скорость не понятно больше ли стала, или нет. Всё также осталось.'''
