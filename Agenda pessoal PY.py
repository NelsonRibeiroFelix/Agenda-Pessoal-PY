# Nome do arquivo onde as tarefas serão salvas
NOME_ARQUIVO = 'tarefas.txt'

def adicionar_tarefa():
    """Adiciona uma nova tarefa ao arquivo de tarefas."""
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    data = input("Digite a data de vencimento (dd/mm/aaaa): ")
    
    # A tarefa é salva no formato: Título | Descrição | Data | Status (Pendente/Concluída)
    # Inicialmente, o status é sempre "Pendente"
    nova_tarefa = f"{titulo}|{descricao}|{data}|Pendente\n"
    
    with open(NOME_ARQUIVO, 'a') as arquivo:
        arquivo.write(nova_tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    """Lê o arquivo de tarefas e lista todas elas."""
    try:
        with open(NOME_ARQUIVO, 'r') as arquivo:
            tarefas = arquivo.readlines()
            
            if not tarefas:
                print("Nenhuma tarefa encontrada.")
                return
            
            print("\n--- SUAS TAREFAS ---")
            for i, linha in enumerate(tarefas):
                # Remove espaços e quebras de linha
                tarefa_info = linha.strip().split('|')
                # Desempacota as informações da tarefa
                titulo, descricao, data, status = tarefa_info
                
                print(f"{i+1}. Título: {titulo}")
                print(f"   Descrição: {descricao}")
                print(f"   Data: {data}")
                print(f"   Status: {status}")
                print("-" * 20)
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")

def marcar_como_concluida():
    """Marca uma tarefa como concluída, atualizando o arquivo."""
    listar_tarefas()
    try:
        num_tarefa = int(input("Digite o número da tarefa para marcar como concluída: "))
        
        with open(NOME_ARQUIVO, 'r') as arquivo:
            linhas = arquivo.readlines()
        
        # Verifica se o número da tarefa é válido
        if 0 < num_tarefa <= len(linhas):
            tarefa_modificada = linhas[num_tarefa - 1].strip().split('|')
            # Muda o status de "Pendente" para "Concluída"
            tarefa_modificada[3] = "Concluída"
            
            # Reconstroi a linha com o novo status
            linhas[num_tarefa - 1] = "|".join(tarefa_modificada) + "\n"
            
            with open(NOME_ARQUIVO, 'w') as arquivo:
                arquivo.writelines(linhas)
            print("Tarefa marcada como concluída!")
        else:
            print("Número de tarefa inválido.")
    except (ValueError, IndexError):
        print("Entrada inválida. Por favor, digite um número.")

def menu_principal():
    """Exibe o menu principal e gerencia a interação do usuário."""
    while True:
        print("\n--- MENU ---")
        print("1. Adicionar nova tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar_tarefa()
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            marcar_como_concluida()
        elif escolha == '4':
            print("Saindo do aplicativo. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu principal quando o programa é iniciado
if __name__ == "__main__":
    menu_principal()