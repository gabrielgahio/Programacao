from config import *
from modelo import Esporte

@app.route("/")
def inicio():
    return 'Sistema para cadastro de modalidades esportivas '+\
        '<a href="/listar_modalidades">Listar Modalidades</a>'

@app.route("/listar_modalidades")
def listar_modalidades():

    esportes = db.session.query(Esporte).all()
    esporte_em_json = [Esporte.json() for Esporte in esportes]
    
    return (jsonify(esporte_em_json))

app.run(debug=True)

