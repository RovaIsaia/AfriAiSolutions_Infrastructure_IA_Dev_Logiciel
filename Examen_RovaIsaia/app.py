from flask import Flask, jsonify, request
import sqlite3
import os

app = Flask(__name__)
DB_FILE = "tasks.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT
    )''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    # C’est cette ligne qu’il faudra modifier a la fin de l’exercice Git
    return "<h1>TaskMaster PRO v2.0</h1><p>L’application tourne dans Docker !</p>"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = [{"id": row[0], "title": row[1]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(tasks)

if __name__ == '__main__':
    init_db()
    print("Serveur lance sur le port 5000...")
    app.run(host='0.0.0.0', port=5000)