import pickle


def display_person(person):
    print(
        f"Nome: {person['name']}, Sobrenome: {person['surname']}, Ano de Nascimento: {person['birthYear']}, RG: {person['rg']}, Ano de admissão: {person['hireYear']}, Salário: {person['salary']}"
    )


def display_all_people(people):
    for person in people:
        display_person(person)
        print()


def add_person(people):
    name = input("Nome: ")
    surname = input("Sobrenome: ")
    birthYear = int(input("Ano de Nascimento: "))
    rg = input("RG: ")
    hireYear = int(input("Ano de Admissão: "))
    salary = float(input("Salário: "))

    person = {
        "name": name,
        "surname": surname,
        "birthYear": birthYear,
        "rg": rg,
        "hireYear": hireYear,
        "salary": salary,
    }

    people.append(person)
    print("Cadastro Realizado!!")


def edit_person(people):
    editRg = input("RG: ")

    for person in people:
        if person["rg"] == editRg:
            print("Current details:")
            display_person(person)

            person["name"] = input("Nome: ")
            person["surname"] = input("Sobrenome: ")
            person["birthYear"] = int(input("Ano de Nascimento: "))
            person["hireYear"] = int(input("Ano de Admissão: "))
            person["salary"] = float(input("Salário: "))

            print("Cadastro Editado!!")
            return

    print("Pessoa não encontrada!!")


def delete_person(people):
    deleteRg = input("Rg: ")

    for person in people:
        if person["rg"] == deleteRg:
            people.remove(person)
            print("Cadastro Deletado!!")
            return

    print("Pessoa não encontrada!!")


def adjust_salary(people):
    for person in people:
        person["salary"] *= 1.1

    print("Salário Ajustado!!")


def save_data(file_name, data):
    with open(file_name, "wb") as file:
        pickle.dump(data, file)


def load_data(file_name):
    try:
        with open(file_name, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


def main():
    file_name = "people.pkl"
    people = load_data(file_name)

    while True:
        print("\n------- Menu -------\n"
        "1. Cadastrar Pessoa\n"
        "2. Editar Pessoa\n"
        "3. Deletar Pessoa\n"
        "4. Listar Pessoas\n"
        "5. Ajustar Salário\n"
        "6. Sair\n\n")
        
        choice = input("Selecione a  opção: ")

        match choice:
            case "1":
                add_person(people)
                print("Pressione Enter para continuar.")
                input()
                print()
            case "2":
                edit_person(people)
                print("Pressione Enter para continuar.")
                input()
                print()
            case "3":
                delete_person(people)
                print("Pressione Enter para continuar.")
                input()
                print()
            case "4":
                display_all_people(people)
                print("Pressione Enter para continuar.")
                input()
                print()
            case "5":
                adjust_salary(people)
                print("Pressione Enter para continuar.")
                input()
                print()
            case "6":
                save_data(file_name, people)
                print("Saindo!!!")
                break
            case _:
                print("Opção Inválida. Tente Novamente!!")


if __name__ == "__main__":
    main()
