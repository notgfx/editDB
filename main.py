import sqlite3

db_name = 'the_base.db'
db_table_name = 'customers'

with sqlite3.connect(db_name) as connect_db:
    # connect_db.row_factory = sqlite3.Row #for raw view
    cursor = connect_db.cursor()

    commit = connect_db.commit()


    def all_rows():
        return cursor.fetchall()


    def one_row():
        return cursor.fetchone()


    def x_rows(x):
        return cursor.fetchmany(x)


    def show_all_rows():
        cursor.execute(f"SELECT * FROM {db_table_name}")
        print(all_rows())


    def input_data():
        global input_user_id
        input_user_id = input('input_user_id: ')
        return input_user_id


    def add_db_line():
        input_data()
        cursor.execute(f"INSERT OR IGNORE INTO '{db_table_name}' (user_id) VALUES (?)", (input_user_id))
        print("Запись, якобы, добавлена.")
        commit


    def create_table_if_not_exists():
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {db_table_name} (
        serial_customers,
        user_id,
        user_sub
    );""")
        commit


    def add_customer(user_id):
        cursor.execute(f"INSERT INTO '{db_table_name}' (user_id) VALUES (?)", (user_id,))
        commit


    def delete_db():  # not work with sqlite3
        cursor.execute(f'DROP DATABASE IF EXISTS {db_name}')
        commit


    def delete_db_table():
        delete_db_table_approve = input('Are you sure? (y/n)\n')
        if delete_db_table_approve.lower() == 'y':
            cursor.execute(f'DROP TABLE IF EXISTS {db_table_name}')
            print(f'Done, table "{db_table_name}" is deleted.')
            commit
        else:
            print(f'Alright, table "{db_table_name}" is NOT deleted')


    # delete_db_table() #удаляем таблицу из базы
    create_table_if_not_exists() #создаем таблицу, если ее нет
    # add_customer('123') #добавляем в базу клиента
    # add_db_line()  # должно добавить в базу строчку с данными из инпута
    commit #сохраняем изменения бд еще раз, на всякий
    #show_all_rows()

add_customer('321')
commit
show_all_rows()