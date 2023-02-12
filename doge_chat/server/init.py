import pymongo
client =pymongo.MongoClient(host= "127.0.0.1", port=27017)
db = client["doge_chat"]
coll = db.get_collection("user")

def alluser():
    """
    It returns a list of all the names of the users in the database
    :return: A list of all the names in the collection.
    """
    return [i["name"] for i in coll.find()]

def allpassword():
    """
    It returns a list of all the passwords in the database
    :return: A list of all the passwords in the database.
    """
    return [i["password"] for i in coll.find()]