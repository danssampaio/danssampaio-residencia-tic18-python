import time, pickle


class Task:
    def __init__(self, description, completed=False):
        self.description = description.capitalize()
        self.completed = completed

    def mark_as_completed(self):
        if not self.completed:
            self.completed = True
            print("Tarefa marcada como concluída!!!\n\n")
        else:
            print("Esta tarefa já foi concluída.\n\n")

    def mark_as_incompleted(self):
        if self.completed:
            self.completed = False
            print("Tarefa marcada como inconcluída!!!\n\n")
        else:
            print("Esta tarefa já está como inconcluída.\n\n")

    def edit_description(self, new_description):
        self.description = new_description.capitalize()
        print("Tarefa alterada com sucesso!!!\n\n")

    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        return f"{self.description} {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def list_tasks(self):
        if len(self.tasks) == 0:
            print("Não existem tarefas!!!\n\n")
        else:
            print("Lista de tarefas:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}.{task}")

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Tarefa adicionada!!!\n\n")

    def mark_as_completed(self, identifier):
        if 1 <= identifier <= len(self.tasks):
            self.tasks[identifier - 1].mark_as_completed()
            self.sort_tasks()
        else:
            print("Identificador inválido ou tarefa já concluída!!\n\n")
            
    def mark_as_incompleted(self, identifier):
        if 1 <= identifier <= len(self.tasks):
            self.tasks[identifier - 1].mark_as_incompleted()
            self.sort_tasks()
        else:
            print("Identificador inválido ou tarefa já inconcluída!!\n\n")

    def edit_task(self, identifier, new_description):
        if 1 <= identifier <= len(self.tasks):
            self.tasks[identifier - 1].edit_description(new_description)
        else:
            print("Identificador inválido!!\n\n")

    def sort_tasks(self):
        self.tasks.sort(key=lambda x: not x.completed)
        
        
    def save_to_file(self, filename="todolist.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.tasks, file)

    def load_from_file(self, filename="todolist.pkl"):
        try:
            with open(filename, "rb") as file:
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            print("Arquivo não encontrado. Criando nova lista.")

    def exit_and_save(self):
        self.save_to_file()
        print("Salvando e saindo!!!\n\n")
        time.sleep(2)
        exit()


def main():
    to_do_list = ToDoList()
    to_do_list.load_from_file()

    while True:
        print("\n ------ Menu------\n")
        print("1. Listar Tarefas")
        print("2. Adicionar Nova Tarefa")
        print("3. Marcar Tarefa como Concluída")
        print("4. Marcar Tarefa como Inconcluída")
        print("5. Editar Tarefa")
        print("6. Sair\n")

        option = input("Selecione a opção: ")
        print("\n\n")

        match option:
            case "1":
                to_do_list.list_tasks()
            case "2":
                description = input("Descrição: ")
                to_do_list.add_task(description)
            case "3":
                to_do_list.list_tasks()
                identifier = int(input("Selecione qual tarefa deseja marcar como concluída: "))
                to_do_list.mark_as_completed(identifier)
            case "4":
                to_do_list.list_tasks()
                identifier = int(input("Selecione qual tarefa deseja marcar como inconcluída: "))
                to_do_list.mark_as_incompleted(identifier)
            case "5":
                to_do_list.list_tasks()
                print("\n")
                identifier = int(input("Selecione qual tarefa deseja editar: "))
                new_description = input("Digite a nova descrição: ")
                to_do_list.edit_task(identifier, new_description)
            case "6":
                to_do_list.exit_and_save()
            case _:
                print("Opção inválida!!!\n\n")

if __name__ == "__main__":
    main()
