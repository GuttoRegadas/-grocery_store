from Models import *#Category, Products, Stock, Sale, Provider, People, Employee


class DaoCategory:
    @classmethod
    def save(cls, category):
        with open('category.txt', 'a') as arp:
            arp.writelines(category, '\n')


    @classmethod
    def read(cls):
        with open('category.txt', 'r') as arq:
            cls.category = arq.readlines()

        cls.category = list(map(lambda x: x.replace('\n', ''), cls.category))

        cat = []
        for i in cls.category:
            cat.append(Category(i))