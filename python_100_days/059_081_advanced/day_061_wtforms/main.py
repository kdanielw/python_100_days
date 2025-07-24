from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5

class LoginForm(FlaskForm):
    email = EmailField(label="E-mail", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Login")

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = "testkey"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    valid_email = "admin@email.com"
    valid_password = "12345678"

    login_form = LoginForm()
    print(login_form.validate_on_submit())
    print(login_form.errors)
    print(login_form.email.data)
    print(login_form.password.data)

    if login_form.validate_on_submit():
        email_data = login_form.email.data
        password_data = login_form.password.data
        if email_data == valid_email and password_data == valid_password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
