from flask import *

app = Flask(__name__)

messages = []

@app.route("/")
def home():
    return render_template("board.html",messages=messages)

@app.route("/post",methods=["POST"])
def post():
    name = request.form.get("name")
    msg = request.form.get("message")
    messages.append({"name":name,"msg":msg})

    return redirect("/")
app.run(debug=True)