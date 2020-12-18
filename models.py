import os
from peewee import *
import datetime

from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ: # later we will manually add this env var 
                              # in heroku so we can write this code
  DATABASE = connect(os.environ.get('DATABASE_URL')) # heroku will add this 
                                                     # env var for you 
                                                     # when you provision the
                                                     # Heroku Postgres Add-on
else:
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
    image = CharField
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class Jacket(Model):
    color = CharField()
    fabric = CharField()
    brand = CharField()
    image = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class Pant(Model):
    color = CharField()
    fabric = CharField()
    brand = CharField()
    image = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class Shoe(Model):
    color = CharField()
    fabric = CharField()
    brand = CharField()
    image = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Shirt, Jacket, Pant, Shoe], safe=True)
    print("TABLES Created")
    DATABASE.close()