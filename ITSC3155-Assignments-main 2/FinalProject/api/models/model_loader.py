from . import (orders, order_details, recipes, resources, guests, promos, menu_items, promo_details)

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    guests.Base.metadata.create_all(engine)
    promos.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    promo_details.Base.metadata.create_all(engine)

