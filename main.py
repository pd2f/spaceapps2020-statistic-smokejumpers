import werkzeug
from flask import Flask, jsonify, abort, redirect, url_for, request
from flask_restplus import Api, Resource, reqparse
import os
import Ativo as atv

app = Flask(__name__)
# api = Api(app)
parser = reqparse.RequestParser()

# @app.route("/ativo/<int:id>", methods=['POST'])
# def cadastrar_ativo(id):
#     return jsonify(id=id, dados=request.get_json(force=True))

# @app.route("/ativo/<int:id>", methods=['GET'])
# def consultar_ativo(id):
#     return jsonify(id=id)

@app.route("/", methods=['GET'])
def welcome():
    return redirect('/documentacao')


app_infos = dict(version='1.0', title='Statistical SKOPE',
                 description='API para AI & ML do SKOPE',
                 contact_email='paulodanielff@gmail.com', doc='/documentacao',
                 prefix='/api')
rest_app = Api(app, **app_infos)
team_endpoint = rest_app.namespace('team',
                                   description='Esse endpoint apresenta dados gerais do projeto e do time.')


@team_endpoint.route("/")
class Team(Resource):
    def get(self):
        return jsonify(equipe="Smoke Jumpers", slogan="Cuidando do ativo mais importante: vida humana",
                       integrantes=["Alcemiro Leite da Silva Jr.", "Amon Ferreira Lara Bernardino",
                                    "Luiz Felippe Tolotti", "Paulo Franco", "Rafael Belém Mazaro",
                                    "Renan Cappi"],
                       component="API estatística Smoke Jumpers")


ativo_endpoint = rest_app.namespace('ativo',
                                    description='Esse endpoint é utilizado para o cadastramento do ativo.')


@ativo_endpoint.route("/<int:id>")
class cadastro_ativo(Resource):
    def post(self,id):
        #json_data = request.get_json(force=True)
        json_data="teste_mock"
        ret = atv.cadastrar_ou_retornar_ativo(id,json_data)
        if ret[0] != 200:
            abort(ret[0], description=ret[1])
        return ret[1],ret[0]

    def get(self,id):
        return  atv.inferencia(id)

incendio_endpoint = rest_app.namespace('incendio',
                                    description='Esse endpoint é utilizado para investigação da causa raiz do incêndio')


@incendio_endpoint.route("/<int:id>")
class cadastro_incendio(Resource):
    def post(self,id):
        json_data = request.get_json(force=True)
        return jsonify(json_data)

    def get(self,id):
        return jsonify(id=id)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
