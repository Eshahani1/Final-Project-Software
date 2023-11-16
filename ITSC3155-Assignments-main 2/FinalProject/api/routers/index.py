from . import orders, order_details, guests, payments, promos, recipes, resources


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(guests.router)
    app.include_router(payments.router)
    app.include_router(promos.router)
    app.include_router(recipes.router)
    app.include_router(resources.router)

