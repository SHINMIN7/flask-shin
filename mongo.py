import pymongo 
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://yheyhe1234:alscjf6173!2k@shin07.fouricn.mongodb.net/?retryWrites=true&w=majority")
db = cluster["software_engineering"]
collection = db["test"]

#post = {"_id":0, "name":"WoongSup", "score": 90}
post1 = {"name":"YeHyun", "score": 80}
post2 = {"name":"JiYoung", "score": 70}


#collection.insert_one(post)
collection.insert_many([post1,post2])

results = collection.find({"name":"JiYoung"})
for results in results:
    print(results)




