from datetime import datetime


class Category:
    def __init__(self, category):
        self.category = category

class Products:
    def __init__(self, name, price, category):
        self.prducts = name
        self.prducts = price
        self.prducts = category


class sStock:
    def __init__(self, products: Products, amount):
        self.products = products
        self.amount = amount


class Sale:
    def __init__(self, unit_sold: Products, seller, buyer, sold_amount, date = datetime.now()):
        self.unit_sold = unit_sold
        self.seller = seller
        self.buyer = buyer
        self.sold_amount = sold_amount
        self.date = date


class Provider:
    def __init__(self, name, cnpj, phone, category):
        self.name = name
        self.cnpj = cnpj
        self.phone = phone
        self.category = category


class People:
    def __init__(self, name, phone, cpf, email, address ):
        self.name = name
        self.phone = phone
        self.cpf = cpf
        self.email = email
        self.address = address


class Employee(People):
    def __init__(self, name, phone, cpf, email, address, clt):
        self.clt = clt
        super().__init__(name, phone, cpf, email, address)