from flask import Flask
import random

app = Flask(__name__)

colors = ['red', "orange", "grey", "blue", 'indigo', 'violet']
gifs = [
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbm5uZTdpNTkwdTFtdDY0YnRtY3BnZno0enZvanczMG1ybmYxMDN0bSZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/jnQYWZ0T4mkhCmkzcn/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTgyYTE0OTNiNnY3dzI5emI2YmRtbTV6dHdnN3Jpdm5va2ZkdGd4eWhiZXZtaW1keCZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/xT4uQ8In2MldI3JL56/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTgyYTE0OTNiOWw4N2d1ZjhnMnplYzJuY3RzYTJ0dnNwOWxjdHZjNzhxbHA4cWxtdSZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/FoH28ucxZFJZu/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTgyYTE0OTNiZjcwbnJsaXlheDgyZjd0c214dWNuODR1OGY1MGl6ZmtuMjV5NDdmaSZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/GBg58w14FovtuzHykg/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTgyYTE0OTNiZzRpeWMyZG4yMDViaXV1cHVodm9wM3hzdTVvczUxejQxcXJ2bG9zdyZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/QhjR3MG9ZFfjB6BtIZ/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTgyYTE0OTNiZGc3bmp0dXR5d3RkaXZnMHJieWQ3bnI3NHNsdmx6cTlzM2R6cnRweiZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/26BRuo6sLetdllPAQ/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTgyYTE0OTNiZGc3bmp0dXR5d3RkaXZnMHJieWQ3bnI3NHNsdmx6cTlzM2R6cnRweiZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/kouVntpG4ypyAK9fBz/giphy.gif"
]


@app.route("/")
def home():
    return f"""
    <h1>Guess a number between 0 and 9</h1>
    <img src='https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3eHY1dnYzZmFkM2tyczkycnE5MWVxa2d2OHdtNWpvbDRndHZ4YmFxcCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/8YZEMvETFSmzg4pbA0/giphy.gif' width='500' height='500'>
    """

@app.route("/<int:number>")
def user_guess(number):
    color = random.choice(colors) 
    if number == correct_number:
        return f"""
        <h1 style = 'color:green'>You guessed it!</h1>
        <img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbm5uZTdpNTkwdTFtdDY0YnRtY3BnZno0enZvanczMG1ybmYxMDN0bSZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/3NtY188QaxDdC/giphy.gif' width='500' height='500'>
        """
    elif number > correct_number:
        return f"""
        <h1 style = 'color:{color}'>Too High, Try again!</h1>
        <img src='{random.choice(gifs)}' width='500' height='500'>
        """
    else:
        return f"""
        <h1 style = 'color:{color}'>Too Low, Try again!</h1>
        <img src='{random.choice(gifs)}' width='500' height='500'>
        """

if __name__ == "__main__":
    correct_number = random.randint(1, 10)
    print(correct_number)
    app.run(debug=True)
    