import json
import io
import os

from Utils import Utils


class Config:

    config = None
    def __init__(self):
        config = self.loadConfig()
        self.config = config
        pass

    def loadConfig(self):
        configPath = os.path.abspath("./resources/config")
        expPath = configPath + '/Experiments.json'
        expJson = Utils.readAllFile(expPath)
        configObj = json.loads(expJson)
        return configObj
        pass
    pass