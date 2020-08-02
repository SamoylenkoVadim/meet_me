import json
import os
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)
app_loger = logging.getLogger(__name__)

configs_path = os.environ["CONFIGS_PATH"]

class AppConfig():

    def __init__(self):
        self._data = self.load()
        app_loger.info("Configs loaded")
    
    def load(self):
        data = {}
        with open(configs_path) as app_config:
            data = json.load(app_config)
        return data
    
    def get_config(self, item):
        return self._data.get(item)
    
config = AppConfig()

class Content():

    def __init__(self):
        self._data = self.load()
        app_loger.info("Content loaded")
    
    def load(self):
        data = {}
        with open(config.get_config('content_path')) as content_path:
            data = json.load(content_path)
        return data
    
    def get_text(self, handler, item):
        return self._data.get(handler + '_handler', {}).get(item, 'Text not found')
    
content = Content()

