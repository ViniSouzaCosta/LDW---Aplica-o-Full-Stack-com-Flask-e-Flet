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
    Busca um Digimon pelo ID
    ---
    tags:
      - Digimons
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do Digimon
    responses:
      200:
        description: Digimon encontrado
      404:
        description: Digimon não encontrado
    """

    for digimon in digimons:
        if digimon["id"] == id:
            return jsonify(digimon)

    return jsonify({"erro": "Digimon não encontrado"}), 404


@bp.route("/digimons", methods=["POST"])
def cadastrar_digimon():
    """
    Cadastra um novo Digimon
    ---
    tags:
      - Digimons
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              example: Patamon
            nivel:
              type: string
              example: Rookie
    responses:
      201:
        description: Digimon cadastrado com sucesso
      400:
        description: Erro de validação
    """

    dados = request.json

    try:
        novo = DigimonSchema(**dados)

    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 400

    digimon = {
        "id": len(digimons) + 1,
        "nome": novo.nome,
        "nivel": novo.nivel
    }

    digimons.append(digimon)

    return jsonify(digimon), 201