# 📝 App de Gerenciamento de Tarefas

Bem-vindo ao **App de Gerenciamento de Tarefas**, um aplicativo simples e intuitivo para ajudar a organizar suas atividades pessoais e profissionais diretamente do terminal.

Este projeto foi desenvolvido em Python e armazena todas as suas tarefas em um arquivo de texto simples (`tarefas.txt`), sem a necessidade de um banco de dados complexo.

## 🚀 Funcionalidades

O aplicativo oferece as seguintes funcionalidades:

-   **Adicionar Tarefa**: Inclua um título, descrição e data de vencimento para cada nova tarefa.
-   **Listar Tarefas**: Visualize todas as suas tarefas, com detalhes e status (Pendente ou Concluída).
-   **Marcar como Concluída**: Mude o status de uma tarefa de "Pendente" para "Concluída".

## 🛠️ Como Usar

### Pré-requisitos

Certifique-se de ter o **Python** instalado em seu computador. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

### Passo a Passo

1.  **Clone o repositório** para sua máquina local:
    ```bash
    git clone [https://github.com/SeuNome/app-de-tarefas.git](https://github.com/SeuNome/app-de-tarefas.git)
    ```
    (Lembre-se de substituir `SeuNome/app-de-tarefas` pelo caminho do seu repositório no GitHub).
2.  **Navegue até a pasta do projeto**:
    ```bash
    cd app-de-tarefas
    ```
3.  **Execute o aplicativo**:
    ```bash
    python meu_app.py
    ```

Ao executar o programa, um menu interativo será exibido no seu terminal, permitindo que você adicione, liste e gerencie suas tarefas.

## 📁 Estrutura do Projeto

-   `meu_app.py`: O código-fonte principal do aplicativo.
-   `tarefas.txt`: (Gerado automaticamente) Arquivo de texto onde as tarefas são salvas.

---

Este `README.md` cobre todas as informações essenciais. Para adicioná-lo ao seu projeto e enviá-lo para o GitHub, você pode usar os seguintes comandos:

```bash
# Adiciona o novo arquivo README.md
git add README.md

# Salva a alteração com uma mensagem descritiva
git commit -m "Adiciona o arquivo README"

# Envia o arquivo para o seu repositório no GitHub
git push origin main