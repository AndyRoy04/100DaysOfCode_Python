from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def login():
    user_name = request.form['name']
    user_password = request.form['password']
    return f"<h1>Name : {user_name}</h1>"\
            f"<h1>Password : {user_password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)