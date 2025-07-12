from flask import Flask

def make_bold(function):    
    def wraped():
        tag = "b"
        html_tag = f"<{tag}>"
        html_tag += function()
        html_tag += f"</{tag}>"
        return html_tag
    return wraped

def make_emphasis(function):    
    def wraped():
        tag = "em"
        html_tag = f"<{tag}>"
        html_tag += function()
        html_tag += f"</{tag}>"
        return html_tag
    return wraped

def make_underline(function):    
    def wraped():
        tag = "u"
        html_tag = f"<{tag}>"
        html_tag += function()
        html_tag += f"</{tag}>"
        return html_tag
    return wraped

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
            "<p>This is a paragraph</p>"

@app.route("/bye")
@make_bold
@make_emphasis
def say_bye():
    return "<p>Bye!</p?"

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"<p>Hello, {name}. You are {number} years old</p?"

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)