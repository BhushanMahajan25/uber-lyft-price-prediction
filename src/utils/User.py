import os
import pandas as pd
from flask_login import UserMixin
from shared_data import DATABASE_DIR

users_csv_path = os.path.join(DATABASE_DIR, 'users.csv')

class User(UserMixin):
    '''
    The user class of type Usermixin from flask_login handles the user information.
    param: Oauth unique ID, name, email
    methods: get(user_id): Checks if the user exists in the database
            create(user_id, name, email): Creates a new user in the database
    '''

    def __init__(self, id_, name, email):
        self.id = id_
        self.name = name
        self.email = email
    
    @staticmethod  
    def read_user_csv():
        try:
            user_information = pd.read_csv(users_csv_path)
            return user_information
        except pd.errors.EmptyDataError as empty_data_error:
            print('EmptyDataError: {}'.format(empty_data_error))
            user_information = pd.DataFrame(columns=['user_id', 'name', 'email'])
            user_information.to_csv(users_csv_path, index=None)
            return user_information
        
    @staticmethod
    def get(user_id):
        '''
        This module checks if the user exists in the database.
        param: user_id
        return : Object of the User class with required details
        '''
        
        user_information = User.read_user_csv()
        specific_user_details = user_information.loc[user_information['user_id'] == user_id]

        if specific_user_details.shape[0] != 0:
            return User(specific_user_details['user_id'].values[0],
                        specific_user_details['name'].values[0],
                        specific_user_details['email'].values[0])
        else:
            return None

    @staticmethod
    def create(id_, name, email):
        '''
        Creates a user if not already present in the database.
        param: google oauth user_id, name, email
        return: True if successfully added to the database
        return: False if any error while adding to the database
        '''
        try:
            user_information = User.read_user_csv()
            current_user = pd.DataFrame({'user_id': [id_], 'name': [name],
                                         'email': [email]})
            user_information = pd.concat([user_information, current_user])
            user_information.to_csv(users_csv_path, index=None)
            return True
        except BaseException as error:
            print('An exception occurred while creating User CSV: {}'.format(error))
            return False