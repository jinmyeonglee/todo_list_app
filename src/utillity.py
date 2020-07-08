from configparser import ConfigParser


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
