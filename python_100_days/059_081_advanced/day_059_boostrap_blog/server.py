from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
import os

def send_email_alert(form_sata):
    load_dotenv()
    MY_EMAIL = (os.getenv('MY_EMAIL'))
    GOOGLE_SMTP_PASSWORD = (os.getenv('GOOGLE_SMTP_PASSWORD'))
    message = f"Name: {form_sata["name"]}\nE-mail: {form_sata["email"]}\nPhone Number: {form_sata["phone"]}\nMessage: {form_sata["message"]}\n"
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=GOOGLE_SMTP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:New Message from yout Blog!\n\n{message}"
        )

blog_response = requests.get("https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json")
blog_data = blog_response.json()
all_blog_post = [post_data for post_data in blog_data]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts = all_blog_post)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", contact_status = "Contact Me")
    elif request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        print(f"{name}\n{email}\n{phone}\n{message}")
        send_email_alert(data)
        return render_template("contact.html", contact_status = "Successfully sent message")

@app.route('/post/<int:blog_id>')
def post(blog_id):
    for post in all_blog_post:
        if post["id"] == blog_id:
            selected_post = post
    return render_template("post.html", blog_post = selected_post)

if __name__ == "__main__":
    app.run(debug=True)
