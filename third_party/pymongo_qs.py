import pymongo

client = pymongo.MongoClient('mongodb://localhost')
db = client.test

existing_collections = db.collection_names()
if 'albums' in existing_collections:
    db.drop_collection('albums')

#C
db.albums.insert_one({'artist': 'Mastodon', 'album': 'Crack the Sky', 'year': 2009})

db['albums'].insert_many([{'artist': 'Corrosion of Conformity', 'album': 'Wiseblood', 'year': 1996}, {'artist': 'Corrosion of Conformity', 'album': 'Blind', 'year': 1991}, {'artist': 'Corrosion of Conformity', 'album': 'In the Arms of God', 'year': 2005}, {'artist': 'Corrosion of Conformity', 'album': 'Deliverance', 'year': 1994}, {'artist': 'Corrosion of Conformity', 'album': 'America\'s Volume Dealer', 'year': 2000}])

db.albums.create_index('artist')


#R
print db.albums.find_one({'artist': 'Corrosion of Conformity'})

cursor = db.albums.find({'artist': 'Corrosion of Conformity'}, {'_id': 0}).sort([('year', pymongo.ASCENDING)])
for c in cursor:
    print c


#U
db.albums.update_one({'artist': 'Mastodon', 'album': 'Crack the Sky'}, {'$set': {'album': 'Crack the Skye'}})

db.albums.update_many({'artist': 'Corrosion of Conformity'}, {'$set': {'artist': 'COC'}})


#D
db.albums.delete_one({'artist': 'Mastodon', 'album': 'Crack the Skye'})

result = db.albums.delete_many({'artist': 'COC'})
print result.deleted_count, 'COC albums deleted'

print db.albums.count(), 'albums in collection'
db.drop_collection('albums')
