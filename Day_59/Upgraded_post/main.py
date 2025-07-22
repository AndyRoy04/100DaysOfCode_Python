from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
all_posts = response.json()
name = 'Anderson'
git_hub = "https://github.com/AndyRoy04"
@app.route('/')
def home():
    return render_template('index.html', posts=all_posts, my_name=name, my_github=git_hub)
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/post/<int:blog_id>")
def post(blog_id):
    return render_template('post.html', current_post=all_posts[blog_id-1], my_name=name, my_github=git_hub)

if __name__ == "__main__":
    app.run(debug=True)
