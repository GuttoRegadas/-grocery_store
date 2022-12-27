from Models import *#Category, Products, Stock, Sale, Provider, People, Employee


class DaoCategory:
    @classmethod
    def save(cls, category):
        with open('category.txt', 'a') as arp:
            arp.writelines(category)
            arp.writelines('\n')


    @classmethod
    def read(cls):
        with open('category.txt', 'r') as arq:
            cls.category = arq.readlines()

        cls.category = list(map(lambda x: x.replace('\n', ''), cls.category))

        cat = []
        for i in cls.category:
            cat.append(Category(i))

        return cat


class DaoSale:
        @classmethod
        def save(cls, sale: Sale):
            with open('sale.txt', 'a') as arp:
                arp.writelines(sale.unit_sold.name + '|' + 
                sale.unit_sold.price + '|' + 
                sale.unit_sold.category + '|' + 
                sale.seller + '|' + sale.buyer + '|' + 
                str(sale.sold_amount) + '|' + 
                sale.date.strftime("%d/%m/%Y"))
                arp.writelines('\n')

        @classmethod
        def read(cls):
            with open('sale.txt', 'r') as arq:
                cls.sale = arq.readlines()

            cls.sale = list(map(lambda x: x.replace('\n', ''), cls.sale))
            cls.sale = list(map(lambda x: x.split('|'), cls.sale))
            print(cls.sale)


            sal = []
            for i in cls.sale:
                sal.append(Sale(i))

            return sal

x = Products('Banana' , '5', 'Frutas')
y = Sale(x, 'gutto', 'josy', '3')

DaoSale.save(y)
DaoSale.read()