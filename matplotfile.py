import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import csv
import pandas as pd
df = pd.read_csv("digital_behaviour.csv")
df['Total_Screen_Time'] = (
    df['Instagram_Minutes'] + 
    df['YouTube_Minutes'] + 
    df['WhatsApp_Minutes'] + 
    df['LinkedIn_Minutes']
)
plt.figure(figsize = (40,16))
plt.bar(df['Date'],df['Total_Screen_Time'],color = "blue")
plt.xlabel("Date",fontsize = 12)
plt.ylabel("Total_Screen_Time(minutes)",fontsize = 12)
plt.title("My Screen Time by Day")
plt.savefig("digital_behaviour_plot.png",dpi = 300,bbox_inches='tight')
print("plot successful")

#2
apps = ['Instagram', 'YouTube', 'WhatsApp', 'LinkedIn']
total_minutes = [
    df['Instagram_Minutes'].sum(),
    df['YouTube_Minutes'].sum(),
    df['WhatsApp_Minutes'].sum(),
    df['LinkedIn_Minutes'].sum()
]
plt.figure(figsize=(8, 5))
plt.bar(apps, total_minutes, color=["#70676A", '#FF0000', "#385D70", "#D196DE"])
plt.xlabel("Social Media Apps", fontsize=12)
plt.ylabel("Total Minutes", fontsize=12)
plt.title("Total Time by App", fontsize=14)
plt.tight_layout()
plt.savefig("total_time_by_app.png")
print("Total time plot saved successfully!")

#3

plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Total_Screen_Time'], label='Total Screen Time', color='purple', marker='o', linewidth=2)
plt.plot(df['Date'], df['Study_Minutes'], label='Study Minutes', color='green', marker='s', linewidth=2)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Minutes", fontsize=12)
plt.title("Study Minutes vs. Total Screen Time per Day", fontsize=14)
plt.xticks(rotation=90, fontsize=9)
plt.legend(fontsize=11)
plt.tight_layout()
plt.savefig("study_vs_screentime_plot.png")
print("Line chart saved successfully!")

#4
plt.figure(figsize=(8, 6))
colors = ['#E1306C', '#FF0000', '#25D366', '#0A66C2']
plt.pie(
    total_minutes, 
    labels=apps, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140,
)
plt.title("Share of Total App Time by App", fontsize=14, pad=20)
plt.tight_layout()
plt.savefig("app_share_pie_chart.png")
print("Pie chart saved successfully!")
