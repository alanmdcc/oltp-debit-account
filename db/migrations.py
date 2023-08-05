import os
import time

from peewee import SqliteDatabase

from schemas.account import Account
from schemas.card import Card
from schemas.transaction import Transaction
from schemas.user import User


def create_db(path: str):
    if not os.path.isfile(path):
        db = SqliteDatabase(path)
        time.sleep(1)
        db.create_tables([User, Account, Card, Transaction])
        return True