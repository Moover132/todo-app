from flask import render_template, request, redirect, url_for
from models import db, Todo  # Импортируем модель из models.py

class TodoController:
    @staticmethod
    def index():
        todo_list = Todo.query.all()
        return render_template('base.html', todos=todo_list)

    @staticmethod
    def add():
        title = request.form.get("title")
        new_todo = Todo(title=title, complete=False)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("index"))

    @staticmethod
    def update(todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.complete = not todo.complete
        db.session.commit()
        return redirect(url_for("index"))

    @staticmethod
    def delete(todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for("index"))