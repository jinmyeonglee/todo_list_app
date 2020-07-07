import pymysql
from src.todo import Todo
from src.utillity import read_sql_file


class MysqlInfo:
    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "Jinmyeong"
        self.password = ""
        self.db = "db_todo_list"


class DBServer:
    def __init__(self):
        self.info = MysqlInfo()
        self.conn = pymysql.connect(host=self.info.host, user=self.info.user,
                                    password=self.info.password,
                                    db=self.info.db, charset='utf8')

    def get_all_todo_list(self):
        cursor = self.conn.cursor()
        sql_query = read_sql_file("./queries/get_todo_list.sql")
        cursor.execute(sql_query)
        result = cursor.fetchall()

        todo_list = []
        for row in result:
            todo_list.append(Todo(row[0], row[1], row[2]))

        return todo_list

    def get_doing_todo_list(self):
        all_todo_list = self.get_all_todo_list()
        doing_todo_list = [todo for todo in all_todo_list if todo.status == 0]
        return doing_todo_list

    def get_done_todo_list(self):
        all_todo_list = self.get_all_todo_list()
        done_todo_list = [todo for todo in all_todo_list if todo.status == 1]
        return done_todo_list

    def create_todo_db(self):
        cursor = self.conn.cursor()
        sql_query = read_sql_file("./queries/create_todo_db.sql")
        cursor.execute(sql_query)

    def delete_todo_db(self):
        cursor = self.conn.cursor()
        sql_query = read_sql_file("./queries/delete_todo_db.sql")
        cursor.execute(sql_query)

    def add_todo(self):
        pass

    def remove_todo(self, todo):
        pass

