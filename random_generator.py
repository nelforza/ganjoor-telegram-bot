import sqlite3
from poets_names import poets_fullnames_dic
from random import randint

def random_verse(poet):
    connect = sqlite3.connect('database.sqlite')
    cur = connect.cursor()
    select_poems = cur.execute('SELECT * FROM poems')
    poems = select_poems.fetchall()

    id = []
    for each_row in poems:
        if each_row[3] == '':
            continue

        url_feild = each_row[3]
        poet_name = url_feild.split('/')[3]
        if poet == poet_name:
            id.append(each_row[0])
    
    id_lenght = len(id)
    random_poemID =  randint(0, id_lenght)
    return id[random_poemID]

