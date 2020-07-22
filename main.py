import config_telegram
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

config_telegram.setup()