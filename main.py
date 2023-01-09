from time import time
from random import randrange


def sortted(spisok: list):
    '''Реализация быстрой сортировки.
    Проверял скорость работы выполненой сортировки в пайтон,
    для будущей сверки по времени и понимая полезности следующей сортировки.'''
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

        return sortted(men) + elem + sortted(big)
    else:
        return spisok


def sortirovka(spisok: list):
    '''Сортировка по налогии с бинарным поиском.
    Берём каждый элемент списка(строки\кортежа) и вставляем в новый по принципу бинарного поиска.
    Главная особенность, перечень должен состоять из однотипных эелементов, все числа, или все строки\буквы.'''
    if len(spisok) > 1:
        # Это иф не смог обойти, что если список будет состоять менее чем из 2 элементов.
        elem1 = spisok[0]
        elem2 = spisok[1]
        spisok = tuple(spisok[2:])
        n_spisok = (min(elem1, elem2), max(elem1, elem2))

        for elem in spisok:
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
                    # коректируем область в которой ищем индекс.

                elif elem < n_spisok[centr_index]:
                    r_index = centr_index
                    centr_index = (r_index + l_index) // 2
                    # коректируем область в которой ищем индекс.

                elif elem == n_spisok[centr_index]:
                    n_spisok = n_spisok[:centr_index] + (elem,) + n_spisok[centr_index:]
                    break
                    # Вставляем элемент и закрываем цикл так как он вечный

                if r_index == l_index and elem < n_spisok[l_index]:
                    n_spisok = n_spisok[:l_index] + (elem,) + n_spisok[r_index:]
                    break

                elif r_index == l_index and elem > n_spisok[r_index]:
                    n_spisok = n_spisok[:r_index + 1] + (elem,) + n_spisok[r_index + 1:]
                    break

                elif r_index - l_index == 1 and n_spisok[l_index] < elem < n_spisok[r_index]:
                    n_spisok = n_spisok[:l_index + 1] + (elem,) + n_spisok[r_index:]
                    break

                elif r_index - l_index == 1 and (elem < n_spisok[l_index] or elem == n_spisok[l_index]):
                    n_spisok = n_spisok[:l_index] + (elem,) + n_spisok[l_index:]
                    break

                elif r_index - l_index == 1 and (elem > n_spisok[r_index] or elem == n_spisok[r_index]):
                    n_spisok = n_spisok[:r_index + 1] + (elem,) + n_spisok[r_index + 1:]
                    break

        return n_spisok

    else:
        return tuple(spisok)


LS = []

for i in range(100000):
    # Формирую рандомный список
    LS.append(randrange(0, 100000))

start = time()
_a = sorted(LS)
time_sorted = (time() - start)
print(time_sorted)

start = time()
a = sortirovka(LS)
time_sortirovka = (time() - start)
print(time_sortirovka)

start = time()
c = sortted(LS)
time_sortted = (time() - start)
print(time_sortted)

print(f'sorted быстрее sortirovka в {time_sortirovka / time_sorted}')
print(f'sorted быстрее sortted в {time_sortted / time_sorted}')
print(f'sortted быстрее sortirovka в {time_sortirovka / time_sortted}')

'''
Это я ещё сравнивал разницу скорости у себя на версиях пайтон 3.10 и 3.11.

На 3.10
0.030642032623291016
109.65123796463013
0.4462869167327881
sorted быстрее sortirovka в 3578.458365104807
sorted быстрее sortted в 14.564533698510761
sortted быстрее sortirovka в 245.69673421612586
_______________________________________________
0.029674768447875977
113.8092451095581
0.4175376892089844
sorted быстрее sortirovka в 3835.2193146667737
sorted быстрее sortted в 14.070461575543325
sortted быстрее sortirovka в 272.5723881960623
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
На 3.11
0.02505660057067871
102.63605499267578
0.21150755882263184
sorted быстрее sortirovka в 4096.168380988629
sorted быстрее sortted в 8.441191303106713
sortted быстрее sortirovka в 485.2595130122294
______________________________________________
0.02314019203186035
100.64344453811646
0.2205972671508789
sorted быстрее sortirovka в 4349.2916739647835
sorted быстрее sortted в 9.533078500262732
sortted быстрее sortirovka в 456.23160176903156
______________________________________________
0.02330470085144043
111.60277915000916
0.23963069915771484
sorted быстрее sortirovka в 4788.852680900693
sorted быстрее sortted в 10.282504833907947
sortted быстрее sortirovka в 465.7282207258299
'''
