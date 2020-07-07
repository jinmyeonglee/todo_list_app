create database todo_list_db;

use todo_list_db;

create table todo_list(
    'idx' int auto_increment primary key,
    'content' varchar(400),
    'status' int,
);