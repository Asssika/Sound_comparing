from Teacher_melody_processing import teacher_melody
from Children_melody_processing import children_melody, time_c
from Add_delete_note import freq_t, freq_c
from Add_delete_note import t_m, c_m
from math import floor


# Четвертый модуль
# Сравнение характеристик, полученных из мелодий обучающегося и преподавателя
# Вывод итоговых значений

def res_character(x, time):
    y = []
    time = round(time, 2)
    count_of_values = round(time*4)
    compared = round(len(x)/count_of_values)
    while len(x) > compared:
        c = sum(x[0:compared])/compared
        if c >= 0.5:
            y = y + [1]
            x = x[compared+1:]
            c = 0
        else:
            y = y + [0]
            x = x[compared+1:]
            c = 0
    if len(x) != 0:
        c = sum(x)/len(x)
    if c >= 0.5:
        y = y + [1]
    else:
        y = y + [0]
    return y


# Сравнение ритма
res_rhythm = []
for i in range(0, len(t_m)):
    if abs((t_m[i]-c_m[i])/t_m[i]) <= 0.25:
        res_rhythm = res_rhythm + list([0 for i in range(c_m[i])])
    elif t_m[i] < c_m[i]:
        res_rhythm = res_rhythm + list([0 for i in range(t_m[i])]) + list([1 for i in range(abs(c_m[i] - t_m[i]))])
    elif t_m[i] > c_m[i]:
        res_rhythm = res_rhythm + list([0 for i in range(c_m[i])]) + list([1 for i in range(abs(t_m[i] - c_m[i]))])


# Сравнение громкости
res_loud = []
teacher_melody = list(map(lambda y: round((y % 1)*100), teacher_melody))
children_melody = list(map(lambda y: round((y % 1)*100), children_melody))
counter_t = 0
counter_c = 0
for i in range(0, len(t_m)):
    if sum(teacher_melody[counter_t:t_m[i] + counter_t]) != 0 and abs(1-(((sum(children_melody[counter_c:c_m[i] + counter_c]))/c_m[i])/(sum(teacher_melody[counter_t:t_m[i] + counter_t])/t_m[i]))) <= 0.25:
        res_loud = res_loud + list([0 for i in range(c_m[i])])
        counter_c += c_m[i]
        counter_t += t_m[i]
    else:
        res_loud = res_loud + list([1 for i in range(c_m[i])])
        counter_c += c_m[i]
        counter_t += t_m[i]


# Сравнение текущей громкости со средней громкостью всей мелодии
res_average = []
count_c = round(len(children_melody)/time_c)*5
time = floor(len(children_melody)/count_c)
average_c = []
while time != 0:
    average_c.append(sum(children_melody[0:count_c])/count_c)
    children_melody = children_melody[count_c+1:]
    time -= 1
if len(children_melody) != 0:
    average_c.append(sum(children_melody)/len(children_melody))
max_c = max(children_melody)
for i in range(0, len(average_c)):
    res_average.append(round(children_melody[i]/max_c, 2))

# Сравнение частот
res_frequency = []
for i in range(0, len(freq_t)):
    if freq_t[i] == freq_c[i]:
        res_frequency = res_frequency + list([0 for i in range(c_m[i])])
    else:
        res_frequency = res_frequency + list([1 for i in range(c_m[i])])


# Результаты сравнений, приведенные по времени
integral_indicator = 1 - round(sum(list(res_rhythm + res_frequency + res_loud))/len(list(res_rhythm + res_frequency + res_loud)), 2)
rhythm = res_character(res_rhythm, time_c)
height = res_character(res_frequency, time_c)
volume1 = res_character(res_loud, time_c)
volume2 = res_average
