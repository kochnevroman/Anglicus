import pyodbc
import os.path
import csv
import time
import pandas as pd

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

# Занести новое слово в пользовательский словарь
def Set_word_at_dictionary(word, translate):
    dictionary_file = open(my_dictionary_path, "r")
    reader = csv.reader(dictionary_file)
    for row in reader:
        if(row[0] == word):
            print("Such a word is already in the dictionary")
            dictionary_file.close()
            return 0

    dictionary_file = open(my_dictionary_path, "a", newline='')
    s = word + "," + translate + "\n"
    dictionary_file.writelines(s)
    dictionary_file.close()
   
# Вывод случайного слова определённого уровня на экран
def Card_get_word():
    s = 'declare @min_difficulty_lvl int\n'
    s = s + 'declare @max_difficulty_lvl int\n'
    s = s + 'declare @result nvarchar(2)\n'

    s = s + 'set @result = (select Achievment.language_lvl from Achievment, [User]\n'
    s = s + 'where ((Achievment.id = [User].achievment_id) and ([User].mail = ?) and ([User].password = ?)))\n'

    s = s + "if(@result = 'A2')\n"
    s = s + "   begin\n"
    s = s + "	    set @min_difficulty_lvl = 1\n"
    s = s + "	    set @max_difficulty_lvl = 3\n"
    s = s + "   end\n"
    s = s + "if(@result = 'B1')\n"
    s = s + "   begin\n"
    s = s + "	    set @min_difficulty_lvl = 4\n"
    s = s + "	    set @max_difficulty_lvl = 8\n"
    s = s + "   end\n"
    s = s + "if(@result = 'B2')\n"
    s = s + "   begin\n"
    s = s + "	    set @min_difficulty_lvl = 9\n"
    s = s + "	    set @max_difficulty_lvl = 12\n"
    s = s + "   end\n"

    s = s + "select top 1 * from Dictionary\n"
    s = s + "where (([Dictionary].difficulty_lvl >= @min_difficulty_lvl) and ([Dictionary].difficulty_lvl <= @max_difficulty_lvl))\n"
    s = s + "order by newid()"

    cursor.execute(s, mail, password)
    row = cursor.fetchone()
    print(row)

    return row.word, row.definition, row.translation

# Загрузка текущих для изучения слов в пользовательский файл
def Load_words():
    if(not os.path.exists(dictionary_path)):
        s = 'declare @min_difficulty_lvl int\n'
        s = s + 'declare @max_difficulty_lvl int\n'
        s = s + 'declare @result nvarchar(2)\n'

        s = s + 'set @result = (select Achievment.language_lvl from Achievment, [User]\n'
        s = s + 'where ((Achievment.id = [User].id) and ([User].mail = ?) and ([User].password = ?)))\n'

        s = s + "if(@result = 'A2')\n"
        s = s + "   begin\n"
        s = s + "	    set @min_difficulty_lvl = 1\n"
        s = s + "	    set @max_difficulty_lvl = 3\n"
        s = s + "   end\n"
        s = s + "if(@result = 'B1')\n"
        s = s + "   begin\n"
        s = s + "	    set @min_difficulty_lvl = 4\n"
        s = s + "	    set @max_difficulty_lvl = 8\n"
        s = s + "   end\n"
        s = s + "if(@result = 'B2')\n"
        s = s + "   begin\n"
        s = s + "	    set @min_difficulty_lvl = 9\n"
        s = s + "	    set @max_difficulty_lvl = 12\n"
        s = s + "   end\n"

        s = s + "select * from Dictionary\n"
        s = s + "where (([Dictionary].difficulty_lvl >= @min_difficulty_lvl) and ([Dictionary].difficulty_lvl <= @max_difficulty_lvl))"

        cursor.execute(s, mail, password)

        dictionary = open(dictionary_path, "w")
        row = cursor.fetchone()

        value = "id,word,time,marker\n"
        dictionary.write(value)

        while(not row is None):
            value = str(row.id) + ',' + str(row.word) + ',' + str(time.time()) + ',' + '-1' + '\n'
            dictionary.write(value)
            row = cursor.fetchone()
        dictionary.close()

# Изменить маркер слова при сдвиге карточки
def Swap(swap_type, word_name):
    dictionary_file = open(dictionary_path, "r")
    reader = csv.reader(dictionary_file)
    i = 0
    for row in reader:
        if(row[1] == word_name):
            print("I find this word")
            dictionary_file.close()
            break
        i = i + 1

    print("i = ", i)

    file = pd.read_csv(dictionary_path, sep = ',')
    if(swap_type == "left"):
        file.loc[i, 'marker'] = str(0)
    if(swap_type == "right"):
        if((time.time() - file.loc[i, 'time']) <= (60 * 60 * 24 * 3)):
            file.loc[i, 'marker'] = 1
        elif((time.time() - file.loc[i, 'time']) <= (60 * 60 * 24 * 14)):
            file.loc[i, 'marker'] = 2
        elif((time.time() - file.loc[i, 'time']) <= (60 * 60 * 24 * 30)):
            file.loc[i, 'marker'] = 3
        else:
            file.loc[i, 'marker'] = 4
    file.loc[i, 'time'] = time.time()
    print(file.loc[i])

    file.to_csv(dictionary_path, index = False)



server = 'den1.mssql8.gear.host'
db = 'englishteacher'
usr = 'englishteacher'
psword = 'Rt0b2!c9Um_i'

conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=' + server + ';''DATABASE=' + db + ';UID=' + usr + ';PWD=' + psword)
cursor = conn.cursor()

dictionary_path = "dictionary.csv"
my_dictionary_path = "my_dictionary.csv"

word = "my_word_2"
translate = "моё_слово_2"

mail = 'novitskiy@gmail.com'
password = '1Qwerty2'

#Load_words()
#Swap("left", "absorb")
Card_get_word()
#Set_word_at_dictionary(word, translate)

#result = login_check('novitskiy@gmail.com', '1Qwerty2')
#print(result)