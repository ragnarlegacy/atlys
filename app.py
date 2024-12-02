from flask import Flask, request, jsonify, render_template

S3_BUCKET_URL = "https://atlys-bucket-077.storage.googleapis.com/"

class User:
    def __init__(self):
        self.users = {}

    def add_user(self):
        """
        API endpoint to add a user.
        Expects a JSON payload with 'id', 'name', and 'email'.
        """
        data = request.json
        if not all(key in data for key in ('id', 'name', 'email')):
            return jsonify({"error": "Missing required fields (id, name, email)."}), 400
        
        user_id = data['id']
        if user_id in self.users:
            return jsonify({"error": "User with this ID already exists."}), 400
        
        self.users[user_id] = {
            "name": data['name'],
            "email": data['email']
        }
        return jsonify({"message": "User added successfully."}), 201

    def get_user(self, user_id):
        """
        API endpoint to retrieve a user by ID.
        """
        user = self.users.get(user_id)
        if not user:
            return jsonify({"error": "User not found."}), 404
        
        return jsonify({"id": user_id, "name": user['name'], "email": user['email']}), 200

# Instantiate Flask app and User class
app = Flask(__name__)
user_manager = User()

# Define routes using methods of the User class
@app.route('/add_user', methods=['POST'])
def add_user():
    return user_manager.add_user()

@app.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return user_manager.get_user(user_id)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
