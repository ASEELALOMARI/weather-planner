from flask import Flask, render_template, request, session,jsonify
import logging
import config

from weather_API import get_weather_data
from Database import save_to_mongodb, display_data
from weather_images import get_image_url
from city_data import city_data


app = Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

@app.route('/')
def index():

    #list all the city name in drop list
    city_list = list(city_data.keys())

    return render_template('index.html', error=False, city_list = city_list)


@app.route('/search', methods=['POST'])
def search():
        if request.method == 'POST':
            city_name = request.form['city_name']
            description = request.form['description']
            

            if city_name in city_data:
                city_info = city_data[city_name]
                latitude = city_info['latitude']
                longitude = city_info['longitude']
                timezone = city_info['timezone']

                # Get weather data from the API 
                weather_data = get_weather_data(latitude, longitude, timezone)

                #Get img url 3 for weather decryptions and 2 for day or night 
                img_URL = get_image_url(weather_data[3], weather_data[2])

                session['save_data'] = {
                'city_name': city_name,
                'weather_data': weather_data,
                'description': description,
                'img_URL': img_URL
                }
                
            result = {"city_name": city_name, "description": description,"weather_data": weather_data, "img_URL": img_URL}
            return jsonify({'result': render_template('result.html', result=result)})
        else:
            return jsonify({'result': render_template('result.html', error=True)})

@app.route('/save', methods=['POST'])
def save():

    print(request.form)
        # Retrieve data from the session
    save_data = session.pop('save_data', None)

    if save_data:
        # Extract data from the saved session data
        city_name = save_data['city_name']
        weather_data = save_data['weather_data']
        description = save_data['description']
        img_URL = save_data['img_URL']

        print("there is a data")

        # Save to MongoDB or your database
        save_to_mongodb(city_name, *weather_data, description = description, img_URL = img_URL)
        session.pop('save_data', None)

        # Return a JSON response
        return jsonify({'status': 'success', 'message': 'Data saved successfully'})

    return jsonify({'status': 'error', 'message': 'No data to save'})


@app.route('/display')
def display():
    all_data = display_data()
    return jsonify({'all_data': render_template('displayed_data.html', all_data=all_data)})
     

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    app.logger.info(f"Opening for global access on port {CONFIG.PORT}")
    app.run(port=CONFIG.PORT, host="0.0.0.0", debug=True)
