import csv
APP = "Instagram"
minutes = []
with open("digital_behaviour.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in list(reader):
            minutes.append((row['Instagram Minutes']))
            minutes = minutes[:7]
            avg = sum(map(int,minutes))/len(minutes)
            mini = min(map(int,minutes))
            maxi = max(map(int,minutes))
            cnt = 0
            for i in minutes:
                 if int(i)>avg:
                      cnt+=1
            print(f'Usage last 7 days :(minutes)\nAverage :(avg)\nMaximum Value:(maxi)\nMinimum Value:(mini)\nCount greater than Average:(cnt)')



