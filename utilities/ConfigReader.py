from configparser import ConfigParser

# config = ConfigParser()
# config.read('config.ini')
# config.get("basic info", "browserName")
# config.get("basic info", "URL")
# config.get("mobile", "executionOS")

class ConfigFileReader:
    def readConfig(self, section, key):
        config = ConfigParser()
        config.read("testData/config.ini")
        return config.get(section, key)