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
        stk = list(filter(lambda  x: x.products.name == name, x))

        if len(h) > 0:
            if len(stk) == 0:
                products = Products(name, price, category)
                DaoStock.save(products, amount)
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


    def product_change(self, change_name, name_new, price_new, category_new, amount_new):
        x = DaoStock.read()
        y = DaoCategory.read()
        h = list(filter(lambda x: x.category == category_new, y))
        if len(h) > 0:
            stk = list(filter(lambda x: x.products.name == change_name, x))
            if len(stk) > 0:
                stk = list(filter(lambda x: x.products.name == name_new, x))
                if len(stk) == 0:
                    x = list(map(lambda x: Stock(Products(name_new, price_new, category_new), amount_new) if(x.products.name == change_name) else(x), x))
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


    def stock_show(self):
        stk = DaoStock.read()
        if len(stk) == 0:
            print("Estoque vazio")
        else:
            print("==========Produto==========")
            for i in stk:
                print(f"Nome: {i.products.name}\n"
                      f"Preço: {i.products.price}\n"
                      f"Categoria: {i.products.category}\n"
                      f"Quantidade: {i.amount}")
                print("----------------------------")

class ControllerSale:
    def sale_register(self, products_name, seller, buyer, amout_sold):
        x = DaoStock.read()
        temp = []
        exist = False
        amount = False

        for i in x:
            if exist == False:
                if i.products.name == products_name:
                    exist = True
                    if i.amount >= amout_sold:
                        amount = True
                        i.amount = int(i.amount) - int(amout_sold)

                        sold = Sale(Products(i.products.name, i.products.price, i.products.category), seller, buyer, amout_sold)

                        purchased_value = int(amout_sold) * int(i.products.price)

                        DaoSale.save(sold)

            temp.append([Products(i.products.name, i.products.price, i.products.category), i.amount])

        arq = open('stock.txt', 'w')
        arq.write("")

        for i in temp:
            with open('stock.txt', 'a') as arq:
                arq.writelines(i[0].name + "|" + i[0].price + "|" + i[0].category + "|" + str(i[1]))
                arq.writelines('\n')

        if exist == False:
            print("O produto não existe!")
            return None
        elif not amount:
            print("A quantidade não contem em estoque!")
            return None
        else:
            print("Venda realizada com sucesso!")
            return purchased_value


    def products_report(self,):
        sale = DaoSale.read()
        products = []
        for i in sale:
            name = i.unit_sold.name
            amount = i.sold_amount
            size = list(filter(lambda x: x['products'] == name, products))
            if len(size) > 0:
                products = list(map(lambda x: {'products': name, 'amount': int(x['amount']) + int(amount)}
                if(x['products'] == name) else(x), products))
            else:
                products.append({'products': name, 'amount': int(amount)})

        oder = sorted(products, key=lambda k: k['amount'], reverse=True)

        print("Esses são os produtos mais vendidos")
        a = 1
        for i in oder:
            print(f"========== Produto [{a}] ==========")
            print(f"Produto: {i['products']} \n"
                  f"Quantidade: {i['amount']}"
                  )
            a += 1

    def sale_show(self,start_date, and_date):
        sale = DaoSale.read()
        start_date01 = datetime.strptime(start_date, '%d/%m/%Y')
        and_date01 = datetime.strptime(and_date, '%d/%m/%Y')

        select_sale = list(filter(lambda x: datetime.strptime(x.date, '%d/%m/%Y') >= start_date01
                                  and datetime.strptime(x.date, '%d/%m/%Y') <= and_date01, sale))

        count = 1
        entire = 0

        for i in select_sale:
            print(f"========== Venda {count}==========")
            print(f"Produto: {i.unit_sold.name}\n"
                  f"Qauntidade: {i.sold_amount}\n"
                  f"Categoria: {i.unit_sold.category}\n"
                  f"Data: {i.date}\n"
                  f"Comprador: {i.buyer}\n"
                  f"Vendedor: {i.seller}\n"
                  f"--------------------\n")

            entire += int(i.unit_sold.price) * int(i.sold_amount)
            count += 1

        print(f"Toral vendido: {entire}")

