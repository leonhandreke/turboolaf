#!/usr/bin/env python3

import json
import time
from decimal import Decimal
import uuid

INVOICE_WIDTH = 40

print("Welcome to TurboOlaf!")

invoice = json.load(open("invoice.json"))
# set the quantity of all products to 0
print(invoice)
for code, product in invoice.items():
    product["quantity"] = 0

while True:
    product_code = input("Product code:")

    # end if an empty product code was given
    if not product_code:
        break
    else:
        if product_code[0] == '$':
            special_id = str(uuid.uuid4())
            invoice.update({
                special_id: {}
                })
            invoice[special_id]['quantity'] = 1
            try:
                special_name = product_code[1:].split(' ')[1]
            except IndexError:
                special_name = "Sonderposten"
            invoice[special_id]['name'] = special_name
            invoice[special_id]['price'] = product_code[1:].split(' ')[0]
        else:
            try:
                invoice[product_code]["quantity"] += 1
            except:
                print("No such product!")

invoice_string = ""
invoice_string += "*" * INVOICE_WIDTH + "\n"
invoice_string +="K1 Getränkeverkauf".center(INVOICE_WIDTH) + "\n"
invoice_string += time.strftime("%d %b %Y %H:%M:%S").center(INVOICE_WIDTH) + "\n"
invoice_string += "*" * INVOICE_WIDTH + "\n\n"

# use decimal to guarantee total accuracy
total_price = Decimal(0)
for code, product in invoice.items():
    if product["quantity"] > 0:
        billed_price = Decimal(str(product["price"])) * Decimal(str(product["quantity"]))
        total_price += billed_price

        billing_string = str(product["price"]).rjust(5) + \
                str(" x " + str(product["quantity"])).rjust(6) + \
                " = " + \
                str(billed_price).rjust(6)

        name_string = product["name"].ljust(INVOICE_WIDTH - len(billing_string))
        invoice_string += name_string + billing_string + "\n"

invoice_string += "-" * INVOICE_WIDTH + "\n"
invoice_string += "Total:" + str(total_price).rjust(INVOICE_WIDTH - 6) + "\n"

print(invoice_string);

