import librosa.feature
import numpy as np


# Первый модуль
# Приведение мелодии к виду, пригодному для обработки

# Загрузка аудиозаписи и образание шумов в начале и конце мелодии
tm, srt = librosa.load('')
tmt, _ = librosa.effects.trim(tm, top_db=14)

# Расчет мел-спектрограммы, вывод матрицы значений
tmt_mel = librosa.feature.melspectrogram(y=tmt, sr=srt, n_mels=64)
tmt_db_mel = librosa.amplitude_to_db(tmt_mel)[4:9]

# Подготовка матрицы к обработке
tmt_db_mel_transponsed = np.transpose(tmt_db_mel)

# Расчет длительности мелодии
time_t = librosa.get_duration(S=tmt_mel, sr=srt)
min_per_t = round(len(tmt_db_mel_transponsed))/(time_t*4)

# Цикл возвращает списоком последовательность значений всей аудиозаписи;
# При этом если длительность звучания меньше четверти секунды,
# то алгоритм будет принимать это значение равным по уровню частоты предыдущим значениям,
# но по уровню громкости они будут равны 0;
# целая часть числа - порядок мела(соответствует частоте)
# дробная часть числа - уровень сигнала в данный момент

teacher_melody = []

for i in tmt_db_mel_transponsed:
    counter = 0
    if all(map(lambda y: y < 0, i)):
        counter += 1
    else:
        max_index = [y for y, val in enumerate(i) if val == max(i)]
        teacher_melody.append(int(max_index[0]) + ((round(max(i))) / 100))
        if counter < min_per_t:
            while counter != 0:
                teacher_melody.append(float(max_index[0]))
                counter -= 1
        else:
            while counter != 0:
                teacher_melody.append(float(0))
                counter -= 1
