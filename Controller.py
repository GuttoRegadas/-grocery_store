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


    def remove_category(self, category_remove):
        x = DaoCategory.read()
        categ = list(filter(lambda x: x.category == category_remove, x))

        if len(categ) <= 0:
            print('A categoria que deseja remover não existe!')
        else:
            for i in range(len(x)):
                if x[i]. category == category_remove:
                    del x[i]
                    break
            print('Categoria removida com sucesso!')

            with open('category.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.category)
                    arq.writelines('\n')

