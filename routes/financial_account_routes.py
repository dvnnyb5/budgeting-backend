from flask import request, Blueprint

import controllers

financial_accounts = Blueprint('financial_accounts', __name__)


@financial_accounts.route('/financial_account', methods=['POST'])
def financial_account_add():
    return controllers.financial_account_add(request)