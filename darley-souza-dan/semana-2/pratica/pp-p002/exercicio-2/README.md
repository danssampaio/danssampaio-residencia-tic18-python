### Exercício 2: Pesquisa sobre persistência de dados.

Utilizei a biblioteca pickle para serializar e desserializar os dados. Poderia utilizar um arquivo .txt para salvar e coletar os dados através de uma função com delimitador, mas como utilizei classes, consigo utilizar esta biblioteca. Este processo também se encontra na fstream do C++, mas um pouco mais bruto.

#### Pickle

Salva em um arquivo .pkl os dados convertidos em uma sequência de bytes.

    def save_to_file(self, filename="todolist.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.tasks, file)

Tenta coletar os dados do arquivo, caso não consiga, como execção, retorna para main para criação de uma nova lista.

    def load_from_file(self, filename="todolist.pkl"):
        try:
            with open(filename, "rb") as file:
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            print("Arquivo não encontrado. Criando nova lista.")

Função de saída, que chava a função para salvar os arquivos e finaliza o programa.

    def exit_and_save(self):
        self.save_to_file()
        print("Salvando e saindo!!!\n\n")
        time.sleep(2)
        exit()