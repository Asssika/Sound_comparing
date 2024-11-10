from Teacher_melody_processing import teacher_melody
from Children_melody_processing import children_melody
from Synchronization import all_t, all_c, c_m, t_m, freq_c, freq_t
from math import floor


# Третий модуль
# Проверка мелодий на лишние или отсутствующие ноты, работает таким образом:
# Если количество нот в мелодиях не равно, то запускается алгоритм, сравнивающий частоты нот,
# если частоты не равны, то алгоритм проверяет соответсвие частот следующих двух нот, учитывая предполагаемую лишнюю.
# При выявлении лишней ноты в мелодии,в другую мелодию будет добавлена нота, в будущем отображаемая на гарфике ошибочной
# Также в модуле происходит выравнивание длин мелодий

exec_t = []
exec_c = []
if len(all_t) != len(all_c) and len(all_t) < len(all_c):
    for i in range(0, len(all_t)-3):
        if all_c[i] != all_t[i] and all_c[i+1: i+3] == all_t[i: i+2]:
            exec_c.append[i + all_c % 1]
        elif all_c[i] != all_t[i] and all_c[i: i+2] == all_t[i+1: i+3]:
            exec_t.append[i + all_t % 1]
elif len(all_t) != len(all_c) and len(all_t) > len(all_c):
    for i in range(0, len(all_c)-4):
        if all_c[i] != all_t[i] and all_c[i+1: i+3] == all_t[i: i+2]:
            exec_c.append[i + all_c % 1]
        elif all_c[i] != all_t[i] and all_c[i: i+2] == all_t[i+1: i+3]:
            exec_t.append[i + all_t % 1]

while len(exec_c) != 0:
    t_m.insert(floor(exec_c[0]), 1)
    freq_t.inset(floor(exec_c[0]), 6)
    exec_c = exec_c[1:]
    exec_c = list(map(lambda y: y + 1, exec_c))

while len(exec_t) != 0:
    c_m.insert(floor(exec_t[0]), 1)
    freq_c.inset(floor(exec_t[0]), 6)
    exec_t = exec_t[1:]
    exec_t = list(map(lambda y: y+1, exec_t))

# Выравние характеристик по длине
while len(teacher_melody) != len(children_melody):
    if len(teacher_melody) > len(children_melody):
        children_melody.append(float(0))
    elif len(teacher_melody) < len(children_melody):
        teacher_melody.append(float(0))

while len(freq_c) != len(freq_t):
    if len(freq_t) > len(freq_c):
        freq_c.append(0)
    elif len(freq_t) < len(freq_c):
        freq_t.append(0)

while len(t_m) != len(c_m):
    if len(t_m) > len(c_m):
        c_m.append(1)
    elif len(t_m) < len(c_m):
        t_m.append(1)
