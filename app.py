from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello from AWS EC2!</h1><p>This app is running inside a Docker container.</p>"


@app.route("/about")
def about():
    return jsonify(project="EC2 Flask Docker", author="Karan Singh Rawat")


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
