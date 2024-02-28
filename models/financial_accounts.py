import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Financial_accounts(db.Model):
    __tablename__ = "Financial_accounts"

    account_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Users.user_id"), nullable=False)
    account_name = db.Column(db.String(), unique=True, nullable=False)
    account_type = db.Column(db.String(), nullable=False)
    current_balance = db.Column(db.Float(), nullable=False)
    available_balance = db.Column(db.Float(), nullable=False)

    def __init__(self, user_id, account_name, account_type, current_balance, available_balance):
        self.user_id = user_id
        self.account_name = account_name
        self.account_type = account_type
        self.current_balance = current_balance
        self.available_balance = available_balance

    def get_new_financial_account(user_id):
        return Financial_accounts(user_id, "", "", 0.00, 0.00)
    

class Financial_accountsSchema(ma.Schema):
    class Meta:
        fields = ['account_id', 'user_id', 'account_name', 'account_type', 'current_balance', 'available_balance']
    
financial_account_schema = Financial_accountsSchema
financial_accounts_schema = Financial_accountsSchema(many=True)


