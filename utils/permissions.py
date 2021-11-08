
from utils import default

owners = default.config()["owners"]


def is_owner(ctx):
    """ Checks if the author is one of the owners """
    return ctx.author.id in owners
