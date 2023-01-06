from Models import Category, Products, Stock, Sale, Provider, People, Employee


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
            arp.writelines(sale.unit_sold.name + '|' + sale.unit_sold.price + '|' + sale.unit_sold.category + '|' + sale.seller + '|' + sale.buyer + '|' + str(sale.sold_amount) + '|' + sale.date)
            arp.writelines('\n')

    @classmethod
    def read(cls):
        with open('sale.txt', 'r') as arq:
            cls.sale = arq.readlines()

        cls.sale = list(map(lambda x: x.replace('\n', ''), cls.sale))
        cls.sale = list(map(lambda x: x.split('|'), cls.sale))

        sal = []
        for i in cls.sale:
            sal.append(Sale(Products(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return sal

class DaoStock:
    @classmethod
    def save(cls, products: Products, amount):
        with open('stock.txt', 'a') as arq:
            arq.writelines(products.name + "|" + products.price + "|" +
                            products.category + "|" + str(amount))
            arq.writelines('\n')


    @classmethod
    def read(cls):
        with open('stock.txt', 'r') as arq:
            cls.stock = arq.readlines()

        cls.stock = list(map(lambda x: x.replace('\n', ''), cls.stock))
        cls.stock = list(map(lambda x: x.split('|'), cls.stock))
        sto = []
        if len(cls.stock) > 0:
            for i in cls.stock:
                sto.append(Stock(Products(i[0], i[1], i[2]), int(i[3])))

        return sto

class DaoProvider:
    @classmethod
    def save(cls, provider: Provider):
        with open('provider.txt', 'a') as arq:
            arq.writelines(provider.name + "|" + provider.cnpj + "|" +
                            provider.phone + "|" + provider.category)
            arq.writelines('\n')


    @classmethod
    def read(cls):
        with open('provider.txt', 'r') as arq:
            cls.provider = arq.readlines()

        cls.provider = list(map(lambda x: x.replace('\n', ''), cls.provider))
        cls.provider = list(map(lambda x: x.split('|'), cls.provider))

        prov = []
        for i in cls.provider:
            prov.append(Provider(i[0], i[1], i[2], i[3]))
        return prov


class DaoPeople:
    @classmethod
    def save(cls, people: People):
        with open('client.txt', 'a') as arq:
            arq.writelines(people.name + "|" + people.phone + "|" +
                            people.cpf + "|" + people.email + "|" + people.address)
            arq.writelines('\n')


    @classmethod
    def read(cls):
        with open('client.txt', 'r') as arq:
            cls.client = arq.readlines()

        cls.client = list(map(lambda x: x.replace('\n', ''), cls.client))
        cls.client = list(map(lambda x: x.split('|'), cls.client))

        client = []
        for i in cls.client:
            client.append(People(i[0], i[1], i[2], i[3], i[4]))
        return client


class DaoEmployee:
    @classmethod
    def save(cls, employee: Employee):
        with open('employee.txt', 'a') as arq:
            arq.writelines(employee.clt + "|" + employee.name + "|" + employee.phone + "|" +
                            employee.cpf + "|" + employee.email + "|" + employee.address)
            arq.writelines('\n')


    @classmethod
    def read(cls):
        with open('employee.txt', 'r') as arq:
            cls.employee = arq.readlines()

        cls.employee = list(map(lambda x: x.replace('\n', ''), cls.employee))
        cls.employee = list(map(lambda x: x.split('|'), cls.employee))

        employee = []
        for i in cls.employee:
            employee.append(Employee(i[0], i[1], i[2], i[3], i[4], i[5]))
        return employee