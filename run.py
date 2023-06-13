from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

todos = [
    {'id': 1, 'title': 'Task 1'},
    {'id': 2, 'title': 'Task 2'},
    {'id': 3, 'title': 'Task 3'}
]
next_id = 4

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def add_todo():
    global next_id
    title = request.json.get('title')
    todo = {'id': next_id, 'title': title}
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return '', 204

if __name__ == '__main__':
    app.run()
