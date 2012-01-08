#!/usr/bin/env python3

import json

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
        try:
            invoice[product_code]["quantity"] += 1
        except:
            print("No such product!")

print("\n\n")
print("*" * INVOICE_WIDTH)
print("K1 Getränkeverkauf".center(INVOICE_WIDTH))
print("*" * INVOICE_WIDTH + "\n")

total_price = 0
for code, product in invoice.items():
    if product["quantity"] > 0:
        billed_price = product["price"] * product["quantity"]
        total_price += billed_price

        print(
                product["name"].ljust(15) +
                str(product["price"]).rjust(5) +
                str(" x " + str(product["quantity"])).rjust(6) +
                " = " +
                str(billed_price).rjust(6)
                )

print("-" * INVOICE_WIDTH)
print("Total:" + str(total_price).rjust(INVOICE_WIDTH - 6))
print("\n")

