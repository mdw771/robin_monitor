import os


class Settings():

    def __init__(self):
        self.credential_path = os.path.join(os.path.expanduser("~"), '.robin_monitor', 'credentials')
