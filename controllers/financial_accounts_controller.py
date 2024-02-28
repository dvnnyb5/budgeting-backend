from flask import jsonify, Request

from db import db
from models.financial_accounts import Financial_accounts, financial_account_schema, financial_accounts_schema
from util.reflection import populate_object


def financial_account_add(req: Request):