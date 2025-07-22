from flask import Flask, render_template, request
import requests
import smtplib


TEST_EMAIL = 'codingjourney25@gmail.com'
RECEIPIENT_EMAIL = 'codingjourney25@gmail.com'
PASSWORD = 'xneamnxivfjkunsk'

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

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        # Sending the feedback to the Receipiant
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(TEST_EMAIL, PASSWORD)
            connection.sendmail(TEST_EMAIL,
                                RECEIPIENT_EMAIL,
                                msg=f'Subject: Message from {name}\n\nName: {name}\nEmail: {email}\nPhone: {phone}\n Message: {message}')
            connection.quit()

        return render_template('contact.html', response_message='Message Successfully sent', msg_sent=True)
    return render_template('contact.html')


@app.route("/post/<int:blog_id>")
def post(blog_id):
    return render_template('post.html', current_post=all_posts[blog_id-1], my_name=name, my_github=git_hub)

if __name__ == "__main__":
    app.run(debug=True)
