# me_sort/Бинарная сортировка/Бесконечная сортировка
Читаю я такой грокаем алгоритмы, на моменте бинарного поиска. В голову приходит идея о бинарной сортировки.
В моём понимае такая сортировка это: читаем не отсортированный список и вставляем элементы в другой попутно сравнивая с центральным элементом "списка".
При условии больше/меньше меняем диапазон и выбора "центрального" элемента. Потом вставляем на своё место новый элемент.
По логике вещей, скорость должна быть n*log(n). Мы идём по списку и со скоростью log(n) вставляем элемент. Но на деле...
Получилось значительно медленнее чем у готового sorted и даже у самописного аналога на python. Но закономерности замедления скорости одинаковые.
На выборки от 10к до 200к коэфициенты изменение скорости от предыдущего теста примерна равны у всех трёх сортировок.
Я пока учусь и многого не знаю/понимаю, знаю что Си быстрее и вот если по всему уму написать этот алгоритм какая будет скорость?
Написал такую сортировку для себя, чтоб голову напрячь. Думаю Я далеко не первый кто об этом думал.
Теперь интересно, как максимально можно её оптимизировать и какая разница во времени будет с быстрой сортировкой.
Повторюсь, писал для себя, чтоб голову напрячь. Но если вдруг, прям вот всё и вся повернётся таким образом, что это ускорит работу вычесления.
Я буду рад. Если вдруг ты читаешь это и владеешь Си, и вдруг тебе стало интересно "как оно", то по итогу твоих стараний дай знать какой результат.
Т.к. знаниями пока не обладаю обширнами собрал инфу в тэхэтэ файлы. Позже думаю сделать графики и повозможности прогнать сутки трое пк для наглядности.
Так-то, как по мне, это идиальная бесконечная сортировка. Вот к примеру нам на вход постоянно приходят новые элементы.
То уже отсортированный список не надо пересортирововать, а просто в него добавить элемент.
Но тут  так понял с особенностью памяти сложности, то что "вставка" происходит.
