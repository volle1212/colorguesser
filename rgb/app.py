from flask import Flask, render_template, request
from random import randint
app = Flask(__name__)

@app.route('/')
def hello_world():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return render_template("index.html",r=r, g=g, b=b)


@app.route('/answer', methods=['GET', 'POST'])
def answer():
    r = request.form["r"]
    g = request.form["g"]
    b = request.form["b"]

    r_answer = request.form["r_answer"]
    g_answer = request.form["g_answer"]
    b_answer = request.form["b_answer"]
    
    points = (abs(int(r_answer)-int(r)) + abs(int(g_answer)-int(g)) + abs(int(b_answer)-int(b)))

    return render_template("answer.html", points=points, r=r, g=g, b=b)
    

if __name__ == '__main__':
    app.run(debug=True, port=8080)