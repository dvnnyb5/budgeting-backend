import routes

def register_blueprints(app):
    app.register_blueprint(routes.financial_accounts)
    app.register_blueprint(routes.transactions)
    app.register_blueprint(routes.categories)
    app.register_blueprint(routes.rules)
    app.register_blueprint(routes.users)
    app.register_blueprint(routes.auth)
