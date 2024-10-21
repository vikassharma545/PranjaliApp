from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    return make_response(render_template('error404.html'), 404)


if __name__ == "__main__":
    app.run(debug=True)