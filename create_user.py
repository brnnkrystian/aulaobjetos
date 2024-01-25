from datetime import datetime
import uuid
import time

db_users = []

def create_user(name):
    user = {
        'id':str(uuid.uuid4()),
        'name':name,
        'created_at':datetime.now().isoformat()
    }
    db_users.append(user)
    return user

create_user('Brenno')
time.sleep(1)
create_user('Bruno')
time.sleep(1)
create_user('Isabelly')

print(db_users)