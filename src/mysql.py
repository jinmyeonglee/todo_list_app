import pymysql
from src.todo import Todo
from src.utillity import read_sql_file, read_config_file


class MysqlInfo:
    def __init__(self, parser):
        self.host = parser.get('db', 'db_host')
        self.user = parser.get('db', 'db_user')
        self.password = parser.get('db', 'db_pwd')
        self.db = parser.get('db', 'db_name')
        self.port = parser.get('db', 'db_port')


class DBServer:
    def __init__(self):
        parser = read_config_file()
        self.info = MysqlInfo(parser)

    def get_connection(self):
        return pymysql.connect(host=self.info.host, port=int(self.info.port),
                               user=self.info.user, password=self.info.password,
                               db=self.info.db, charset='utf8', autocommit=True)

    def excute_queries(self, query_list, cursor):
        for q in query_list:
            cursor.execute(q)

    def get_all_todo_list(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql_query = read_sql_file("./queries/get_todo_list.sql")

        self.excute_queries(sql_query, cursor)

        result = cursor.fetchall()

        todo_list = []
        for row in result:
            print(row[0], row[1], row[2])
            todo_list.append(Todo(row[0], row[1], row[2]))

        conn.close()

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
        conn = self.get_connection()
        cursor = conn.cursor()
        sql_query = read_sql_file("./queries/create_todo_db.sql")

        self.excute_queries(sql_query, cursor)

        conn.close()

    def delete_todo_db(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql_query = read_sql_file("./queries/delete_todo_db.sql")

        self.excute_queries(sql_query, cursor)

        conn.close()

    def add_todo(self, todo):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql_query = read_sql_file("./queries/add_todo.sql")
        sql_query[-1] = sql_query[-1] % (todo.content, todo.status)

        self.excute_queries(sql_query, cursor)

        conn.close()

    def remove_todo(self, todo):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql_query = read_sql_file("./queries/remove_todo.sql")
        sql_query[-1] = sql_query[-1] % todo.idx

        self.excute_queries(sql_query, cursor)

        conn.close()

    def mark_todo_done(self, todo):
        if todo.status == 1:
            raise Exception(str(todo.idx) + ": already done!")
        conn = self.get_connection()
        cursor = conn.cursor()

        sql_query = read_sql_file("./queries/mark_todo_done.sql")
        sql_query[-1] = sql_query[-1] % todo.idx

        self.excute_queries(sql_query, cursor)

        conn.close()
