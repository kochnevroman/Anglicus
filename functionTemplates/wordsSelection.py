# Принимает на вход уровень слова, возвращяет все слова этого уровня

def words_selection(lvl):
    cursor.execute('select * from [Dictionary] where (difficulty_lvl = ?)', lvl)
    return cursor.fetchall()
