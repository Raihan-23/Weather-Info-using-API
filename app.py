from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '49d05ec6dfd6a066eba407c6003c577d'  # Replace with your actual API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.json.get('city', '')
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    try:
        response = requests.get(weather_url)
        data = response.json()

        # Debugging output
        print(f"Request URL: {weather_url}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Data: {data}")

        if response.status_code == 200 and data.get('cod') != '404':
            return jsonify(data)
        else:
            error_message = data.get('message', 'City not found')
            return jsonify({'error': error_message})
    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
