from time import time
from random import randrange
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from main import sortirovka, clone_sorted

T_sortirovka = []
T_clone_sorted = []
T_sorted = []

res_mid_T_sortirovka = []
res_mid_T_clone_sorted = []
res_mid_T_sorted = []

len_list = [elem * 10000 for elem in range(1, 21)]

for count in len_list:
    TSka, TCSed, TSed = [], [], []

    for __ in range(10):
        # Было вначале не 10 а 100, но со своим пк очень долго ждать
        LS = [randrange(10000, 100000) for _ in range(count)]

        start = time()
        sortirovka(LS)
        TSka.append(time() - start)

        start = time()
        clone_sorted(LS)
        TCSed.append(time() - start)

        start = time()
        sorted(LS)
        TSed.append(time() - start)

    T_sortirovka.append(sum(TSka) / 10)
    T_clone_sorted.append(sum(TCSed) / 10)
    T_sorted.append(sum(TSed) / 10)

    print(f'Порядок {count} завершён.')

df = pd.DataFrame(np.array([T_sortirovka, T_clone_sorted, T_sorted]).T)
# df = pd.DataFrame.from_dict({'T_sortirovka': T_sortirovka, 'T_clone_sorted': T_clone_sorted, 'T_sorted': T_sorted})
df.columns = ['T_sortirovka', 'T_clone_sorted', 'T_sorted']
df.to_csv(f'statistics/stat2.csv')

fig = plt.figure(figsize=(50, 50))

graf_sortirovka = fig.add_subplot(221)
graf_sortirovka.plot(len_list, df['T_sortirovka'])
graf_sortirovka.set_title('Время sortirovka')
plt.xticks(len_list, [i for i in range(1, 21)])
plt.xlabel("Порядок 10е4")
plt.grid()

graf_clone = fig.add_subplot(222)
graf_clone.plot(len_list, df['T_clone_sorted'])
graf_clone.set_title('Время clone')
plt.xticks(len_list, [i for i in range(1, 21)])
plt.xlabel("Порядок 10е4")
plt.grid()

graf_sorted = fig.add_subplot(223)
graf_sorted.plot(len_list, df['T_sorted'])
graf_sorted.set_title('Время sorted')
plt.xticks(len_list, [i for i in range(1, 21)])
plt.xlabel("Порядок 10е4")
plt.grid()

plt.show()
