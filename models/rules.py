import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Rules(db.Model):
    __tablename__ = "Rules"

    rule_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Users.user_id", ondelete="CASCADE"), nullable=False)
    rule_name = db.Column(db.String(), nullable=False)
    merchant_name = db.Column(db.String(), nullable=False)
    merchant_name_type = db.Column(db.String(), nullable=False) #don't remember what this is for
    amount = db.Column(db.Float(), nullable=False)
    amount_type = db.Column(db.String(), nullable=False)


    def __init__(self, user_id, rule_name, merchant_name, merchant_name_type, amount, amount_type):
        self.user_id = user_id
        self.rule_name = rule_name
        self.merchant_name = merchant_name
        self.merchant_name_type = merchant_name_type
        self.amount = amount
        self.amount_type = amount_type

    def get_new_rule(user_id):
        return Rules(user_id , "", "", "", 0.00, "")
    

class RulesSchema(ma.Schema):
    class Meta:
        fields = ['rule_id', 'user_id', 'rule_name', 'merchant_name', 'merchant_name_type', 'amount', 'amount_type']


rule_schema = RulesSchema()
rules_schema = RulesSchema(many=True)

