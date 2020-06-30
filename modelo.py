from config import *

class Esporte(db.Model):
    nome = db.Column(db.String(254, primary_key=True))
    modalidade = db.Column(db.String(254))

    def __str__(self):
        return str(self.nome)+") "+ self.modalidade + ", "

        def json(self):
            return {
            "nome": self.nome,
            "modalidade": self.modalidade
        }

if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    p1= Esporte(nome="Arremesso de Dardo", modalidade="Atletismo")
    p2= Esporte(nome="Arremesso de peso", modalidade = "Atletismo")

    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    
    print(p2)

    print(p2.json())