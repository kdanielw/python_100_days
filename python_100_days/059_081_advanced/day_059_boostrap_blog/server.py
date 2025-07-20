from flask import Flask, render_template
import requests

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

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:blog_id>')
def post(blog_id):
    for post in all_blog_post:
        if post["id"] == blog_id:
            selected_post = post
    return render_template("post.html", blog_post = selected_post)

if __name__ == "__main__":
    app.run(debug=True)
