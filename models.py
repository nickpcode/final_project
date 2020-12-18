from peewee import *
import datetime
# from flask_login import UserMixin

DATABASE = PostgresqlDatabase('clothes')

# class Users(UserMixin, Model):
#     username = CharField(unique=True)
#     password = CharField()

#     class Meta:
#         database = DATABASE

class Shirt(Model):
    color = CharField()
    fabric = CharField()
    brand = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class Jacket(Model):
    color = CharField()
    fabric = CharField()
    brand = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class Pant(Model):
    color = CharField()
    fabric = CharField()
    brand = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class Shoe(Model):
    color = CharField()
    fabric = CharField()
    brand = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Shirt, Jacket, Pant, Shoe], safe=True)
    print("TABLES Created")
    DATABASE.close()