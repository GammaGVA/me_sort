# Бинарная сортировка/Бесконечная сортировка.

Идея пришла при прочтении книги про алгоритмы, в частности из-за бинарного поиска. Средствами python данная сортировка сортирует очень медленно, но сама идея мне приятна. В теории должна работать со скоростью O(N log(N)). Принцип её в том, что берём элемент из несортированного списка, ищем ему индекс в предполагаемом отсортированном по аналогии с бинарным поиском, а потом вставляем. Но из-за того что ряд условий(if/elif/else) указано и это средства python, разница скорости сортировки различается от sorted +- в 200 раз. Мне интересен какой результат покажет если реализовать это на C/C++/C#.

Главным плюсом считаю, что алгоритм способен "досортирововать", ему не надо уже отсортированный список заново прогонять с новыми элементами. Только новые элементы ищут своё место в новом списке. Так что сортировку можно вести бесконечно, постоянно добавляя новые элементы. В теории не должен тратить много памяти, занимает x2 размера исходного списка.
