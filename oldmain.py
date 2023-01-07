import smtplib
import smtplib
import datetime as dt

my_email = ""
password = ""
target_email = ""
#message = "Hello"

# connection = smtplib.SMTP("smtp.gmail.com",587)
# connection.starttls() #makes connections ecure through encryption
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email, 
#     to_addrs=target_email, 
#     msg="Subject: Hello Freiby\n\n This is the body of the email")
# connection.close()

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user = my_email, password = password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="soyellokito768@gmail.com",
        msg = "Subject: Hello Loki \n\n This is the body of the email"
    )
    
