import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = client["mydatabase"]#create databse mydatabase
mycol = mydb["customers"]
#MongoDB waits until you have inserted a document before it actually creates the collection.

mydict = { 
    "name": "John", 
    "address": "Highway 37" 
}

x = mycol.insert_one(mydict)

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)

if x.acknowledged:
    for objectids in x.inserted_ids:
        print(objectids)

x = mycol.find_one()

print(x)

#findAll
for x in mycol.find():
    print(x)

'''
MongoDB waits until you have created a collection (table),
with at least one document (record) before it actually
creates the database (and collection).
'''

print(client.list_database_names())#see databases name

'''
In MongoDB we use the find and findOne methods to find data in a collection.

Just like the SELECT statement is used to find data in a table in a MySQL database.

'''
