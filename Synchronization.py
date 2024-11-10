from Teacher_melody_processing import teacher_melody, min_per_t
from Children_melody_processing import children_melody, min_per_c
from math import floor


# Второй модуль
# Синхронизации мелодий и устранение временной разнесенности нот

counter_t = 0
counter_c = 0

# Смешанное значение частоты и длительности ноты, оно необходимо для проверки сигнала на отсутсвие какой-либо ноты в
# мелодии ученика или наличие лишних нот
all_t = []
all_c = []

# Значение частоты каждой ноты
freq_t = []
freq_c = []

# Длительность каждой ноты
t_m = []
c_m = []

# Разделение мелодии по нотам, каждая новая нота играется на другой частоте, соответсвенно
# происходит отсечение отрезков мелодии при переходе на новую частоту
# Кроме того, если нота длится менее 0.25 с, то она не учитывается
for i in range(0, len(teacher_melody)-1):
    if floor(teacher_melody[i]) == floor(teacher_melody[i+1]):
        counter_t += 1
    elif floor(teacher_melody[i]) != floor(teacher_melody[i+1]) and counter_t >= min_per_t:
        all_t.append(floor(teacher_melody[i]) + counter_t/100)
        freq_t.append(floor(teacher_melody[i]))
        t_m.append(counter_t)
        counter_t = 0
    else:
        counter_t = 0

for i in range(0, len(children_melody)-1):
    if floor(children_melody[i]) == floor(children_melody[i+1]):
        counter_c += 1
    elif floor(children_melody[i]) != floor(children_melody[i+1]) and counter_c >= min_per_c:
        all_c.append(floor(children_melody[i]) + counter_c/100)
        freq_c.append(floor(children_melody[i]))
        c_m.append(counter_c)
        counter_c = 0
    else:
        counter_c = 0
