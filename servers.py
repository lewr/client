from decouple import config
import helpers

req_params=['CONNECTOR']
helpers.check_config(config, req_params)

if config('CONNECTOR') == 'db':
    import db
    CONNECTOR = db
elif config('CONNECTOR') == 'api':
    import api
    CONNECTOR = api
else:
    print('Not set or wrong type of connector')
    exit()

def search(names):
    result = CONNECTOR.find_servers(names)
    return(result)