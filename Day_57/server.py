from flask import Flask, render_template, url_for
import random
import time
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 99)
    year = time.strftime("%Y")
    return render_template("index.html", num=random_number, year=year)

@app.route("/guess/<name>")
def guess(name):
    my_name = name.capitalize()
    age_response = requests.get(f"https://api.agify.io/?name={my_name}")
    age_response = age_response.json()
    gender_response = requests.get(f"https://api.genderize.io/?name={my_name}")
    gender_response = gender_response.json()
    
    my_age = age_response['age']
    my_gender = gender_response['gender']
    
    if my_gender == None or my_age == None:
        return f"<h1>Hey {my_name}</h1>"\
            "<h3>I couldn't find any information about you.</h3>"
    
    return render_template("app.html", name=my_name, age=my_age, gender=my_gender)

@app.route("/blog/<num>")
def blog(num):
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)

