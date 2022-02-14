import pymongo

# Establishing connection
my_client = pymongo.MongoClient('mongodb://localhost:27017/')

# Create a database, if database exists, connect to it
mydb = my_client['mydatabase']

# List all the databases
print(f'Existing databases: {my_client.list_database_names()}')

# Creating collection, or connecting to one
mycol = mydb['customers']

# List all collection names
print(f'Existing collections: {mydb.list_collection_names()}')

# Insert one document
mydict = {
    'name': 'John Wick',
    'nick_name': 'Babayaga',
    'intro': 'Once he killed a man with a fuuuuking pencil.'
}
x = mycol.insert_one(mydict)

# Check the document
print(f'Data inserted successfullt? {x.acknowledged}.\nID: {x.inserted_id}')

# Insert many documents
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
y = mycol.insert_many(mylist)

# Check the document
print(f'Data inserted successfullt? {y.acknowledged}.\nID: {y.inserted_ids}')

# Query one document
a = mycol.find_one()
print(a)

# Query all docs
# find() Returns a cursor object which is an iterator
for i in mycol.find():
    print(i)

# Limit the Result
print('-' * 50)
for i in mycol.find().limit(5):
    print(i)
# Return Only Some Fields
"""
The second parameter of the find() method is an
object describing which fields to include in the 
result.

This parameter is optional, and if omitted, all 
fields will be included in the result.
"""
# Following Returns only the names and addresses,
# not the _ids:
print('-' * 50)
for i in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
    print(i)

"""You are not allowed to specify both 0 and 1 
values in the same object (except if one of the 
fields is the _id field). If you specify a field 
with the value 0, all other fields get the value 
1, and vice versa"""

# Filter the Result
myquery = { "address": "Park Lane 38" }
mydoc = mycol.find(myquery, {'_id': 0})
print('-'*50)
for i in mydoc:
    print(i)

"""
Find documents where the address starts with 
the letter "S" or higher:
"""
myquery = { "address": { "$gt": "S" } }
mydoc = mycol.find(myquery, {'_id': 0})
print('-'*50)
for i in mydoc:
    print(i)

# Filter With Regular Expressions
"""
Find documents where the address starts with 
the letter "S":
"""
myquery = { "address": { "$regex": "^S" } }
mydoc = mycol.find(myquery, {'_id': 0})
print('-'*50)
for x in mydoc:
    print(x)

# Sort the Result
"""
Sort the result alphabetically by name:
"""
# sort("name", 1) #ascending
# sort("name", -1) #descending
mydoc = mycol.find({}, {'_id': 0}).sort("name")
print('-'*50)
for i in mydoc:
    print(i)

# Delete a Document
"""
Delete the document with the address "Mountain 21":
"""
myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)

# Delete Many Documents
myquery = { "address": {"$regex": "^S"} }
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")

# Delete All Documents in a Collection
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")

# Delete Collection
mycol.drop()