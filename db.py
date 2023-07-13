from decouple import config
import pymysql
import helpers

req_params = ['DB_HOST', 'DB_USER', 'DB_PASS', 'DB']
helpers.check_config(config, req_params)


# try:
#    connection = pymysql.connect(
#        host=DB_HOST,
#        user=DB_USER,
#        password=DB_PASS,
#        database=DB
#    )
# except:

#    may be need probros...
#    предупреждаем выводом
#    try check config
#       try делаем проброс
#       
#       except
#         проброс не получился
#    except 
#    нет конфига для проброса и не доступен локальный майскюэль..конец

# try:
#     # Устанавливаем соединение с базой данных
#     connection = pymysql.connect(
#         host="localhost",  # Хост базы данных
#         user="пользователь",  # Имя пользователя
#         password="пароль",  # Пароль
#         database="название_базы_данных"  # Имя базы данных
#     )

#     # Создаем объект "курсора" для выполнения SQL-запросов
#     cursor = connection.cursor()

#     # Выполняем SELECT-запрос
#     query = "SELECT * FROM имя_таблицы"
#     cursor.execute(query)

#     # Получаем результаты запроса
#     results = cursor.fetchall()

#     # Выводим результаты на экран
#     for row in results:
#         print(row)

# except pymysql.Error as e:
#     print("Ошибка при подключении к базе данных MySQL:", e)

# finally:
#     # Закрываем соединение с базой данных
#     if cursor:
#         cursor.close()
#     if connection:
#         connection.close()


def find_servers(names):
    print(names[0])
    print(names[1])
    return ['server1', 'server2']
