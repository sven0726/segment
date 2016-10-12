# encoding=utf-8
import csv
import random

def dim(day):
    dimData = {}
    randomData = random.sample(range(-1000000,1000000), 288)
    with open("08.csv","r") as data_08_csv:
        reader = csv.reader(data_08_csv, delimiter=",")
        index = 0
        for line in reader:
            line[0] = line[0].replace("2016-09-08","2016-09-{}".format(day))
            line[1] = long(line[1]) + randomData[index]
            dimData[line[0]] = line[1]
            index += 1
    return dimData

def gen(days):
    with open("1380603831-5min-09-bandwidth.csv","r") as source_csv, open("1380603831-5min-09-bandwidth_fix.csv","w") as result_csv:
        reader = csv.reader(source_csv, delimiter=",")
        writer = csv.writer(result_csv, delimiter=",")
        mapRs = {}
        counts = {}
        for day in days:
            mapRs[day] = dim(day)
        for line in reader:
            _day = line[0][8:10]
            if _day in days:
                dayKey = line[0]
                line[1] = mapRs[_day][dayKey]
                counts[_day] =  counts[_day] + 1 if counts.has_key(_day) else 1
            writer.writerow(line)
        print counts
gen(["09","10","11","12","13"])

