from flask import Blueprint, jsonify, request
from schemas.digimon_schema import DigimonSchema

bp = Blueprint("digimons", __name__)

digimons = [
    {
        "id": 1,
        "nome": "Agumon",
        "nivel": "Rookie"
    },
    {
        "id": 2,
        "nome": "Gabumon",
        "nivel": "Rookie"
    }
]

@bp.route("/digimons", methods=["GET"])
def listar_digimons():
    """
    Lista todos os Digimons
    ---
    tags:
      - Digimons
    responses:
      200:
        description: Lista de Digimons
    """
    return jsonify(digimons)

@bp.route("/digimons/<int:id>", methods=["GET"])
def buscar_digimon(id):
    """
    Busca Digimon por ID
    ---
    tags:
      - Digimons
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Digimon encontrado
    """
    for digimon in digimons:
        if digimon["id"] == id:
            return jsonify(digimon)

    return jsonify({"erro": "Digimon não encontrado"}), 404

@bp.route("/digimons", methods=["POST"])
def cadastrar_digimon():

    dados = request.json

    try:
        novo = DigimonSchema(**dados)
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

    digimon = {
        "id": len(digimons) + 1,
        "nome": novo.nome,
        "nivel": novo.nivel
    }

    digimons.append(digimon)

    return jsonify(digimon), 201    