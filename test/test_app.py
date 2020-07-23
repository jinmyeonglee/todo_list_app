from src.mysql import MySQLClient
# from src.utillity import Config

def test_mysql():
    db_server = MySQLClient()
    todo_list = db_server.get_all_todo_list()
    assert len(todo_list) != 0
