import math
from statistics import mean


def corr_pearson(list_1, list_2):
    if (len(list_1) == len(list_2)):
        den = 0
        m_x = mean(list_1) # Среднее значение первого массива
        m_y = mean(list_2) # Среднее значение второго массива
        num = sum(list(map(lambda x, y: (x-m_x)*(y - m_y), list_1, list_2))) # Вычисление числителя
        den = math.sqrt(sum(list(map(lambda x: (x-m_x)**2, list_1)))
                        * sum(list(map(lambda y: (y-m_y)**2, list_2)))) # Вычисление знаменателя
        return num/den
    else: 
        return "Массивы должны быть одинаковой длины!"


l_1 = [1, 2, 3, 4, 6, 7]

l_2 = [10, 20, 29, 40, 52, 40]

print(corr_pearson(l_1, l_2))


