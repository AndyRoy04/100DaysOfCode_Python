from flask import Flask, render_template
import requests

app = Flask(__name__)
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:blog_id>')
def show_post(blog_id):
    return render_template("post.html",current_post=all_posts[blog_id-1])

if __name__ == "__main__":
    app.run(debug=True)
