from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)  
    complete = db.Column(db.Boolean, default=False) 

@app.route('/')
def index():
    # Показать все задачи
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html', todos=todo_list) 
@app.route("/add",methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))
    

if __name__ == "__main__":
    with app.app_context(): 
        db.create_all()       
    app.run(debug=True)