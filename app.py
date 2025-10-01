from flask import Flask
from controller import TodoController  # Импортируем контроллер
from models import db  # Импортируем базу данных

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Маршруты
@app.route('/')
def index():
    return TodoController.index()

@app.route('/add', methods=["POST"])
def add():
    return TodoController.add()

@app.route('/update/<int:todo_id>')
def update(todo_id):
    return TodoController.update(todo_id)

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    return TodoController.delete(todo_id)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Создаем таблицы в базе данных
    app.run(debug=True)