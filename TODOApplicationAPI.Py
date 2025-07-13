from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory TODO list
todos = []
next_id = 1

# Get all TODO items
@app.route('/todos', methods=['GET'])
def get_all_todos():
    return jsonify(todos), 200

# Get a single TODO item by ID
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if todo:
        return jsonify(todo), 200
    return jsonify({'error': 'Todo not found'}), 404

# Create a new TODO item
@app.route('/todos', methods=['POST'])
def create_todo():
    global next_id
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    todo = {
        'id': next_id,
        'title': data['title'],
        'completed': False
    }
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201

# Update a TODO item
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404

    todo['title'] = data.get('title', todo['title'])
    todo['completed'] = data.get('completed', todo['completed'])
    return jsonify(todo), 200

# Delete a TODO item
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [item for item in todos if item['id'] != todo_id]
    return jsonify({'message': f'Todo {todo_id} deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)