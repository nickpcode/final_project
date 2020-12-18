from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = PostgresqlDatabase('clothes')

class Users(UserMixin, Model):
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE

class Shirts(Model):
    color = CharField()
    fabric = CharField()
    brand = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class Jackets(Model):
    color = CharField()
    fabric = CharField()
    brand = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class Pants(Model):
    color = CharField()
    fabric = CharField()
    brand = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class Shoes(Model):
    color = CharField()
    fabric = CharField()
    brand = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Users, Shirts, Jackets, Pants, Shoes], safe=True)
    print("TABLES Created")
    DATABASE.close()