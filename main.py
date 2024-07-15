from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import subprocess
import json



app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/retrieve/data', methods=['POST'])
def retriever():
    data = request.json
    db_name = data.get('db_name')

    print(db_name)
    collection_name = data.get('collection')
    print(collection_name)


    params = json.dumps(data.get('params', {}))
    host = data.get('host', 'localhost')
    port = data.get('port', 27017)

    cmd = [
        'python', 'db.py', 
        '--db', db_name, 
        '--collection', collection_name, 
        '--host', host, 
        '--port', str(port), 
        '--params', params
    ]

    result = subprocess.run(cmd, shell=True,capture_output=True, text=True)

    return jsonify({
        'stdout': result.stdout,
        'stderr': result.stderr,
        'returncode': result.returncode
    })

if __name__=='__main__':
    app.run('0.0.0.0', debug=True, port=8080)