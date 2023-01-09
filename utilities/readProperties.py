import configparser

Config = configparser.RawConfigParser()
Config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationurl():
        baseurl = Config.get("COMMON INFO", "baseurl")
        return baseurl

    @staticmethod
    def getusername():
        username = Config.get("COMMON INFO", "username")
        return username

    @staticmethod
    def getpassword():
        password = Config.get("COMMON INFO", "password")
        return password












