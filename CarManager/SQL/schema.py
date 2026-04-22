from . import init_db


def create_tables():
    conec = init_db.get_connection()
    cursor = conec.cursor()

    query = '''--sql
    CREATE TABLE IF NOT EXISTS CarManager(
        owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner_name TEXT CHECK(length(owner_name) <= 90) NOT NULL,
        owner_age INTEGER NOT NULL,
        car_maker TEXT CHECK(length(car_maker) <= 50) NOT NULL,
        car_model TEXT CHECK(length(car_model) <= 50) NOT NULL,
        car_color TEXT CHECK(length(car_color) <= 60) NOT NULL,
        car_price REAL NOT NULL
    )
    '''
    conec.execute(query)
    conec.commit()
    conec.close()
