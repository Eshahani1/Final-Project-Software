from . import orders, order_details, guests


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(guests.router)

