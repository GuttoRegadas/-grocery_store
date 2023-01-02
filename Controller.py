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
a = ControllerCategory()
a.category_show()