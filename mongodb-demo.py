import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb["customers"]
'''
mydict = { "name": "Tony", "address": "Bangalore 37" }

x = mycol.insert_one(mydict)

print(x.inserted_id)
'''
#----------inserting many values
'''
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

#print list of the _id values of the inserted documents:
print(x.inserted_ids)
'''
#-------inserting many values with id
'''
mylist = [
    { "_id": 1, "name": "John", "address": "Highway 37"},
    { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    { "_id": 3, "name": "Amy", "address": "Apple st 652"},
    { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
    { "_id": 5, "name": "Michael", "address": "Valley 345"},
    { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
    { "_id": 8, "name": "Richard", "address": "Sky st 331"},
    { "_id": 9, "name": "Susan", "address": "One way 98"},
    { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
    { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
    { "_id": 12, "name": "William", "address": "Central st 954"},
    { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
    { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)
'''
#print list of the _id values of the inserted documents:
#print(mycol.find_one())

#for x in mycol.find():
#for x in mycol.find({},{ "_id":1,"name": 1, "address": 1 }):

#Find document(s) with the address "Park Lane 38":
#myquery = { "address": "Park Lane 38" }
#Find documents where the address starts with the letter "S" or higher:
#myquery = { "address": { "$gt": "S" } }
#Find documents where the address starts with the letter "S":
#myquery = { "address": { "$regex": "^S" } }
#mydoc = mycol.find(myquery)

#Sort the result alphabetically by name:
#mydoc = mycol.find().sort("name")
#Sort the result reverse alphabetically by name:
mydoc = mycol.find().sort("name",-1)
for x in mydoc:
    print(x)