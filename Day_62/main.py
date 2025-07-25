from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

coffe_rating = ['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕']
wifi_strength = ['✘', '💪🏾', '💪🏾💪🏾', '💪🏾💪🏾💪🏾', '💪🏾💪🏾💪🏾💪🏾', '💪🏾💪🏾💪🏾💪🏾💪🏾']
power_strength = ['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']

csv_file_location = '100DaysOfCode_Python/Day_62/cafe-data.csv'

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g. 6PM', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', choices=coffe_rating, validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices=wifi_strength, validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices=power_strength, validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # making the data received in string format inorder to ease insertion
        received = f"{form.cafe.data},{form.location.data},{form.open_time.data},{form.close_time.data},{form.coffee.data},{form.wifi.data},{form.power.data}"
        # print(received)
        with open(csv_file_location, 'a', encoding='utf-8') as new_file:
            new_file.write(f"\n{received}")
            # print("Data added successfully")
        return redirect(url_for('cafes'))  # rendering the cafes page after the user added all the required informations in the respective fields
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(csv_file_location, newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        # print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
