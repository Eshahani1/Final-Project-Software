from . import orders, order_details, recipes, resources, guests, promos, payments, menu_items

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    guests.Base.metadata.create_all(engine)
    promos.Base.metadata.create_all(engine)
    payments.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)


