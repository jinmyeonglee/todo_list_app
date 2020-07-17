from configparser import ConfigParser
from datetime import datetime
from logging.handlers import RotatingFileHandler
from logging import Formatter, DEBUG


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


def init_log(app):
    file_handler = RotatingFileHandler("./sample-app.log",
                                       maxBytes=100000,
                                       backupCount=1000)

    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s in %(filename)s:%(lineno)d]'))
    file_handler.setLevel(DEBUG)
    app.logger.addHandler(file_handler)
    app.logger.info("logging start")