from decouple import config

try:
    CONNECTOR = config('CONNECTOR')
except:
    print('CONNECTOR option not set')
    exit()

if CONNECTOR == 'db':
    import db
    CONNECTOR = db
else:
    print('Not set or wrong type of connector')
    exit()


def find(name, fix_name):
    result = CONNECTOR.find_servers(name, fix_name)
    print(result)