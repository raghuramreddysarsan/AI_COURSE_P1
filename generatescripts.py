import csv
import random as rd
from datetime import datetime,timedelta

NUM_DAYS = 30
rows = []
for i in range(NUM_DAYS):
    insta_min = rd.randint(50,100)
    youtube_mins = rd.randint(12,14)
    whatsapp_mins = rd.randint(3,5)
    facebook_mins = rd.randint(4,6)
    linkedin_mins = rd.randint(1,3)
    reels_watch = rd.randint(20,55)
    rows.append([insta_min,youtube_mins,whatsapp_mins,facebook_mins,linkedin_mins,reels_watch])


with open(
    "digital_behavior.csv",
    "w",
    newline='',
    encoding = "utf-8"
)as f:
    writer = csv.writer(f)
    writer.writerow(["Instagram Minutes","Youtube Minutes","Whatsapp Minutes","Facebook Minutes","Linkedin Minutes","Reels Watch"])
    writer.writerows(rows)
    print("Data generated successfully and saved to CSV file.")