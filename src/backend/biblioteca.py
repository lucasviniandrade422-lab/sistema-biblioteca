from usuario import Usuario
from livro import Livro

class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.livros = []

    def cadastrar_usuario(self, nome, email):
        usuario = Usuario(nome, email)
        self.usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")

    def cadastrar_livro(self, titulo, autor):
        livro = Livro(titulo, autor)
        self.livros.append(livro)
        print("Livro cadastrado com sucesso!")

    def listar_livros(self):
        for livro in self.livros:
            print(livro)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.emprestar():
                    print("Livro emprestado com sucesso!")
                else:
                    print("Livro já está emprestado.")
                return
        print("Livro não encontrado.")
