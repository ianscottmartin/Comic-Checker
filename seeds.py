from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data.db')

Session = sessionmaker(bind=engine)
session = Session

import random
import requests
from faker import Faker

fake = Faker()

for _ in range(10):
    first_name = fake.first_name()
    last_name = fake.last_name()
    username= f"{first_name}_{last_name}"
    
    
    
    users = User(first_name=first_name, last_name=last_name, username =username, email=fake.ascii_company_email())
    
    print(users)
    
    import ipdb; ipdb.set_trace()
    

