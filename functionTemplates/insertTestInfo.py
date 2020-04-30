# Принимает информацию, заносит ее в таблицу Test_check

def insert_test_info(userId, testId, flag, date):
    cursor.execute('insert into Test_check(user_id, test_id, flag, date_of_completion) values(?,?,?,?)', userId,
                   testId, flag, date)

