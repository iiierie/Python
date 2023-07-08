#import modules
import pandas as pd
import datetime as dt
import random
import smtplib

#open database and create a custom dictionary of data
#birthday_dict format should be {(dd,mm): full data}
df = pd.read_csv("birthdays.csv")
birthdays_dict = {(row_data.month, row_data.day): row_data for (index, row_data) in df.iterrows()}


today_tuple = (dt.datetime.now().month, dt.datetime.now().day)

#credentials
myEmail = "iire0604@gmail.com"
myPassword = "ndwtborlshxxosyt"
toEmail = birthdays_dict[today_tuple]["email"]


#check if birthday exists in dictionary
if today_tuple in birthdays_dict:
    letter_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter_path, "r+") as letter:
        name_to_replace = birthdays_dict[today_tuple]["name"]
        message_content = letter.read()
        Subject = f"Subject: Happy Birthday {name_to_replace}\n\n"
        message_content = Subject + message_content.replace("[NAME]", name_to_replace)
        print(message_content)

    with smtplib.SMTP("smtp.gmail.com") as emailSender:
        try:
            emailSender.starttls()
            emailSender.login(user = myEmail, password=myPassword)
            emailSender.sendmail(to_addrs= toEmail,from_addr= myEmail, msg = message_content )
        except Exception as e:
            print(e)
        else:
            print("E-mail Sent! ")




