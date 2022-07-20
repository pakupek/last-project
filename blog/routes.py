from flask import render_template, Flask

app = Flask(__name__)

#Route leading into homepage
@app.route('/')
def homepage():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)