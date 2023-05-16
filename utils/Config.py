import json
import time


class Config():
    def __init__(self):
        with open('./config.json') as config_file:
            config = json.load(config_file)
            self.config = config

    def get(self, path: str):
        return self.config[path]

