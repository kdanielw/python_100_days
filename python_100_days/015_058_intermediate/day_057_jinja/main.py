from flask import Flask, render_template
import requests
from post import Post

blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_data = blog_response.json()
all_blog_post = [Post(post_data) for post_data in blog_data]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts = all_blog_post)

@app.route('/post/<int:blog_id>')
def post(blog_id):
    for post in all_blog_post:
        if post.id == blog_id:
            selected_post = post
    return render_template("post.html", blog_post = selected_post)

if __name__ == "__main__":
    app.run(debug=True)
