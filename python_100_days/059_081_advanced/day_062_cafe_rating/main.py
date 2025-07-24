from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL, Length
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe Name', validators=[DataRequired()])
    location = URLField(label='Localization', validators=[DataRequired(), URL()])
    open = StringField(label='Open Time (07:30)', validators=[DataRequired(), Length(min=5,max=5)])
    close = StringField(label='Closing Time (17:30)', validators=[DataRequired(), Length(min=5,max=5)])
    coffee = SelectField(label='Coffee',choices=["☕️","☕️☕️","☕️☕️☕️","☕️☕️☕️☕️","☕️☕️☕️☕️☕️"], validators=[DataRequired()])
    wifi = SelectField(label='Wifi',choices=["✘","💪","💪💪","💪💪💪","💪💪💪💪","💪💪💪💪💪"], validators=[DataRequired()])
    power = SelectField(label='Power',choices=["✘","🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField(label='Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        new_cafe = [form.cafe.data, form.location.data, form.open.data, form.close.data, form.coffee.data, form.wifi.data, form.power.data]
        new_cafe_str = ",".join(new_cafe)
        print(new_cafe_str)
        with open('cafe-data.csv', newline='', encoding='utf-8', mode="a") as csv_file:
            wr = csv.writer(csv_file)
            wr.writerow(new_cafe)
            print("updated")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
