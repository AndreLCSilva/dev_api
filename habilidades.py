from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'PHP', 'JavaScript', 'HTML', 'CSS', 'C#']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
