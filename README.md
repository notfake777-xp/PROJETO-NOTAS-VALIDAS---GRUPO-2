<<<<<<< HEAD
# PROJETO-NOTAS-VALIDAS---GRUPO-2
# REGRAS DO HISTÓRICO
# O CÓDIGO COMEÇA ESTRUTURANDO OS DADOS EM DICIONÁRIOS
# EXISTEM TRÊS DICIONÁRIOS PRINCIPAIS: dicionário para armazenar informações dos alunos, dicionário para armazenar informações das disciplinas e um dicionário para armazenar informações 
=======
# Sistema de Registro de Notas Académicas

Este é um sistema desenvolvido em **Python** para a gestão e registo de notas de estudantes. O projeto foi estruturado de forma modular, onde cada funcionalidade principal foi desenvolvida em diferentes ramificações (*branches*) pelo grupo de trabalho e, posteriormente, integrada na ramificação principal (`main`).

---

## 🛠️ Arquitetura e Módulos do Sistema

O ficheiro principal do sistema é o `main.py`, que atua como o orquestrador, importando e gerindo o fluxo de execução dos seguintes módulos:

* **`cadastro_aluno`**: Responsável pelas funções de registo e listagem dos estudantes (`cadastrar_aluno`, `listar_alunos`).
* **`cadastro_disciplina`**: Responsável pela gestão das disciplinas do sistema (`cadastrar_diplina`, `listar_disciplinas`).
* **`inserir_notas`**: Módulo que permite a atribuição e inserção de notas aos alunos.
* **`calculo_media`**: Contém as regras de negócio para calcular a média das notas obtidas.
* **`situacao_aluno`**: Avalia e valida a situação final do estudante (ex: Aprovado, Reprovado, Exame) com base na média.
* **`historico_aluno`**: Gera e exibe o histórico completo dos estudantes e as respetivas notas.
* **`interface_usuario`**: Gere toda a componente visual no terminal (`exibir_menu`, `obter_opcao`, `limpar_tela`, `exibir_cabecalho`).
* **`validacoes`**: Garante a integridade dos dados inseridos no menu (`validar_opcao_menu`).

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Antes de começar, certifique-se de que tem o **Python 3** instalado no seu computador.

### 1. Clonar o Repositório e Sincronizar as Branches
Se acabou de descarregar o projeto ou precisa de garantir que todas as funcionalidades desenvolvidas pela equipa estão na sua máquina, execute os seguintes comandos no terminal:

```bash
# Aceder à branch principal
git checkout main

# Atualizar o repositório local com o servidor
git pull origin main

# Unir os módulos das outras branches na main (exemplo)
git merge nome-da-branch-do-modulo
>>>>>>> 7770c930b76a5fd9acc46207994716eccab1d8b4
