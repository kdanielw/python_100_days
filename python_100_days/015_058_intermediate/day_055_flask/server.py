from flask import Flask
import random

NUMBERS_URL = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
generated_number = random.randint(0, 9)
print(generated_number)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Guess The number between 0 and 9</h1>" \
    f"<img src='{NUMBERS_URL}'>"

@app.route("/<int:number>")
def guess_the_number(number):
    if number == generated_number:
        return f"<h1 style='color: green'>You found me! I am #{number}</h1>"
    elif number > generated_number:
        return f"<h1 style='color: red'>#{number} is too high! Try again.</h1>"
    elif number < generated_number:
        return f"<h1 style='color: purple'>#{number} is too low! Try again.</h1>"

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)