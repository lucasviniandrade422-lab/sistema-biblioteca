from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# =========================
# "BANCO DE DADOS" MOCK
# =========================

usuarios = [
    {"id": 1, "email": "admin@email.com", "senha": "123"}
]

livros = [
    {"id": 1, "nome": "1984 - George Orwell", "disponivel": True},
    {"id": 2, "nome": "O Hobbit - Tolkien", "disponivel": True},
    {"id": 3, "nome": "Harry Potter - J.K Rowling", "disponivel": True},
    {"id": 4, "nome": "Dom Casmurro - Machado de Assis", "disponivel": True}
]

# =========================
# UTILITÁRIOS (PADRÃO RESPOSTA)
# =========================

def resposta_sucesso(mensagem, dados=None):
    return jsonify({
        "status": "sucesso",
        "mensagem": mensagem,
        "dados": dados
    }), 200


def resposta_erro(mensagem, status_code=400):
    return jsonify({
        "status": "erro",
        "mensagem": mensagem
    }), status_code


# =========================
# SERVIÇOS (LÓGICA)
# =========================

def autenticar_usuario(email, senha):
    for user in usuarios:
        if user["email"] == email and user["senha"] == senha:
            return user
    return None


def buscar_livro_por_id(livro_id):
    for livro in livros:
        if livro["id"] == livro_id:
            return livro
    return None


def emprestar_livro(livro):
    if not livro["disponivel"]:
        return False, "Livro já está emprestado"

    livro["disponivel"] = False
    return True, "Livro emprestado com sucesso"


def devolver_livro(livro):
    if livro["disponivel"]:
        return False, "Livro já está disponível"

    livro["disponivel"] = True
    return True, "Livro devolvido com sucesso"


# =========================
# ROTAS (API)
# =========================

@app.route("/", methods=["GET"])
def home():
    return resposta_sucesso("API Sistema de Biblioteca online")


# LOGIN
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    if not data:
        return resposta_erro("Dados não enviados")

    email = data.get("email")
    senha = data.get("senha")

    if not email or not senha:
        return resposta_erro("Email e senha são obrigatórios")

    usuario = autenticar_usuario(email, senha)

    if not usuario:
        return resposta_erro("Credenciais inválidas", 401)

    return resposta_sucesso("Login realizado com sucesso", {"usuario_id": usuario["id"]})


# LISTAR LIVROS
@app.route("/livros", methods=["GET"])
def listar_livros():
    return resposta_sucesso("Lista de livros", livros)


# EMPRESTAR
@app.route("/livros/<int:livro_id>/emprestar", methods=["POST"])
def rota_emprestar(livro_id):

    livro = buscar_livro_por_id(livro_id)

    if not livro:
        return resposta_erro("Livro não encontrado", 404)

    sucesso, mensagem = emprestar_livro(livro)

    if not sucesso:
        return resposta_erro(mensagem)

    return resposta_sucesso(mensagem, livro)


# DEVOLVER
@app.route("/livros/<int:livro_id>/devolver", methods=["POST"])
def rota_devolver(livro_id):

    livro = buscar_livro_por_id(livro_id)

    if not livro:
        return resposta_erro("Livro não encontrado", 404)

    sucesso, mensagem = devolver_livro(livro)

    if not sucesso:
        return resposta_erro(mensagem)

    return resposta_sucesso(mensagem, livro)


# =========================
# START
# =========================

if __name__ == "__main__":
    app.run(debug=True)
