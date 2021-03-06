# -*- coding: utf-8 -*-
"""06_Intro_to_Pandas_I_homework.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cj1OY1pTOW3Hfjcqlq87rJQRWn9Ohh0n

# Обработка данных с Pandas
"""

import pandas as pd
from google.colab import files

"""### Задача 1.1

Импортируйте библиотеку pandas и создайте pandas dataframe как на картинке ниже

<img src="06_intro_to_Pandas_I.jpg">
"""

columns = ['Year', 'Movie Name', 'Rating', 'Votes', 'Genre', 'RunTime', 'Director']
index = [1, 2, 3, 4]
data =  [[2015, 'Bajirao Mastani', 7.2, 17362, 'Drama', 158, 'Sanjay Leela Bhansali'],
     [2014, 'Queen', 8.4, 39518, 'Drama', 146, 'Vikas Bahl'],
     [2013, 'Bhaag Milkha Bhaag', 8.3, 39731, 'Drama', 186, 'Rakeysh Omprakash Mehra'],
     [2012, 'Barfi!', 8.2, 52308, 'Family', 151, 'Anurag Basu']]

df = pd.DataFrame(data, columns=columns, index=index)
df

"""### Задача 1.2

Для таблички выше, найдите все фильмы в жанре "Drama"
"""

print(df.loc[df['Genre'] == 'Drama'])

"""### Задача 1.3

Посчитайте средний рейтинг фильмов в жанре "Drama"
"""

dram = df.loc[df['Genre'] == 'Drama']
print(dram['Rating'].mean())

"""### Задача 1.4 

Посчитайте средневзвешенный рейтинг всех фильмов в жанре "Drama". Взвешивать рейтинг будем на кол-во голосов (Votes).

P.S. конкретно нужно посчитать: $$\frac{\sum{Rating_i * Votes_i}}{\sum{Votes_i}}$$

Используем только встроенные методы библиотеки pandas
"""

dram['Rating'].sum() * dram['Votes'].sum()/ dram['Votes'].sum()

"""### Задача 2

Используя соответствующую функцию библиотеки pandas, подгрузите датасет 'train.csv' из .csv файла. Выведите на экран первые 5 строчек файла (метод head)
"""

file = files.upload()

!ls

data = pd.read_csv('train (1).csv')
data.head(5)

"""### Задача 3

Для подгруженного датасета из предыдущей задачи:
* посчитайте сколько записей
* определите тип данных в каждом столбце
* проверьте, есть ли пропуски

P.S. используйте соответствующие встроенные методы
"""

data.count()

data.shape

data.info()

data.dtypes

data.isnull().sum()

data.isnull().sum().sum()

data.isnull().sum().sum()/data.size

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

fig, ax = plt.subplots(figsize=(20,12))
sns_heatmap = sns.heatmap(data.isnull(), yticklabels = False, cbar = False, cmap = 'viridis')
plt.show()

"""### Задача 4

Используя соответствующий встроенный метод, выведите на экран описательные статистики для датасета из предыдущей задачи.
"""

data.describe()

data.describe(include=['O'])

"""## Задачи PRO

### Задача 5

Используя соответствующий встроенный метод, "дропните", т.е. удалите из нашей таблички все столбцы, у которых кол-во пропущенных значений больше 200.

* найдите все такие столбцы (метод .isna() + подвыборка с условием)
* определите их названия (поймите как выцепить названия и сохраните их в массив, т.е. по цепочке примените методы .index, .tolist() или .values)
* "дропните их" (используйте метод .drop(имена столбцов))
* результат сохраните в новой табличке (например, data_1), исходную менять не нужно
"""

data.isna().sum()

mask = data.isna().sum() > 200
sp = mask[lambda n : n].index.tolist()

sp

data_1 = data.drop(sp, axis=1, inplace=False)

data_1.isna().sum()

data_1

data.isna().sum()

"""#### Задача 6

В финальном датасете из прошлой задачи "дропните" все строки с пропусками в данных, используйте соответствующий встроенный метод (.dropna()). В этой задаче, в отличие от предыдущей, выполните операцию "inplace", т.е. измените исходную таблицу.
"""

data.dropna(axis=1, how='any', inplace=True)
data.isna().sum()

data.head()

"""### Задача 7

Данные, с которыми мы работаем в этом домашнем задании, содержат информацию о проданных домах. В табличке из прошлой задачи найдите все дома, проданные в 2007 году, у которых цена продажи выше 300000 и есть бассейн. Для подвыборки с указанными условиями сначала создайте маску.

* цена продажи SalePrice
* год продажи YrSold
* наличие бассейна можно определить по столбцу PoolArea
"""

SalePrice = data['SalePrice'] > 300000
YrSold = data['YrSold'] == 2007
PoolArea = data['PoolArea'] > 0

cen = data[SalePrice & PoolArea]
cen

"""### Задача 8

Создайте сводную таблицу, содержащую информацию о средней цене дома и средней площади дома в разбивке по типам зон и общей форме собственности.

* типы зон - MSZoning
* типы форм собственности - LotShape
"""

data_3 = data.groupby(['MSZoning', 'LotShape'])[['LotArea', 'SalePrice']].mean()
data_3

"""### Задача 9

Добавьте к табличке data_1 новый столбец с названием 'Flag'. Присвойте ему значения 0 или 1 в случайном порядке. Для этого:
    
* создайте одномерный массив из случайных целых чисел 0 или 1
* размер массива должен соответствовать кол-ву наблюдений в основной табличке
* создайте новый столбец и присвойте ему значения одномерного массива
"""

import numpy as np
import scipy as sp
import random
data_1.shape

np.random.seed(42)
A = np.random.randint(0, 2, 1460)
A

data_1['Flag'] = A
data_1.shape

data_1

"""### Задача 10

В прошлой задаче мы создали новый столбец "Flag". Будем считать, что это индикатор продажи дома, т.е. дом был продан, если 1, и не был продан, если 0.

Создайте сводную таблицу, которая содержит информацию о сумме продаж домов (SalePrice) за все года (YrSold). Проданными домами будем считать только те дома, где Flag = 1.
"""

data_1.head()

data_1.pivot_table(values=['SalePrice', 'YrSold'], index=['Flag'])

"""### Задача 11

Используя встроенный метод .hist, нарисуйте гистограмму распределения площади домов (LotArea) с параметром кол-во бинов = 60.
"""

data_1.hist(column='LotArea', bins=60)

data_1['LotArea'].plot()