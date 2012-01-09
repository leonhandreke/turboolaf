import time
from decimal import Decimal

def get_total_price(invoice):
    total_price = Decimal(0)
    for code, product in invoice.items():
        billed_price = Decimal(str(product["price"])) * Decimal(str(product["quantity"]))
        total_price += billed_price
    return total_price

def get_qif(invoice):
    qif = "!Type:Cash\n"
    qif += "T" + str(get_total_price(invoice)) + "\n"
    qif += "D" + time.strftime("%d") + "/" + time.strftime("%m") + "' " + time.strftime("%y") + "\n"
    qif += "MBierminister Verkauf\n"
    qif += "^"
    return qif
