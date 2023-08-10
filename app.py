from flask import Flask,request

app = Flask(__name__)

LISTA=["bar","qux","echo","alfa","foo"]

@app.route("/")
def inicio():
    return {"payload":"welcome to my project"}

@app.route("/read")
def read():
    contend = request.args.get('content')
    index = LISTA.index(content) if contend in LISTA else False
    user = LISTA[index] if index else 'Usuario no encontrado'
    return {
        "payload": user
    }

@app2.route("/create", methods=["POST"])
def create():
    userlist = request.args.get("usuario")
    if userlist in LISTA:
        return {
            "payload": userlist
        }
    else:
        return "no esta"

@app2.route("/delete", methods=["DELETE"])
def delete():
    userlist = request.args.get("content")
    if userlist in LISTA:
        return {
            "payload": userlist
        }
    else:
        return "no se encontró el usuario"

@app.route("/put", methods=["PUT"])
def put():
    leer=request.args.get("content")
    if leer=="echo":
        return {"payload":leer}
    else:
        return "Usuario No Existe"  

@app.route("/init")
def init():
    un_usuario = request.args.get("content")

    if un_usuario == "alfa":
        return {"payload":un_usuario}
    else:  return "no esta"

if __name__ == "__Main__":
    app.run(debug=True)
