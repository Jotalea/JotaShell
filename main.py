import os; from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    with open('index.html', 'r') as f:
        return f.read()

@app.route('/cmd', methods=['POST'])
def execute_command():
    command = request.form['cmd']
    import subprocess
    try:
        output_bytes = subprocess.check_output(command, shell=True)
        output = output_bytes.decode('utf-8')
    except subprocess.CalledProcessError:
        output = f"bash: {command.split(' ')[0]}: command not found"
    outhtml = f"{os.getcwd()}$ {command}<br>{output}"
    return jsonify({"output": outhtml, "endreason": "success"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)