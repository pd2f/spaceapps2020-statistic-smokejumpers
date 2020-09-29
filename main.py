import werkzeug
from flask import Flask, jsonify, abort
from flask_restful import Api, reqparse

app = Flask(__name__)
api = Api(app)


@app.route("/", methods=['GET'])
def welcome():
    return jsonify(equipe="Smoke Jumpers", slogan= "Onde há fumaça, há smoke jumpers",
                   integrantes=["Alcemiro Leite da Silva Jr.","AMON FERREIRA LARA BERNARDINO",
                                    "Luiz Felippe Tolotti","Paulo Franco","Rafael Belém Mazaro",
                                    "Renan Cappi"],
                   component="API estatística Smoke Jumpers")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("1000"), debug=True)