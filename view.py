import Controller
import os.path

def arq_register(*args):
    for i in args:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write("")
arq_register("category.txt", "client.txt", "stock.txt", "provider.txt", "employee.txt", "sale.txt" )


if __name__ == "__main__":
    while True:
        place = int(input("Digite 1 para acessar ( Categoria )\n"
                          "Digite 2 para acessar ( Estoque )\n"
                          "Digite 3 para acessar ( Fornecedor )\n"
                          "Digite 4 para acessar ( cliente )\n"
                          "Digite 5 para acessar ( Funinario )\n"
                          "Digite 6 para acessar ( Categoria )\n"
                          "Digite 7 para ver produtos vendidos\n"
                          "Digite 8 para sair\n"))

        if place == 1:
            cat = Controller.ControllerCategory()
            while True:
                decide = int(input("Digite 1 para cadastrar categoria\n"
                          "Digite 2 para remover categoria\n"
                          "Digite 3 para alterar categoria\n"
                          "Digite 4 para mostar categorias cadastradas\n"
                          "Digite 5 para sair\n"))

                if decide == 1:
                    category = input("Digite a categoria que deseja cadastrar\n")
                    cat.category_register(category)
                elif decide == 2:
                    category = input("Digite a categoria que deseja remover\n")
                    cat.category_remove(category)
                elif decide == 3:
                    category = input("DIgite a categoria que deseja alterar\n")
                    category_new = input("Digite a categoria para qual deseja alterar\n")
                    cat.category_change(category, category_new)
                elif decide == 4:
                    cat.category_show()
                else:
                    break

        elif place == 2:
            stk = Controller.ControllerStock()
            while True:
                decide = int(input("Digite 1 para cadastrar um produto\n"
                                    "Digite 2 para remover um produto\n"
                                    "Digite 3 para alterar um produto\n"
                                    "Digite 4 para mostar estoque\n"
                                    "Digite 5 para sair\n"))

