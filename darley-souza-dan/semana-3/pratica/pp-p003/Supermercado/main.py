import pickle


def add_product(products):
    auxCode = True
    
    while auxCode:
        code = input("Código(13 números): ")
        
        if len(code) != 13 or not code.isdigit():
            print("Código inválido!!!.")
        else:
            for product in products:
                if 'code' in product and code == product['code']:
                    print("Produto com esse código já existe!!!")
                    continue
                else:    
                    auxCode = False;

    while True:
        name = input("Nome do produto(Primeira letra maíuscula): ")
        if not name[0].isupper():
            print("Nome Inválido. Primeira letra precisa ser maíuscula")
        else:
            break

    price = "{:.2f}".format(float(input("Preço do produto: ")))

    product = {"name": name, "price": price, "code": code}
    products.append(product)
    print("Produto adicionado com sucesso!")


def delete_product(products):
    code = input("Entre com o código do produto: ")
    
    for product in products:
        if product["code"] == code:
            products.remove(product)
            print("Produto excluído!!!")
            return
    print("Produto não encontrado!!!!")


def list_products(products):
    for i, product in enumerate(products, start=1):
        print(
            f"{i}. Nome: {product['name']}, Preço: R${product['price']}, Código: {product['code']}"
        )


def check_price(products):
    code = input("Entre com o código do produto: ")
    for product in products:
        if product["code"] == code:
            print(f"{product['name']}: R${product['price']} ")
            return
    print("Produto não encontrado!!!!")


def save_to_file(products):
    with open("product_data.pkl", "wb") as file:
        pickle.dump(products, file)


def load_from_file():
    try:
        with open("product_data.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


def main():
    products = load_from_file()

    while True:
        print("\n--------- MENU ---------\n"
        "1. Adicionar novo produto\n"
        "2. Deletar produto\n"
        "3. Listar produtos\n"
        "4. Checar preço de um produto\n"
        "5. Exit\n\n")

        option = input("Selecione a opção: ")
        print();
        match option:
            case "1":
                add_product(products)
                print("Pressione Enter para continuar.")
                input()
                print();
            case "2":
                delete_product(products)
                print("Pressione Enter para continuar.")
                input()
                print();
            case "3":
                list_products(products)
                print("Pressione Enter para continuar.")
                input()
                print();
            case "4":
                check_price(products)
                print("Pressione Enter para continuar.")
                input()
                print();
            case "5":
                save_to_file(products)
                print("Saindo!!!!")
                break
            case _:
                print("Opção Inválida. Tente novamente!!")


if __name__ == "__main__":
    main()
