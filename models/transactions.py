import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Transactions(db.Model):
    __tablename__ = "Transactions"

    transaction_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Users.user_id"), nullable=False)
    account_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Financial_accounts.account_id"), nullable=False)
    category_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Categories.category_id"), nullable=False)
    amount = db.Column(db.Float(), nullable=False)
    date = db.Column(db.String()) #not sure what the best way to get the date here is
    note = db.Column(db.String())
    merchant = db.Column(db.String())


    def __init__(self, user_id, account_id, category_id, amount, date, note, merchant):
        self.user_id = user_id
        self.account_id = account_id
        self.category_id = category_id
        self.amount = amount
        self.date = date
        self.note = note
        self. merchant = merchant


    def get_new_transaction(user_id, account_id, category_id):
        return Transactions(user_id, account_id, category_id, 0.00, "", "", "")
    

class TransactionsSchema(ma.Schema):
    class Meta:
        fields = ['transaction_id', 'user_id', 'account_id', 'category_id', 'amount', 'date', 'note', 'merchant']


transaction_schema = TransactionsSchema()
transactions_schema = TransactionsSchema(many=True)

