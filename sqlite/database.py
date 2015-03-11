__author__ = 'Matt Borgman'

from peewee import *


db = SqliteDatabase('users.db')

class Customer(Model):
    name = CharField()
    email = CharField()
    password = CharField()

    class Meta:
        database = db


