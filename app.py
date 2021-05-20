from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.errorhandler(404) # e is the error thrown
def pageNotFound(e):
    print(e)
    return render_template("pageNotFound.html")

@app.route('/projects', methods=["GET", "POST"])
def returnProjects():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(port=5500 , debug=True)