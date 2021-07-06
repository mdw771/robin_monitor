import pickle
import os

from robin_monitor.settings import Settings


class User(Settings):

    def __init__(self):
        super(User, self).__init__()
        self.robin_username = None
        self.robin_password = None
        self.email = None
        self.email_password = None

    def try_load_credentials(self):
        try:
            self.load_all_credentials()
        except:
            print('I was unable to load saved user credentials.')
            self.robin_username = input('Please enter your Robinhood username: ')
            self.robin_password = input('Please enter your Robinhood password: ')
            self.email = input('Please enter your email: ')
            self.email_password = input('Please enter your email password (for sending notification from your email account): ')
            if input('Do you want to save your credentials? (y/n): ') in ['y', 'Y']:
                self.save_all_credentials()

    def set_robin_credentials(self, username, password):
        self.robin_username = username
        self.robin_password = password

    def set_email_credentials(self, email, password):
        self.email = email
        self.email_password = password

    def save_all_credentials(self):
        if not os.path.exists(self.credential_path):
            os.makedirs(self.credential_path)
        f = open(os.path.join(self.credential_path, 'robin_creds'), 'wb')
        pickle.dump([self.robin_username, self.robin_password], f)
        f.close()
        f = open(os.path.join(self.credential_path, 'email_creds'), 'wb')
        pickle.dump([self.email, self.email_password], f)
        f.close()

    def load_all_credentials(self):
        f = open(os.path.join(self.credential_path, 'robin_creds'), 'rb')
        self.robin_username, self.robin_password = pickle.load(f)
        f.close()
        f = open(os.path.join(self.credential_path, 'email_creds'), 'rb')
        self.email, self.email_password = pickle.load(f)
        f.close()