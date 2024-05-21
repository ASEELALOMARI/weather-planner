from pymongo import MongoClient

client = MongoClient(host="weather_mongodb", port=27017)
db = client['weather_db']
collection = db['weather_collection']

def save_to_mongodb(city_name, *weather_data, description, img_URL):

    data_to_insert = {
        'city': city_name,
        'img': img_URL,
        'time': weather_data[0],
        'temp':weather_data[1],
        'day':weather_data[2],
        'weather':weather_data[3],
        'Precipitation':weather_data[4],
        'wind':weather_data[5],
        'description': description,
    }

    collection.insert_one(data_to_insert)





def display_data():

    # Retrieve all data from the collection
    all_data = list(collection.find())


    return all_data



def delete_columns(city_name, columns_to_delete):

    # Find the document by city name
    document = collection.find_one({'city': city_name})

    # Delete specified columns
    for column in columns_to_delete:
        document.pop(column, None)

    # Update the document in the collection
    collection.update_one({'_id': document['_id']}, {'$set': document})

