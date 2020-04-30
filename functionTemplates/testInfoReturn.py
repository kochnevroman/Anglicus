# Возвращает массив с названиями тем тестов

def test_info_return():
    cursor.execute('select * from [Test]')
    temp = cursor.fetchall()
    names = []
    for i in temp:
        names.append([i.theme, i.desctiption])
    return names
