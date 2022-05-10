from flask import Flask

app = Flask(__name__)

def dummy_response():
    return "<p>Hello, World!</p>"

@app.route("/")
def dummy_server():
    return dummy_response()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)