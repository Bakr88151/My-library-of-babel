from string import ascii_lowercase
import random
import sqlite3


def create_page():
    page = ''

    for _ in range(3200):
        is_space = random.randint(1,5)
        page += random.choice(list(ascii_lowercase))
        if is_space == 1:
            page += ' '
    save_page(page)
    return page


def save_page(content:str):
    db = sqlite3.connect('bable.db')
    cur = db.cursor()
    command = 'INSERT INTO pages(content) VALUES(?)'
    data_to_insert = (f"{content}",)

    cur.execute(command, data_to_insert)
    db.commit()
    db.close()


def search_page(content:str):
    res = []
    db = sqlite3.connect('bable.db')
    cur = db.cursor()
    command = 'SELECT id, date FROM pages WHERE content LIKE ? LIMIT 10'
    data_to_insert = (f"%{content}%",)
    cur.execute(command, data_to_insert)

    rows = cur.fetchall()
    columns = [column[0] for column in cur.description]

    for row in rows:
        result_dict = dict(zip(columns, row))
        res.append(result_dict)
    
    db.close()
    return res


def get_page(id: int):
    db = sqlite3.connect('bable.db')
    cur = db.cursor()

    # Use a tuple for the parameter
    data_to_insert = (id,)

    command = 'SELECT content, date FROM pages WHERE id = ?'
    cur.execute(command, data_to_insert)

    row = cur.fetchone()

    # Check if there's a result
    if row is not None:
        columns = [column[0] for column in cur.description]
        result_dict = dict(zip(columns, row))
    else:
        result_dict = {}  # or you can raise an exception, or handle the case as needed

    db.close()
    return result_dict


if __name__ == '__main__':
    print(search_page('i am happy'))