from flask_restful import Resource

lista_habilidades = ["Python", "Java", "Flask"]
class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    def put(self):
        # a partir de um id deve alterar a habilidade
        pass
    def post(self):
        # deve inserir uma habilidade nova na lista
        pass
    def delete(self):
        # deve deletar uma habilidade na posicao informada
        pass
