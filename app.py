from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    with app.app_context():
        return render_template('home.html')
hello_world()


if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)