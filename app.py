from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/open_barrier')
def open_barrier():
    try:
        response = requests.get('http://localhost:3000/open')
        if response.status_code == 200:
            return 'Barrier opened successfully!', 200
        else:
            return f'Failed to open the barrier. Status code: {response.status_code}', 500
    except Exception as e:
        print(f'An error occurred: {e}')  # Logging the exception
        return f'An error occurred: {e}', 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
