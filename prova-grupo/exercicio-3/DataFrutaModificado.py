from abc import ABC, abstractmethod
from datetime import datetime


class Data:
    def __init__(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano

    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return (
            self.__dia == outraData.__dia
            and self.__mes == outraData.__mes
            and self.__ano == outraData.__ano
        )

    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False

    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False


class AnaliseDados(ABC):
    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass

    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

    @abstractmethod
    def listarEmOrdem(self):
        pass


class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(tipoDeDados=str)
        self.__lista = []
        self.__index = 0

    def entradaDeDados(self):
        while True:
            try:
                n = int(input("Quantos nomes deseja adicionar? "))
                break  
            except ValueError:
                print("Por favor, insira um valor inteiro válido.")

        for _ in range(n):
            nome = input("Digite um nome: ")
            self.__lista.append(nome)

    def mostraMediana(self):
        sorted_list = sorted(self.__lista)
        n = len(sorted_list)
        if n % 2 == 0:
            median = sorted_list[n // 2 - 1]
            print(f"Mediana: {median}")
        else:
            median = sorted_list[n // 2]
            print(f"Mediana: {median}")

    def mostraMenor(self):
        print(f"Menor: {min(self.__lista)}")

    def mostraMaior(self):
        print(f"Maior: {max(self.__lista)}")

    def listarEmOrdem(self):
        sorted_list = sorted(self.__lista)
        print("Lista em ordem:")
        print(", ".join(sorted_list))

    def __str__(self):
        return ", ".join(self.__lista)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < len(self.__lista):
            result = self.__lista[self.__index]
            self.__index += 1
            return result
        else:
            self.__index = 0
            raise StopIteration


class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(tipoDeDados=Data)
        self.__lista = []

    def entradaDeDados(self):
        while True:
            try:
                n = int(input("Quantas datas deseja adicionar? "))
                break  
            except ValueError:
                print("Por favor, insira um valor inteiro válido.")

        for _ in range(n):
            while True:
                try:
                    print("Digite a data no formato dia/mês/ano: ")
                    data_input = input().split("/")
                    dia = int(data_input[0])
                    mes = int(data_input[1])
                    ano = int(data_input[2])

                    if ano < 2000 or mes < 1 or mes > 12 or dia < 1:
                        raise ValueError("A data inserida não atende aos requisitos.")

                    data = Data(dia, mes, ano)
                    self.__lista.append(data)
                    break

                except ValueError as e:
                    print(f"Erro: {e}. Tente novamente.")

    def mostraMediana(self):
        sorted_list = sorted(self.__lista, key=lambda x: (x.ano, x.mes, x.dia))
        n = len(sorted_list)
        if n % 2 == 0:
            median = sorted_list[n // 2 - 1]
            print(f"Mediana: {median}")
        else:
            median = sorted_list[n // 2]
            print(f"Mediana: {median}")

    def mostraMenor(self):
        menor_data = min(self.__lista, key=lambda x: (x.ano, x.mes, x.dia))
        print(f"Menor: {menor_data}")

    def mostraMaior(self):
        maior_data = max(self.__lista, key=lambda x: (x.ano, x.mes, x.dia))
        print(f"Maior: {maior_data}")

    def listarEmOrdem(self):
        sorted_list = sorted(self.__lista, key=lambda x: (x.ano, x.mes, x.dia))
        print("Lista em ordem:")
        print("\n".join(str(data) for data in sorted_list))

    def __str__(self):
        return "\n".join(str(data) for data in self.__lista)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__lista):
            result = self.__lista[self.__index]
            self.__index += 1
            return result
        else:
            self.__index = 0
            raise StopIteration


class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(tipoDeDados=float)
        self.__lista = []

    def entradaDeDados(self):
        try:
            n = int(input("Quantos salários deseja adicionar? "))
            for _ in range(n):
                while True:
                    try:
                        salario = float(input("Digite um salário: "))
                        break
                    except ValueError:
                        print("Por favor, insira um valor numérico válido.")
                self.__lista.append(salario)
        except ValueError:
            print("Por favor, insira um número válido para a quantidade de salários.")

    def mostraMediana(self):
        sorted_list = sorted(self.__lista)
        n = len(sorted_list)

        if n % 2 == 0:
            median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
            print(f"Mediana: {median:.2f}")
        else:
            median = sorted_list[n // 2]
            print(f"Mediana: {median:.2f}")

    def mostraMenor(self):
        print(f"Menor: {min(self.__lista):.2f}")

    def mostraMaior(self):
        print(f"Maior: {max(self.__lista):.2f}")

    def listarEmOrdem(self):
        sorted_list = sorted(self.__lista)
        print("Lista em ordem:")
        print(", ".join(map(str, sorted_list)))

    def __str__(self):
        return ", ".join(map(str, self.__lista))

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__lista):
            result = self.__lista[self.__index]
            self.__index += 1
            return result
        else:
            self.__index = 0
            raise StopIteration


class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__(tipoDeDados=int)
        self.__lista = []

    def entradaDeDados(self):
        try:
            n = int(input("Quantas idades deseja adicionar? "))
        except:
            print("Digite um valor numérico!!\n")

        for _ in range(n):
            while True:
                try:
                    idade = int(input("Digite uma idade: "))
                    break
                except:
                    print("Digite um valor numérico!!\n")
            self.__lista.append(idade)

    def mostraMediana(self):
        sorted_list = sorted(self.__lista)
        n = len(sorted_list)
        if n % 2 == 0:
            median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
            print(f"Mediana: {median}")
        else:
            median = sorted_list[n // 2]
            print(f"Mediana: {median}")

    def mostraMenor(self):
        print(f"Menor: {min(self.__lista)}")

    def mostraMaior(self):
        print(f"Maior: {max(self.__lista)}")

    def listarEmOrdem(self):
        sorted_list = sorted(self.__lista)
        print("Lista em ordem:")
        print(", ".join(map(str, sorted_list)))

    def __str__(self):
        return ", ".join(map(str, self.__lista))


def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()
    listaListas = [nomes, salarios, datas, idades]

    while True:
        print("\n------ Menu ------")
        print(
            "1. Incluir nomes na lista de nomes\n"
            + "2. Incluir salários na lista de salários\n"
            + "3. Incluir datas na lista de datas\n"
            + "4. Incluir idades na lista de idades\n"
            + "5. Percorrer as listas de nomes e salários\n"
            + "6. Calcular o valor da folha com um reajuste de 10%\n"
            + "7. Modificar o dia das datas anteriores a 2019\n"
            + "8. Sair"
        )

        opcao = input("Selecione a opção: ")

        print("\n")

        match (opcao):
            case "1":
                listaListas[0].entradaDeDados()
                listaListas[0].mostraMediana()
                listaListas[0].mostraMenor()
                listaListas[0].mostraMaior()
                listaListas[0].listarEmOrdem()
                print("------------------------------------\n\n")
            case "2":
                listaListas[1].entradaDeDados()
                listaListas[1].mostraMediana()
                listaListas[1].mostraMenor()
                listaListas[1].mostraMaior()
                listaListas[1].listarEmOrdem()
                print("------------------------------------\n")
            case "3":
                listaListas[2].entradaDeDados()
                listaListas[2].mostraMediana()
                listaListas[2].mostraMenor()
                listaListas[2].mostraMaior()
                listaListas[2].listarEmOrdem()
                print("------------------------------------\n")
            case "4":
                listaListas[3].entradaDeDados()
                listaListas[3].mostraMediana()
                listaListas[3].mostraMenor()
                listaListas[3].mostraMaior()
                listaListas[3].listarEmOrdem()
                print("------------------------------------\n")
            case "5":
                for nome, salario in zip(nomes, salarios):
                    print(f"{nome}: R${salario:.2f}")
            case "6":
                salarios_reajustados = map(lambda salario: salario * 1.1, salarios)
                for salario in salarios_reajustados:
                    print(f"Novo Salário: R${salario:.2f}")
            case "7":
                datas_modificadas = filter(lambda x: x.ano < 2019, datas)
                for data in datas_modificadas:
                    data.dia = 1
                    print(data)
            case "8":
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Por favor, selecione uma opção válida.")


if __name__ == "__main__":
    main()
