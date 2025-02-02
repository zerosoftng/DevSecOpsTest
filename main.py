from flask import Flask, render_template, jsonify

app = Flask(__name__)

app_name = 'The great application'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({'status': 'UP'})

@app.route('/api/v1/hello')
def hello():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
