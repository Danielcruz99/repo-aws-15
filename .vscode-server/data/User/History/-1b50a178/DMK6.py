from flask import Flask

app = Flask(__name__)

@app.route('/home')

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4000
    app.run(host,port)