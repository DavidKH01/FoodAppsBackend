import database_connect

connect, cursor, db = database_connect.get_db()

def test_select():
    cursor.execute('SELECT * FROM restaurants')
    print(cursor.fetchall())
    # connect.commit()


def test_insert():
    cursor.execute('INSERT INTO restaurants(id, name, price_range, address, opening_time, closing_time) VALUES (%s, %s, %s,%s,%s, %s)', (3, "Pizza Hut", "$$", "123 Main St", "10:00", "22:00"))
    connect.commit()



test_select()
test_insert()
test_select()