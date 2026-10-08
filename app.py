from flask import Flask, jsonify, request

app = Flask(__name__)

# Список пользователей
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# 1. Получение списка пользователей (GET /api/users)
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# 2. Создание пользователя (POST /api/users)
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Bad request"}), 400
    
    new_user = {
        "id": len(users) + 1,
        "name": data['name']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# 3. Удаление пользователя (DELETE /api/users/<id>)
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return jsonify({"message": f"User {user_id} deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
