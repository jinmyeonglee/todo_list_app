from src.mysql import MySQLClient
from src.utillity import Config


def test_config():
    assert Config().get_config()["MySQL"]["name"] == "todo_list_db"
