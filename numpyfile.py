import csv
import numpyfile as np
instaMinutes = []
studyMinutes = []
with open("digital_behavior.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in list(reader):
        instaminutes.append((row['Instagram Minutes']))
        studyminutes.append((row['Youtube Minutes']))
    instaminutes = instaminutes[:7]
    studyminutes = studyminutes[:7]
    instaArray = np.array(instaminutes)
    studyArray = np.array(studyminutes)
    total = instaArray.sum()
    avg = instaArray.mean()
    mini = instaArray.min()
    maxi = instaArray.max()
    instaArray[0]
    instaArray[-1]
    instaArray[0:3]
    instaArray[-2::]
    instaArray[1:4]
    #instaArray = [val/60 for val in instaArray]
    hours = instaArray/60
    diff = instaArray - studyArray
    greater_than_100 = instaArray > 100
    greater = instaArray[instaArray>100]
    count = (instaArray>100).sum()
    greater = instaArray[instaArray > avg]
    

    
