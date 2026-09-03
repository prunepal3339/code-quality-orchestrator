from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Create a connection to your SQLite database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create a new table if it doesn't exist
def init_db():
    conn=get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL)')
    conn.commit()
    conn.close()

@app.route('/users', methods=['POST'])
def add_user():
    # Get the data from the request
    data = request.get_json()

    # Validate the input
    if not 'name' in data or not 'email' in data:
        return jsonify({'error': 'Missing name or email'}), 400

    # Store the data in the database
    conn = get_db_connection()
    
    try:
        conn.execute('INSERT INTO users (name, email) VALUES (?, ?)', (data['name'], data['email']))
        conn.commit()
        conn.close()
        return jsonify(data), 201
    except sqlite3.IntegrityError:
        conn.rollback()
        conn.commit() 
        conn.close()  
        return jsonify({"error": "Email already exists"}), 422

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
