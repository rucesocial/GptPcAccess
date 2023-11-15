from flask import Flask, request, jsonify
import subprocess
import requests

app = Flask(__name__)

# Security Warning: This variable controls whether the received code is executed.
# Setting this to True can be dangerous if the incoming code is not trusted.
ALLOW_EXECUTION = False

@app.route('/', methods=['GET', 'POST'])
def generate_code():
    if request.method == 'GET':
        runtime = request.args.get('runtime')
        code = request.args.get('code')
    elif request.method == 'POST':
        data = request.get_json()
        runtime = data.get('runtime')
        code = data.get('code')
        print(code)

    file_name = 'generated_code.py'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(code)

    if runtime == 'python':
        if ALLOW_EXECUTION:
            try:
                output = subprocess.check_output(
                    ['python', '-X', 'utf8', file_name],
                    stderr=subprocess.STDOUT) 
                return jsonify({'status': 'success', 'message': 'Python code generated and executed successfully', 'output': output.decode('utf-8')})
            except subprocess.CalledProcessError as e:
                return jsonify({'status': 'error', 'message': 'Error while executing the Python code', 'error': e.output.decode('utf-8')})
        else:
            return jsonify({'status': 'success', 'message': 'Python code generated but not executed due to security settings (ALLOW_EXECUTION = False)'})

    elif runtime == 'unity':
        # Redirect the request to Unity on localhost:5001
        response = requests.get('http://localhost:5001/', params=request.args)
        print("Content: " + response.text + "content finish")
        return response.text

    return jsonify({'status': 'error', 'message': 'Invalid parameters'})

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
