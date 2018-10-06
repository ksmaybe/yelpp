import json
import csv


def biz_id_collection(data):
    id=[]
    with open(data) as f:
        lines=f.readlines()
        if "Shack Shack" in lines[1]:
            id.append(lines[0])
    return id


def review_data(data,month):
    stars = []
    for i in data:
        date = i['date']
        mon = int(date[5] + date[6])
        if i['business_id'] in id and mon == month:
            stars.append(i['stars'])
    return sum(stars)/len(stars)

def main():
    data=[]
    with open('yelp_academic_dataset_business.json',encoding='utf8') as f:
        i=0
        for line in f:
            print(i)
            i+=1
            lines=json.loads(line)
            print(lines["name"])
    print(data)

main()
