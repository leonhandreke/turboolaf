#!/usr/bin/env bash

# mail the total amount of all QIF files in the qif/ directory
# to the given email address

# add a greeting
email_string="Hello Sir,\n\n"

# list all the individual prices of the evening
for qif in `find qif/*.qif`
do
	email_string="$email_string$qif: $(grep "^T" $qif)\n"
done

email_string="$email_string\n"

# construct a sum of all the invoices
calculation="0"
for i in `grep -h "^T" qif/*.qif`
do
	calculation="$calculation + $(echo $i | cut -c 2- -)"
done

# calculate the sum
sum=`echo $calculation | bc`
# append the sum to the email
email_string=$email_string"Total amount:	"$sum

email_string=$email_string"\n\nCheers!\nTurboOlaf\n"

# seek confirmation to send the email
echo -e $email_string
echo "Send this message to $1 now?"
read

echo -e $email_string | mail -s "TurboOlaf sales report generated $(date +"%A, %d.%m.%Y")" $1
