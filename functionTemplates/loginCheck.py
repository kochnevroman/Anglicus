
def login_check(uLogin, uPassword):
    cursor.execute('select * from [User] where (mail = ?)', uLogin)
    row = cursor.fetchone()

    if row is None:
        print('No such user')
        return False

    if row.password == uPassword:
        return True
    else:
        print('Wrong password')
        return False


# Принимает на вход логин и пароль. Возвращает int

def login_check(uLogin, uPassword):
    cursor.execute('select * from [User] where (mail = ?)', uLogin)
    row = cursor.fetchone()

    if row is None:
        # Если пользователя нет
        return 0

    if row.password == uPassword:
        # Если пользователь есть
        return 1
    else:
        # Если пароль неверный
        return 2
