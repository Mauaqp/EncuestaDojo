from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)  
app.secret_key = "estoessecreto"

#Ruta index
@app.route('/')
def index():
    return render_template("index.html")

#Ruta process data
@app.route('/process', methods=['POST'])
def post():
    session["nombre"] = request.form["nombre"]
    session["loc-dojo"] = request.form["loc-dojo"]
    session["leng"] = request.form["leng"]
    session["comments"] = request.form["comments"]
    return render_template('result.html')

#app.run
if __name__=="__main__":
    app.run(debug=True)