from config import *
from modelo import Esporte

@app.route("/")
def inicio():
    return 'Sistema para cadastro de modalidades esportivas '+\
        '<a href="/listar_modalidades">listar</a>'

@app.route("/listar_modalidades")
def listar_modalidades():
    esportes = db.session.query(Esporte).all()
    esporte_em_json = [x.json() for x in esportes]
    resposta = jsonify(esporte_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

app.run(debug=True)

