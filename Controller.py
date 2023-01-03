from Models import *
from DAO import DaoCategory, DaoSale, DaoStock, DaoPeople, DaoProvider, DaoEmployee
from datetime import datetime

class ControllerCategory:
    def category_register(self, new_category):
        existe = False
        x = DaoCategory.read()
        for i in x:
            if i.category == new_category:
                existe = True

        if not existe:
            DaoCategory.save(new_category)
            print('Categoria cadastrada com sucesso!')
        else:
            print('A categoria que deseja cadastrar já existe!')


    def category_remove(self, remove_category):
        x = DaoCategory.read()
        categ = list(filter(lambda x: x.category == remove_category, x))

        if len(categ) <= 0:
            print('A categoria que deseja remover não existe!')
        else:
            for i in range(len(x)):
                if x[i]. category == remove_category:
                    del x[i]
                    break
            print('Categoria removida com sucesso!')
        #TODO: COLOCAR SEM CATEGORIA NO ESTOQUE
            with open('category.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.category)
                    arq.writelines('\n')


    def category_change(self, change_category, category_altered):
        x = DaoCategory.read()

        categ = list(filter(lambda x: x.category == change_category, x))

        if len(categ) > 0:
            categ01 = list(filter(lambda x: x.category == category_altered, x))
            if len(categ01) == 0:
                x = list(map(lambda x: Category(category_altered) if(x.category == change_category) else(x), x))
                print("A alteração foi concluida com sucesso!")
                # TODO: ALTERAR A CATEGORIA TAMBEM NO ESTOQUE
            else:
                print("A categoria para qual deseja alterar já existe")
        else:
            print("A categoria que deseja alterar não existe")

        with open('category.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.category)
                arq.writelines('\n')

    def category_show(self):
        categorys = DaoCategory.read()
        if len(categorys) == 0:
            print("Categoria vazia!")
        else:
            for i in categorys:
                print(f'Category: {i.category}')


class ControllerStock:
    def products_register(self, name, price, category, amount):
        x = DaoStock.read()
        y = DaoCategory.read()
        h = list(filter(lambda x: x.category == category, y))
        stk = list(filter(lambda  x: x.product.name == name, x))

        if len(h) > 0:
            if len(stk) == 0:
                product = Products(name, price, category)
                DaoStock.save(product, amount)
                print("Produto cadastrado com sucesso!")
            else:
                print("Produto já existe em estoque")
        else:
            print("Produto inexistente!")


    def product_remove(self, name):
        x = DaoStock.read()
        stk = list(filter(lambda x: x.products.name == name, x))
        if len(stk) > 0:
            for i in range(len(x)):
                if x[i].products.name == name:
                    del x[i]
                    break
            print("Produto foi removio com sucesso!")
        else:
            print("O produto de deseja remover não existe!")

        with open('stock.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.products.name + "|" + i.products.price + "|" +
                               i.products.category + "|" + str(i.amount))
                arq.writelines('\n')


    def product_change(self, change_name, name_new, prive_new, category_new, amount_new):
        x = DaoStock.read()
        y = DaoCategory.read()
        h = list(filter(lambda x: x.category == category_new, y))
        if len(h) > 0:
            stk = list(filter(lambda x: x.products.name == change_name, x))
            if len(stk) > 0:
                stk = list(filter(lambda x: x.products.name == name_new, x))
                if len(stk) == 0:
                    x = list(map(lambda x: Stock(Products(name_new, prive_new, category_new), amount_new) if(x.products.neme == change_name) else(x), x))
                    print("Produto alterado com sucesso!")
            else:
                print("O produto que deseja alterar não existe!")

            with open('stock.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.products.name + "|" + i.products.price + "|" +
                                   i.products.category + "|" + str(i.amount))
                    arq.writelines('\n')

        else:
            print("Categoria informada não existe!")
a = ControllerStock()
a.product_change('banana', 'Maca', 'Verduras', '20')