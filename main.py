from flask import Flask, render_template, jsonify

app = Flask(__name__)

DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_PORT = '3306'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({'status': 'UP'})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
