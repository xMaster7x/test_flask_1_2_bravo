from flask import Flask,request

app = Flask(__name__)

LISTA=["alfa","bravo","charlie","delta","echo"]

@app.route("/")
def inicio():
    return {"payload":"welcome to my project"}

if __name__ == "__Main__":
    app.run(debug=True)
