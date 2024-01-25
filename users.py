import uuid
from datetime import datetime

user_brenno = {
    'id':str(uuid.uuid4()),
    'created_at':datetime.now().isoformat(timespec='seconds'),
    'nome':'Brenno',
    'sobrenome':'Vieira',
    'idade':20,
    'email':'brenno.vieira@hotmail.com'
}

user_bruno = {
    'nome':'Bruno',
    'sobrenome':'Vieira',
    'idade':43,
    'email':'vieira.es@gmail.com'
}

user_fulano = {
    'nome':'Fulano',
    'sobrenome':'Ciclano',
    'idade':17,
    'email':'fulano@email.com'
}