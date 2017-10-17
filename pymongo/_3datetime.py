
import datetime
import pymongo
from pymongo import MongoClient
myClinet = MongoClient()
db = myClinet["my_database"] # db name
users = db["users"]  # collections

# date time
current_date = datetime.datetime.now()
old_date= datetime.datetime(2016,7,14)

# insert date time
users.insert({"username":"user","password":"2314","date":current_date})


# find
find = db.users.find({"username":"apple"}).count()
print(find)

# find $gt 
find_gt = db.users.find({"date":{"$gt":old_date}}).count()
print(find_gt)

# find $gte
find_gte = db.users.find({"date":{"$gte":old_date}}).count()
print(find_gte)

# find $lt
find_lt = db.users.find({"date":{"$lt":old_date}}).count()
print(find_lt)

# find $lte
find_lte = db.users.find({"date":{"$lte":old_date}}).count()
print(find_lte)

# find $exists
find_exists = db.users.find({"date":{"$exists":True}}).count()
print(find_exists)


# find $ne  : not eqaul
find_ne = db.users.find({"username":{"$ne":"apple"}}).count()
print(find_ne)