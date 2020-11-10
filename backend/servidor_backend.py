from config import *
from modelo import Esporte, Campeonato, CampeonatoRealizado

@app.route("/")
def inicio():
    return 'Sistema para cadastro de modalidades esportivas '+\
        '<a href="/listar_modalidades">Listar Modalidades</a>'

@app.route("/listar_modalidades")
def listar_modalidades():

    esportes = db.session.query(Esporte).all()
    esporte_em_json = [Esporte.json() for Esporte in esportes]
    
    return (jsonify(esporte_em_json))


@app.route("/incluir_modalidades", methods=['POST'])
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

@app.route("/excluir_modalidades/<int:modalidades_id>", methods=['DELETE'])
def excluir_modalidades(modalidades_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Esporte.query.filter(Esporte.id == modalidades_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta    

@app.route("/listar_campeonatos_realizados")
def listar_campeonatos_realizados():
    campeonatos_realizados= db.session.query(CampeonatoRealizado).all()
    lista_json = [ x.json() for x in campeonatos_realizados ]
    resposta = jsonify(lista_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listar/<string:classe>")
def listar(classe):
    dados = None
    if classe == "CampeonatoRealizado":
        dados = db.session.query(CampeonatoRealizado).all()
    elif classe == "Esporte":
        dados = db.session.query(Esporte).all() 
    elif classe == "Campeonato":
        dados = db.session.query(Campeonato).all()
    lista_json = [x.json() for x in dados]
    resposta = jsonify(lista_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


app.run(debug=True)

