import json
record={'name':'John','Favourite number':0}
records=[]
file='Records.json'


def greetUser():
    print("I keep track of Users Favourite number")
    print("let me see if I have record of yours")
    name=input("Enter your name\n")
    return name
def checkingRecords(name,records):
    if not records:
        found=False
    else:
        for record in records:
            found=str(name) == str(record['name'])
            if found:
                return record
def OnRecordFound(record):
    print(f"oh hello {record['name']},your favourite number is {record['Favourite number']}")
def OnrecordNotFounnd(name):
    print(f"we have no record for {name}")
    print("let's store your Favourite number")
    number = int(input("Enter your Favourite number\n"))
    return number
def storeData(name, number,records):
    record['name']=name
    record['Favourite number']=number
    records.append(record)
def fileDump(records):    
    with open(file,'w') as database:
        json.dump(records,database)
def fileLoad(file):
    with open(file) as database:
        records=json.load(database)
    return records
def Main(Username,data):
    User=checkingRecords(Username,data)
    if User:
        OnRecordFound(User)
    else:
        num=OnrecordNotFounnd(Username)
        storeData(Username,num,data)
        fileDump(data)


Username=greetUser()
try:
    data=fileLoad(file)
    
except FileNotFoundError:
    data=[]
       
Main(Username,data)