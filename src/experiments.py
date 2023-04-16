import pandas as pd
import os
from utils.User import User
from shared_data import DATABASE_DIR

from os import environ as env
from dotenv import load_dotenv, find_dotenv

# We're continuing from the steps above. Append this to your server.py file.
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
    
print(env.get('GOOGLE_CLIENT_ID'))


# users_csv_path = os.path.join(DATABASE_DIR, 'users.csv')
# unique_id = 123456789
# user_name = 'John Doe'
# user_email = 'john.doe@gmail.com'

# user = User.get(unique_id)
# if user is not None:
#     print(user)
#     print("user exists in database")
#     print("call login_user(user)")
# else:
#     print("create user in database")
#     user = User(unique_id, user_name, user_email)
#     user_created = user.create(unique_id, user_name, user_email)
#     if not user_created:
#         print("user creation in database failed")

# print("call login_user(user)")
# print("Google Login Successful")
# print("redirect(url_for('index'))")
