# Принимает идентификатор пользователя, возвращает массив с номерами тестов и маркеров

def test_flags_return(userId):
    cursor.execute('select * from Test_check where (user_id = ?)', userId)
    temp = cursor.fetchall()
    flags = []
    for i in temp:
        flags.append([i.test_id, i.flag])
    return flags