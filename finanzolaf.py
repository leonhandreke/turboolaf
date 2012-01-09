#!/usr/bin/env python3

import json
import time
import datetime
import os

from decimal import Decimal
import uuid

def getfilelist():
   return os.listdir("./invoices")

def gettotalprice(f):  
   invoice = json.load(open("./invoices/" + f))

   total_price = Decimal(0)
   for code, product in invoice.items():
       if product["quantity"] > 0:
           billed_price = Decimal(str(product["price"])) * Decimal(str(product["quantity"]))
           total_price += billed_price
   
   return total_price

def main():
   filelist = getfilelist()

   for files in filelist:
       price = gettotalprice(files)

       qif = '''
       !Type:Cash
       '''
       qif += "T" + str(price) + "\n"
       qif += "D" + time.strftime("%d") + "/" + time.strftime("%m") + "' " + time.strftime("%y") + "\n"
       qif += "MBierminister Verkauf\n"
       qif += "^"

       qif_filename = files.split(".")

       qif_file = open("./GnuCash/" + qif_filename[0] + ".qif", 'w')
       qif_file.write(qif)
       qif_file.close()

       print (qif_filename[0] + ".qif written")

   #TODO: Move files to Archiv after the job is done

if __name__ == "__main__":
    main()
