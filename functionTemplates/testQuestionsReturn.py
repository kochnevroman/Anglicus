# Принимает номер темы (теста). Возвращает массив из 10 случайно выбранных записей из таблицы по указанной теме
import numpy as np

def test_questions_return(themeId):
    cursor.execute('select * from Question where (theme_id = ?)', themeId)
    temp = cursor.fetchall()
    indices = np.arange(len(temp))
    np.random.shuffle(indices)
    questions = []
    for i in indices[0:10]:
        questions.append(temp[i])
    return questions