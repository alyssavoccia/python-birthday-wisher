import smtplib
import datetime as dt
import random

MY_EMAIL = "email@gmail.com"
MY_PASSWORD = "password"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        quotes = [quote.strip() for quote in quotes]
        random_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="other_email@gmail.com",
            msg=f"Subject:Motivational Quote\n\n{random_quote}"
        )
