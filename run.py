import os
from flask import Flask, render_template #We first import the class Flask capital F for class names 

app = Flask(__name__) #creates instance of class name Flask and storing in a variable called app


@app.route("/") #tells flask what url should trigger the function that follows using the .route decorator
def index():
    return render_template("index.html")


@app.route("/about") #tells flask what url should trigger the function that follows using the .route decorator
def about():
    return render_template("about.html")


@app.route("/contact") #tells flask what url should trigger the function that follows using the .route decorator
def contact():
    return render_template("contact.html")


@app.route("/careers") #tells flask what url should trigger the function that follows using the .route decorator
def careers():
    return render_template("careers.html")


if __name__ == "__main__": # __main__ is the name of the default module in python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )