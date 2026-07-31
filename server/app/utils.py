import ccy
from flask import request


def format_currency_filter(amount):
    currency_code = ccy.countryccy(request.accept_languages.best[-2:])
    return f"{currency_code} {amount}"
