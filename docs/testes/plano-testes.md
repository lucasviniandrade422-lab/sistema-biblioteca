# Plano de Testes

## Teste 1 - Empréstimo com sucesso

**Cenário:** Empréstimo de livro disponível
**Pré-condição:** Usuário cadastrado no sistema e livro disponível para empréstimo
**Entrada:** Usuário solicita empréstimo do livro
**Resultado esperado:** O sistema registra o empréstimo e altera o status do livro para indisponível

---

## Teste 2 - Livro indisponível

**Cenário:** Tentativa de empréstimo com livro já emprestado
**Pré-condição:** Livro já está emprestado para outro usuário
**Entrada:** Usuário tenta realizar o empréstimo do mesmo livro
**Resultado esperado:** O sistema bloqueia a operação e exibe mensagem de indisponibilidade

---

## Teste 3 - Usuário não cadastrado

**Cenário:** Tentativa de empréstimo por usuário não cadastrado
**Pré-condição:** Usuário não existe no sistema
**Entrada:** Usuário tenta solicitar empréstimo
**Resultado esperado:** O sistema impede a ação e informa que o usuário precisa estar cadastrado
