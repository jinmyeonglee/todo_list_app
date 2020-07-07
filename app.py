from flask import Flask, render_template, request
from jinja2 import Template
import src.mysql

app = Flask(__name__)
db_server = src.mysql.DBServer()


@app.route('/')
def index():
    doing_todo_list = db_server.get_doing_todo_list()
    return render_template('index.html', todo_list=doing_todo_list)


if __name__ == '__main__':
    app.run()
