import os
import re


class Settings():

    def __init__(self):
        self.credential_path = os.path.join(os.path.expanduser("~"), '.robin_monitor', 'credentials')
        self.datetime_pattern = re.compile(r'(\d+)-(\d+)-(\d+)T(\d+):(\d+):(\d+)Z')
