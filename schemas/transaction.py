from peewee import *

from schemas.account import Account
from schemas.card import Card

db = SqliteDatabase('./db/db_oltp.db', timeout=10)


class Transaction(Model):
    account_id = ForeignKeyField(Account, backref='transactions')
    card_id = ForeignKeyField(Card, backref='transactions')
    amount = FloatField()
    timestamp = TimestampField()
    appr_status = BooleanField()

    class Meta:
        database = db