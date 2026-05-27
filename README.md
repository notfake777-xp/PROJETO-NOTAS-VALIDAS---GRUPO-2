# 📚 Sistema de Registro de Notas
**Projeto Acadêmico em Grupo - Notas Validas | Git & GitHub**

---

## 👥 Equipe e Branches

| Membro     | Branch              | Arquivo              |
|------------|---------------------|----------------------|
| Salatiel   | main                | main.py              |
| Pedro      | cadastro aluno      | cadastro_aluno.py    |
| Richard    | cadastro disciplina | cadastro_disciplina.py |
| Felipe     | inserir notas       | inserir_notas.py     |
| Neto       | Calculo media       | calculo_media.py     |
| Daniel     | situação aluno      | situacao_aluno.py    |
| Anderson   | Histórico aluno     | historico_aluno.py   |
| Soares     | interface usuário   | interface_usuario.py |
| Iago       | validações          | validacoes.py        |
| Danilo     | Develop             | develop.py           |

---

## 🚀 Como Usar o Git (Passo a Passo)

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/registro-notas.git
cd registro-notas
```

### 2. Cada membro cria/acessa sua branch
```bash
# Criar a branch (primeira vez)
git checkout -b "nome-da-sua-branch"

# Ou acessar uma branch já existente
git checkout "nome-da-sua-branch"
```

### 3. Trabalhar no seu arquivo e salvar alterações
```bash
git add nome-do-seu-arquivo.py
git commit -m "feat: descrição do que foi feito"
git push origin "nome-da-sua-branch"
```

### 4. Enviar para a branch Develop (via Pull Request)
- Acesse o GitHub
- Clique em "Compare & Pull Request"
- Direcione para a branch **Develop**
- Aguarde revisão do responsável (Iago)

### 5. Após todos aprovados, Develop vai para Main
- Somente após testes passarem no develop.py
- Pull Request: **Develop → Main** (responsável: Salatiel)

---

## 🗂️ Estrutura do Projeto
```
registro-notas/
│
├── main.py                  # Ponto de entrada (Salatiel)
├── cadastro_aluno.py        # Cadastro de alunos (Pedro)
├── cadastro_disciplina.py   # Cadastro de disciplinas (Richard)
├── inserir_notas.py         # Inserção de notas (Felipe)
├── calculo_media.py         # Cálculo de médias (Neto)
├── situacao_aluno.py        # Situação do aluno (Daneil)
├── historico_aluno.py       # Histórico acadêmico (Anderson)
├── interface_usuario.py     # Interface do terminal (Soares)
├── validacoes.py            # Validações de dados (Iago)
├── develop.py               # Testes e integração (Danilo)
│
└── dados/                   # Criado automaticamente
    ├── alunos.json
    ├── disciplinas.json
    └── historico.json
```

---

## ▶️ Como Executar
```bash
python main.py
```
> Requer Python 3.10+

---

## 📌 Regras da Equipe
- **Nunca** commitar direto na `main`
- Todo código passa pela branch `Develop` antes
- Use mensagens de commit descritivas:
  - `feat:` nova funcionalidade
  - `fix:` correção de bug
  - `refactor:` melhoria de código
- Cada membro só mexe no **seu arquivo**
