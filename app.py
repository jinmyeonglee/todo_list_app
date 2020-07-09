from flask import Flask, render_template, request, redirect, url_for
from jinja2 import Template
import src.mysql
import src.todo

app = Flask(__name__)
db_server = src.mysql.DBServer()


@app.route('/')
def index():
    doing_todo_list = db_server.get_doing_todo_list()
    return render_template('index.html', todo_list=doing_todo_list)


@app.route('/delete/<idx>', methods=['POST'])
def delete_todo(idx):
    db_server.remove_todo(src.todo.Todo(int(idx), None, None))
    return redirect(url_for('index'))


@app.route('/done/<idx>', methods=['POST'])
def mark_todo_done(idx):
    db_server.mark_todo_done(src.todo.Todo(int(idx), None, None))
    return redirect(url_for('index'))


@app.route('/done_list')
def show_done_todo():
    done_todo_list = db_server.get_done_todo_list()
    return render_template('done_list.html', todo_list=done_todo_list)


@app.route('/')
def show_todo_list():
    return redirect(url_for('index'))


@app.route('/done_list/<idx>', methods=['POST'])
def unmark_todo(idx):
    db_server.unmark_todo_done(src.todo.Todo(int(idx), None, None))
    done_todo_list = db_server.get_done_todo_list()
    return render_template('done_list.html', todo_list=done_todo_list)


if __name__ == '__main__':
    app.run('0.0.0.0')
