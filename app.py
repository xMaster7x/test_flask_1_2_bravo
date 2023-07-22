from flask import Flask,request

app = Flask(__name__)

LISTA=["bar","qux","echo","alfa","foo"]

@app.route("/")
def inicio():
    return {"payload":"welcome to my project"}

@app.route("/read")
def read():
    contend = request.args.get('contend')
    index = LISTA.index(contend) if contend in LISTA else False
    user = LISTA[index] if index else 'Usuario no encontrado'
    return {
        "payload": user,
    }

@app2.route("/create", methods=["POST"])
def create():
    userlist = request.args.get("usuario")
    if userlist in LISTA:
        return userlist
    else:
        return "no esta"

if __name__ == "__Main__":
    app.run(debug=True)
