

from config import *

class Esporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    modalidade = db.Column(db.String(254))
    pais_favorito = db.Column(db.String(254))    
    atleta = db.Column(db.String(254))
    nivel_de_dificuldade = db.Column(db.String(254))

    def __str__(self):
        return  str(self.id)+") " + self.nome + ", " +\
            str(self.modalidade) + " , " + str(self.pais_favorito) + " , " +\
                str(self.atleta) + " , " + str(self.nivel_de_dificuldade)

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome ,
            "modalidade": self.modalidade,
            "pais_favorito": self.pais_favorito,
            "atleta": self.atleta,
            "nivel_de_dificuldade": self.nivel_de_dificuldade,
        }
class Campeonato(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    nome_campeonato = db.Column(db.String(254)) 
    local = db.Column(db.String(254))

    def __str__(self):
        return F"{self.nome_campeonato} [{self.id}], local={self.local}"

    def json(self):
        return {
            "id":self.id,
            "nome_campeonato": self.nome_campeonato,
            "local": self.local
        }

class CampeonatoRealizado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(254))
    ganhador = db.Column(db.String(254))

    esporte_id = db.Column(db.Integer, db.ForeignKey(Esporte.id), nullable=False)
    esporte = db.relationship("Esporte")
    campeonato_id = db.Column(db.Integer, db.ForeignKey(Campeonato.id), nullable=False)
    campeonato = db.relationship("Campeonato")

    def __str__(self):
        return F"{self.data}, {self.ganhador}, {self.esporte}, {self.campeonato}"

    def json(self):
        "id":self.id,
        "data":self.data,
        "ganhador":self.ganhador,
        "esporte_id":self.esporte_id,
        "esporte":self.esporte.json(),
        "campeonato_id":self.campeonato_id,
        "campeonato":self.campeonato.json()


class Elenco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atleta = db.Column(db.String(254))
    tecnico = db.Column(db.String(254))
    aux_tecnico = db.Column(String(254))
    medico = db.Column(String(254))
    
    esporte_id = bd.Column(db.Integer, db.ForgeingKey(Esporte.id))
    esporte = db.relationship("Esporte")


if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    p1= Esporte(nome="100 metros rasos", modalidade="Atletismo", pais_favorito="Jamaica", atleta="Usain Bolt", nivel_de_dificuldade="10")
    p2= Esporte(nome="Arremesso de peso", modalidade = "Atletismo", pais_favorito="Brasil", atleta="Jorge", nivel_de_dificuldade="10" )

    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    
    print(p1.json())
    print(p2.json())
    