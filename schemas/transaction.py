from peewee import *

from schemas.card import Card

db = SqliteDatabase('./db/db_oltp.db', timeout=10)


class Transaction(Model):
    card_id = ForeignKeyField(Card, backref='transactions')
    amount = FloatField()
    timestamp = TimestampField()
    appr_status = BooleanField()

    class Meta:
        database = db
