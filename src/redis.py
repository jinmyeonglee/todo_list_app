import redis
from src.utillity import read_config_file
from src.todo import Todo


class RedisInfo:
    def __init__(self, parser):
        self.host = parser.get('Redis', 'host')
        self.port = parser.get('Redis', 'port')
        self.pwd = parser.get('Redis', 'pwd')


class RedisClient:
    def __init__(self):
        parser = read_config_file()
        self.info = RedisInfo(parser)
        self.client = redis.StrictRedis(host=self.info.host, port=self.info.port, password=self.info.pwd)

    def add_todo(self, todo):
        self.client.set(todo.idx, todo.content + str(todo.status))

    def delete_todo(self, todo):
        self.client.delete(todo.idx)

    def toggle_status(self, todo):
        value = self.client.get(todo.idx).decode('utf-8')
        toggled_todo = Todo(todo.idx, value[:-1], 0 if int(value[-1]) == 1 else 1)
        self.add_todo(toggled_todo)

    def add_todo_list(self, todo_list):
        # for todo in todo_list:
        #     self.add_todo(todo)
        self.client.mset({x.idx: x.content + str(x.status) for x in todo_list})

    def get_todo_list(self):
        todo_list = []
        keys = self.client.scan_iter("*")

        for key in keys:
            value = self.client.get(key).decode('utf-8')
            todo_list.append(Todo(key, value[:-1], int(value[-1])))
        return todo_list
