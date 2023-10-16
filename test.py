from flask import Flask

app = Flask(__name__)

@app.route('/open')
def open_barrier():
    return "Barrier has been opened!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
