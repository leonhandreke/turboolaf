#!/usr/bin/env python3

import json

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
        try:
            invoice[product_code]["quantity"] += 1
        except:
            print("No such product!")

print(invoice)
print("bye!")
