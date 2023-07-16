from decouple import config
import pymysql
import helpers
import socket
from sshtunnel import SSHTunnelForwarder

def is_port_close(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    try:
        return sock.connect_ex(('127.0.0.1', port))
    except socket.error as e:
        print(f"Ошибка при проверке порта: {e}")
    finally:
        sock.close()


def ssh_port_forwarding(config):
    try:
        tunnel = SSHTunnelForwarder(
            (config('SSH_DB_HOST'), 22),
            ssh_username=config('SSH_DB_USER'),
            ssh_pkey=config('SSH_DB_KEY'),
            remote_bind_address=('127.0.0.1', 3306),
            local_bind_address=('127.0.0.1', 3306)
        )
        tunnel.start()
    except Exception as e:
        print("Ошибка создания туннеля")


if config('USE_SSH_FORWARDING') == 'true':
    if is_port_close(3306):
        req_params = ['SSH_DB_HOST', 'SSH_DB_USER', 'SSH_DB_KEY']
        helpers.check_config(config, req_params)
        ssh_port_forwarding(config)

req_params = ['DB_HOST', 'DB_USER', 'DB_PASS', 'DB', 'USE_SSH_FORWARDING']
helpers.check_config(config, req_params)

try:
    connection = pymysql.connect(
    host=config('DB_HOST'),
    user=config('DB_USER'),
    password=config('DB_PASS'),
    database=config('DB')
    )
    cursor = connection.cursor()
    query = "SELECT * FROM имя_таблицы"
    cursor.execute(query)
    results = cursor.fetchall()


except pymysql.Error as e:
     print("Ошибка при подключении к базе данных MySQL:", e)

finally:
     if cursor:
         cursor.close()
     if connection:
         connection.close()


def find_servers(names):
    print(names[0])
    print(names[1])
    return ['server1', 'server2']
