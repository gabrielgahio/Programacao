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


@app.route("/incluir_modalidade", methods=['POST'])
def incluir_modalidade():
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    dados = request.get_json()
    try:   
        nova=Esporte(**dados)
        db.session.add(nova)
        db.session.commit()
        
    except Exception as e: 
        resposta = jsonify({"resultado":"erro","detalhes":str(e)})
        
    resposta.headers.add("Access-Control-Allow-Origin","*")
    
    return resposta


app.run(debug=True)

