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
print(f'Data inserted successfullt? {x.acknowledged}.')

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
print(f'Data inserted successfullt? {y.acknowledged}.')

# Update Collection
"""
Change the address from "Valley 345" to "Canyon 
123":
"""
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }
mycol.update_one(myquery, newvalues)
#print "customers" after the update:
print('-' * 50)
for i in mycol.find():
    print(i)

# Update Many
"""
Update all documents where the address starts 
with the letter "S":
"""
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }
x = mycol.update_many(myquery, newvalues)
print('-' * 50)
print(x.modified_count, "documents updated.")