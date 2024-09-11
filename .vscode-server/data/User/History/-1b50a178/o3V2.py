from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "<h1> Buenas noches Hola Estudiantes </h1> "


if __name__ == "__main__": 
    host = "127.0.0.1"
    port = 4000
    app.run(host,port, debug=True)