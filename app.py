import json

from users import *
from wallets import *

apresentacao = {
    'data':[
        {'user':user_brenno,
        'wallet':wallet_brenno},
        {'user':user_bruno,
        'wallet':wallet_bruno},
        {'user':user_fulano,
        'wallet':wallet_fulano}
        ]
}

formatted_json = json.dumps(apresentacao, indent=4)

print(formatted_json)