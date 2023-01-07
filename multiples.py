import smtplib
import datetime as dt
import random



my_email = "pr0b4nd0xxy@gmail.com" #from_email
password = ""
 #["soyellokito768@gmail.com", "imthefreiby@google.com"]



now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    # with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    #     connection.starttls()
    #     connection.login(user = my_email, password = password)
    #     connection.sendmail(
    #     from_addr=my_email,
    #     to_addrs="imthefreiby@gmail.com",
    #     msg = f"Subject: Monday Motivation \n\n{quote}"
    # )

    for email in email_list:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user = my_email, password = password)
            connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg = f"Subject: Monday Motivation \n\n{quote}"
        )


