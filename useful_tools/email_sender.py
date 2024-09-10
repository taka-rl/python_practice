import smtplib


MY_EMAIL = "your gmail address"
PASSWORD = "password"
TO_EMAIL = "to the destination email address"
MESSAGE = "Write a message here"


with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=TO_EMAIL,
        msg=MESSAGE)
