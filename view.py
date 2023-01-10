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
                if decide == 1:
                    product = input("Digite um produto que deseja cadastrar\n")
                    price = input("Digite o preço do produto\n")
                    category = input("Digite a categoria do produto\n")
                    amount = input("Digite a qunatidade\n")
                    stk.products_register(product, price, category, amount)
                elif decide == 2:
                    name = input("Digite um produto que deseja remover\n")
                    stk.product_remove(name)
                elif decide == 3:
                    change_name = input("Digite um produto que deseja alterar\n")
                    name_new = input("Digite o nome do produto\n")
                    price = input("Digite o preço do produto\n")
                    category = input("Digite a categoria do produto\n")
                    amount = input("Digite a qunatidade\n")
                    stk.product_change(change_name, name_new, price, category, amount)
                elif decide == 4:
                    stk.stock_show()
                else:
                    break

        elif place == 3:
            pvd = Controller.ControllerProvider()
            while True:
                decide = int(input("Digite 1 para cadastrar um fornecedor\n"
                                    "Digite 2 para remover um fornecedor\n"
                                    "Digite 3 para alterar um fornecedor\n"
                                    "Digite 4 para mostar fornecedores cadastrados\n"
                                    "Digite 5 para sair\n"))

                if decide == 1:
                    name = input("Digite o nome do fornecedor:\n")
                    cnpj = input("Digite o CNPJ do fornecedor:\n")
                    phone = input("Digite o telefone do fornecedor:\n")
                    category = input("Digite a categoria de produto do fornecedor:\n")
                    pvd.provider_register(name, cnpj, phone, category)
                elif decide == 2:
                    name = input("Digite o nome do fornecedor:\n")
                    pvd.provider_remove(name)
                elif decide == 3:
                    change_n = input("Digite o nome do fornecedor que deseja alterar:\n")
                    n_name = input("Digite o nome do fornecedor:\n")
                    n_cnpj = input("Digite o CNPJ do fornecedor:\n")
                    n_phone = input("Digite o telefone do fornecedor:\n")
                    n_category = input("Digite a categoria de produto do fornecedor:\n")
                    pvd.provider_change(change_n, n_name, n_cnpj, n_phone, n_category)
                elif decide == 4:
                    pvd.provider_show()
                else:
                    break
