from decimal import Decimal
import time

def invoice_as_printable_string(invoice, width=60):
    """
    Render the given invoice as a string ready to print on a receipt.
    Dependencies are not resolved and should already have been resolved by the caller.
    """
    invoice_string = ""
    invoice_string += "*" * width + "\n"
    invoice_string += "K1 Getränkeverkauf".center(width) + "\n"
    invoice_string += time.strftime("%d %b %Y %H:%M:%S").center(width) + "\n"
    invoice_string += ("ID: " + invoice['id']).center(width) + "\n"
    invoice_string += "*" * width + "\n\n"

    for product in invoice['items']:
        price = Decimal(str(product.get('price', 0)))
        # only print products that actually cost money
        if product["quantity"] != 0 and price != 0:
            billed_price = price * Decimal(str(product["quantity"]))
            billing_string = str(price).rjust(5) + \
                    str(" x " + str(product["quantity"])).rjust(6) + \
                    " = " + \
                    str(billed_price).rjust(6)

            name_string = product["name"].ljust(width - len(billing_string))
            invoice_string += name_string + billing_string + "\n"

    invoice_string += "-" * width + "\n"
    invoice_string += "Total:" + str(invoice.get_total_price()).rjust(width - 6) + "\n"

    return invoice_string

def product_list_as_string(product_list):
    """
    Render a string with a list containing the quantity and name of the products in the list
    """
    entered_items_string = ""
    for product in product_list:
        if product["quantity"] != 0:
            entered_items_string += str(product["quantity"]).rjust(4) + " x " + product["name"] + "\n"
    return entered_items_string

def invoice_as_qif(invoice):
    """
    Render the invoice as a QIF file.
    """
    qif = "!Type:Cash\n"
    qif += "T" + str(invoice.get_total_price()) + "\n"
    qif += "D" + time.strftime("%d/%m/%y") + "\n"
    qif += "MBierminister Verkauf\n"
    qif += "^"
    return qif