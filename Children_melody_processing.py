import librosa.feature
import numpy as np


# Применение первого модуля к мелодии обучающегося

cm, src = librosa.load('')
cmt, _ = librosa.effects.trim(cm, top_db=14)

cmt_mel = librosa.feature.melspectrogram(y=cmt, sr=src, n_mels=64)
cmt_db_mel = librosa.amplitude_to_db(cmt_mel)[4:9]

cmt_db_mel_transponsed = np.transpose(cmt_db_mel)
time_c = librosa.get_duration(S=cmt_mel, sr=src)
min_per_c = round(len(cmt_db_mel_transponsed))/(time_c*4)

children_melody = []

for i in cmt_db_mel_transponsed:
    counter = 0
    if all(map(lambda y: y < 0, i)):
        counter += 1
    else:
        max_index = [y for y, val in enumerate(i) if val == max(i)]
        children_melody.append(int(max_index[0]) + ((round(max(i))) / 100))
        if counter < min_per_c:
            while counter != 0:
                children_melody.append(float(max_index[0]))
                counter -= 1
        else:
            while counter != 0:
                children_melody.append(float(0))
                counter -= 1
