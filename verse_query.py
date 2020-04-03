import sqlite3
from poets_names import poets_fullnames_dic

def relevant_verse_finder(break_point, verse_order, verse):
    connect = sqlite3.connect('database.sqlite')
    cur = connect.cursor()
    """
    each verse is in one field in DB, I have to check it's order so I can get next and previous
    related verses the random verse chosen by user.
    """
    order_count = 1 # Helps me to see how many times While_loop has been run.
    while True:
        new_id = (verse[0] + order_count) # Get the next verse of the random verse
        order = cur.execute('SELECT * FROM verses WHERE id = ?', (new_id,))
        order_query = order.fetchone()
        if order_query[2] == break_point: # checks if the next verse is related to random one
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

        ## Query for the Poet name and Poem category
    Poem_ID = verse[1]
    select_poems = cur.execute('SELECT * FROM poems WHERE id = ?', (Poem_ID,))
    query_poems = select_poems.fetchone()


    # Poem category
    category_id = int(query_poems[1])
    select_category  = cur.execute('SELECT * FROM categories WHERE id = ?', (category_id,))
    fetch_category = select_category.fetchone()
    poem_category = fetch_category[2]
    if poem_category not in poets_fullnames_dic.values() :    
        poem.insert(0, str(poem_category))

    # poet name
    url = str(query_poems[3])
    if bool(url) == True:
        poet_name = url.split('/')[3]
        poet_name = poets_fullnames_dic[poet_name]
        poem.insert(0, poet_name)


    return poem

def query(verse, length):
    # Checking verse order in DB
    if length == 'long':
        return relevant_verse_finder(break_point=1, verse_order=int(verse[2]), verse=verse)
    elif length == 'short':
        return relevant_verse_finder(break_point=0, verse_order=int(verse[3]), verse=verse)
    
    



