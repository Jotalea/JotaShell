from flask import Flask, jsonify, request, Response
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    page = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>JotaShell</title>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <style>
        body {
          background-color: black;
          color: white;
          font-family: monospace;
          margin: 0;
          padding: 0;
        }

        #output {
          color: white;
          font-family: monospace;
          padding: 10px;
          white-space: pre-wrap;
        }
        </style>
    </head>
    <body>
        <div id="output"></div>
        <input type="text" id="cmdInput" placeholder="Enter command">
        <button onclick="runCommand()">Run</button>

        <script>
            var output = document.getElementById('output');
            var source = new EventSource('/stream');

            source.onmessage = function(event) {
                output.innerHTML += event.data + '<br>';
                output.scrollTop = output.scrollHeight;
            };

            function runCommand() {
                var cmdInput = document.getElementById('cmdInput').value;
                $.post('/cmd', {cmd: cmdInput});
                document.getElementById('cmdInput').value = '';
            }
        </script>
    </body>
    </html>
    """
    return page

def execute_command(command):
    try:
        output_bytes = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        output = output_bytes.strip()
    except subprocess.CalledProcessError as e:
        output = f"bash: {command}: {e.output.strip()}"
    return output

@app.route('/stream')
def stream():
    def generate():
        while True:
            yield 'data: \n\n'
    return Response(generate(), content_type='text/event-stream')

@app.route('/cmd', methods=['POST'])
def cmd():
    command = request.form['cmd']
    output = execute_command(command)
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)