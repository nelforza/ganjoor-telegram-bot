
import sqlite3
from poets_names import poets_fullnames_dic, poets_names_list
from verse_query import query
from random_generator import random_verse

def msg_poem(msg, length):
    connect = sqlite3.connect('database.sqlite')
    cur = connect.cursor()
    # Searching for English name of the poet which user has given it in Persian
    search_for_poet_key = [(k, v) for (k, v) in poets_fullnames_dic.items() if msg in v]
    # Accessing the poet English name from a tuple inside a list
    poet = [x[0] for x in search_for_poet_key][0]
    # Finding a relevant random Poem ID
    random_poem_id = random_verse(poet)  
    verse_id = cur.execute('SELECT * FROM verses WHERE poemId = ?', (random_poem_id,))
    verse = verse_id.fetchone()
    # Query for the random Poem ID to find the whole poem
    poem = query(verse, length)
    return poem
