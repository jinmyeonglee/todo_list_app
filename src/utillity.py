from configparser import ConfigParser
from datetime import datetime
from logging import FileHandler
from logging import Formatter, DEBUG, StreamHandler, getLogger
from sys import stdout


def timestamp():
    return "[" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "] "


def read_config_file(filename="dev.ini"):
    parser = ConfigParser()
    parser.read(filename)
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

    # handler = StreamHandler(stdout)
    # handler.setFormatter(formatter)
    # handler.setLevel(DEBUG)

    # logger.addHandler(handler)

    logger.info("logging start")

    return logger
