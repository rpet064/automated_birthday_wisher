#! Python 3
# birthday_wisher.py
# This programme checks a list of birthdays everyday. If It's someone's birthday
# it chooses a birthday template and sends it to the recipient

import smtplib
import datetime as dt
from random import randint
import pandas
PLACEHOLDER = "[NAME]"
SUBJECT = "Happy Birthday!"
my_email = "pencilcasetester@gmail.com"
my_password = "xGE81tW3b#$azA"
recipient_email = ""

# check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
months = now.month
days = now.day
data = pandas.read_csv("birthdays.csv")
birthday_dict = data.to_dict(orient="records")

for i in range(len(birthday_dict)):
    if birthday_dict[i]["day"] == days and birthday_dict[i]["month"] == months:
        name = birthday_dict[i]["name"]
        recipient_email = birthday_dict[i]["email"]
        # pick a random letter from letter templates replace [NAME]
        with open(f"letter_templates/letter_{randint(1,3)}.txt") as letter_file:
            letter_contents = letter_file.read()
            stripped_name = name.strip()
            new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # send the letter generated to email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=recipient_email,
                                msg=f"Subject:{SUBJECT}\n\n{new_letter}"
                                )
