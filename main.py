from flask import Flask, render_template, jsonify
from os import environ

app = Flask(__name__)

app_name = 'The great application'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({'status': 'UP'})

def calculate():
    print('Calculating...')
    return 1 + 1

def calculate2():
    print('Calculating...')
    return 1 + 1

if __name__ == '__main__':
    app.run(debug=True, port=8000)
