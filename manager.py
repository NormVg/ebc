from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Vishnu:gameisworld4me@thenormvg.c66lnwg.mongodb.net/?retryWrites=true&w=majority&appName=TheNormVg"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

dbs = client.list_database_names()
db = client['electric_bill_calculator']['bill_calculator']


def update_table(seq:int,date:str,mm:int,motor:int,slave:int,bill:int,ground:int,first:int):
    a = {
        "seq":seq,
        "date" : date,
        "main-meter" : mm,
        "motor" : motor,
        "slave" : slave,
        "bill-rs" : bill,
        "bill-ground" : ground,
        "bill-first" : first,
    }
    
    db.insert_one(a)


def all_data():
    a =  db.find({})
    b = []
    for i in a:
        b.insert(i['seq'],i)
        
    b.reverse()
    
    return b

def cal(mm:int,motor:int,slave:int,bill:int):
    a = all_data()
    a.reverse()
    b = len(a)
    c = a[b-1]

    mm = int(mm) - int(c['main-meter'])
    motor = int(motor) - int(c['motor'])
    slave = int(slave) - int(c['slave'])

    each_motor = motor/2

    one = (mm - slave) - each_motor
    two = slave - each_motor
    ground = int((one/mm)*bill)
    first = int((two/mm)*bill)
    
    return b,ground,first

def nowdate():
    d = datetime.now()
    return f"{d.day}/{d.month}/{d.year}"


#cal(18954,2220,4656,4000)