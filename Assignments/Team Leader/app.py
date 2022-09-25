from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome Vijay!!</h1>"

@app.route("/course")
def course():
    return "Flask is Coming"

if __name__=="__main__":
    app.run(debug=True)