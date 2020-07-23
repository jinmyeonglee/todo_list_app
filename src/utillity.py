from configparser import ConfigParser
from datetime import datetime
from logging import FileHandler
from logging import Formatter, DEBUG, getLogger
import argparse


def timestamp():
    return "[" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "] "


def get_option():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--ENV', action="store_true")
    args = arg_parser.parse_args()
    return vars(args)


class Config:
    parser = None

    def __init__(self, options=None):
        if self.parser is None:
            if options is None:
                options = {'ENV': False}
            Config.parser = self.set_config(options)

    def get_config(self):
        if Config.parser is None:
            raise ValueError("Should initialize first!")
        return Config.parser

    def set_config(self, options):
        if 'ENV' in options and options['ENV']:
            return self.config_from_env()
        else:
            return self.config_from_file()

    def config_from_file(self, filename="dev.ini"):
        parser = ConfigParser()
        parser.read(filename)
        return parser

    def config_from_env(self):
        from os import getenv
        parser = {}
        parser["MySQL"]["host"] = getenv("VERDA_MYSQL_HOST")
        parser["MySQL"]["port"] = getenv("VERDA_MYSQL_PORT")
        parser["MySQL"]["name"] = getenv("VERDA_DB_NAME")
        parser["MySQL"]["user"] = getenv("VERDA_MYSQL_USER")
        parser["MySQL"]["pwd"] = getenv("VERDA_MYSQL_PWD")

        parser["VOS"]["access_key"] = getenv("VERDA_VOS_ACCESS_KEY")
        parser["VOS"]["secret_key"] = getenv("VERDA_VOS_SECRET_KEY")
        parser["VOS"]["s3_host"] = getenv("VERDA_VOS_HOST")
        parser["VOS"]["bucket_name"] = getenv("VERDA_VOS_BUCKET")

        parser["Redis"]["host"] = getenv("VERDA_REDIS_HOST")
        parser["Redis"]["port"] = getenv("VERDA_REDIS_PORT")
        parser["Redis"]["pwd"] = getenv("VERDA_REDIS_PWD")

        parser["VES"]["user_id"] = getenv("VERDA_VES_USER_ID")
        parser["VES"]["pwd"] = getenv("VERDA_VES_PWD")

        return parser


def read_sql_file(filename):
    with open(filename) as sql_file:
        lines = sql_file.read().split(';')
        lines.pop()
        lines = [line.strip() for line in lines]
        return lines


def init_log():
    logger = getLogger('werkzeug')
    formatter = Formatter(
        '%(asctime)s %(levelname)s: %(message)s in %(filename)s:%(lineno)d]')

    file_handler = FileHandler("./sample-app.log")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(DEBUG)

    logger.addHandler(file_handler)

    logger.info("logging start")

    return logger
