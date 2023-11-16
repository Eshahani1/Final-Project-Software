from . import guests, menu, order_details, orders, payments, promos, recipes, resources

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    guests.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
    payments.Base.metadata.create_all(engine)
    promos.Base.metadata.create_all(engine)
