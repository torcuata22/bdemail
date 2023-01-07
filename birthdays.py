
import pandas as pd 
import datetime as dt
import random
import smtplib

MY_EMAIL = "pr0b4nd0xxy@gmail.com"
PASSWORD = ""



#read date from here (birthday) and compare with now, need data["month"] and data["day"] from data set

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


today = dt.datetime.now()
today_month = today.month
today_day = today.day
today_tuple = (today_month,today_day)

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        content = contents.replace("[NAME]",birthday_person["name"]  )



    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password = PASSWORD)
        connection.sendmail(
            from_addr= MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg = f"Subject: Happy birthday! \n\n {content}"
        )

