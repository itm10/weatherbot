import psycopg2


def connect():
    con = psycopg2.connect(
        dbname='p15_db',
        user='postgres',
        password='postgres',
        host='localhost',
        port=5432
    )
    return con


def insert_data(data: dict):
    con = connect()
    cur = con.cursor()
    query = """
        insert into create_user_table(phone,first_name,last_name,address) 
        values (%s,%s,%s,%s)
    """
    values = (data['phone'], data['first_name'], data['last_name'], data['address'])
    cur.execute(query, values)
    con.commit()


def is_exist(names, phone):
    con = connect()
    cur = con.cursor()
    query = f"""
        select * from create_user_table
        where last_name=%s and phone=%s 
    """
    values = (names, phone)
    cur.execute(query, values)
    return bool(cur.fetchone())
