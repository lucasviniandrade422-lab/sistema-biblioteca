
# Sistema simples de biblioteca

# Dados simulados
usuarios = ["Lucas", "Maria"]
livros = {
    "Python Básico": True,
    "Algoritmos": True,
    "Banco de Dados": False  # já emprestado
}

def emprestar_livro(usuario, livro):
    # Verifica se usuário existe
    if usuario not in usuarios:
        return "Erro: usuário não cadastrado."

    # Verifica se livro existe
    if livro not in livros:
        return "Erro: livro não encontrado."

    # Verifica disponibilidade
    if not livros[livro]:
        return "Erro: livro indisponível."

    # Realiza empréstimo
    livros[livro] = False
    return f"Empréstimo realizado com sucesso para {usuario}."

# Testes no terminal
print(emprestar_livro("Lucas", "Python Básico"))  # sucesso
print(emprestar_livro("Lucas", "Banco de Dados"))  # indisponível
print(emprestar_livro("João", "Python Básico"))  # usuário não cadastrado
