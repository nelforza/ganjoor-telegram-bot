import sqlite3
from poets_glossary import poets_name_glossary
from random import randint

def query(verse):
    connect = sqlite3.connect('database.sqlite')
    cur = connect.cursor()
    # Checking verse order in DB
    verse_order = int(verse[3])

    """
    each verse is in one field in DB, I have to check it's order so I can get next and previous
    related verses the random verse chosen by user.
    """
    order_count = 1 # Helps me to see how many times While_loop has been run.
    while True:
        new_id = (verse[0] + order_count) # Get the next verse of the random verse
        order = cur.execute('SELECT * FROM verses WHERE id = ?', (new_id,))
        order_query = order.fetchone()
        if order_query[3] == 0: # checks if the next verse is related to random one
            break 
        else:
            order_count += 1

    # Total verses of the random poem        
    order_sum = verse_order+order_count 

    poem = []
    for i in range(verse[0], (verse[0] + order_sum)):
        Select_whole_poem = cur.execute('SELECT * FROM verses WHERE id = ?', (i,))
        fetch_poem = Select_whole_poem.fetchone()
        verses = str(fetch_poem[4])
        poem.append(verses)



    return (poem)
