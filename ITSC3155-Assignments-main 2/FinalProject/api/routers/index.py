from . import (orders, order_details, guests, promos,
               recipes, resources, menu_items, promo_details)


def load_routes(app):
    app.include_router(promos.router)
    app.include_router(promo_details.router)
    app.include_router(guests.router)
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(menu_items.router)
    app.include_router(recipes.router)
    app.include_router(resources.router)

