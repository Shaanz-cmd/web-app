from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = [
{    "id":1,
    "title":"Setup Apache Server",
    "status":"Completed"
    },
{    "id":2,
    "title":"Build Flask API",
    "status":"in-progress"
    },
]

@app.route('/api/tasks',methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/api/status',methods=['GET'])
def get_status():
    return jsonify({"Server": "online", "memory_mode": "Low-RAM optimized"})

if __name__ == '__main__':
    app.run( host = '0.0.0.0', port = 5000, debug = True )
