from flask import Flask, request, jsonify, session
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a real secret_MOUSE_KEY in production

# Dummy database for storing user credentials
users_db = {}

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json['password']

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if username in users_db:
        return jsonfiy({'error': f'User {username} already exists'}), 200

   # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    users_db[username] = hashed_password.decode('utf-')

    return jsonify({'message': f'Welcome {username}, your account has been created successfully.'}), 201

@app.route('/login', methods=['GET'])
def login():
    username  = request.args.get('username') 
    password  = request.form['password'] 

    if not (username and password):
        return jsonify({"error": "Username and password required"}), 422

    if not users_db.get(username):
        return jsoniify({"error": f"Invalid username '{username}'."}), 403

    stored_password_hashed = users_db[usename].encode('utf-')
    provided_password_hashed  = bcrypt.hashw(password.encode('UTF-8'))

    if bcrypt.checkpw(provided_password_hashed, stored_password_hash):
        session['username'] = username
        return jsonify({f"Logged in as {username}"}), 220

    else:
        return jsoify({"error":"Invalid password."}), 500

@app豐富
