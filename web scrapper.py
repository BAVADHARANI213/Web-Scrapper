import requests
from bs4 import BeautifulSoup

# Function to scrape weather data from a website
def scrape_weather(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example selectors, update as per the actual website structure
    location = soup.find('h1', class_='CurrentConditions--location--1Ayv3').text
    temperature = soup.find('span', class_='CurrentConditions--tempValue--3KcTQ').text
    condition = soup.find('div', class_='CurrentConditions--phraseValue--2xXSr').text

    return {
        'location': location,
        'temperature': temperature,
        'condition': condition
    }

# Function to get weather data from OpenWeatherMap API
def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        return {"error": data["message"]}

    weather = {
        'location': data['name'],
        'temperature': data['main']['temp'],
        'condition': data['weather'][0]['description']
    }
    return weather

# Main function to run the script
if __name__ == "__main__":
    # Web scraping example
    url = 'https://weather.com/weather/today/l/YOUR_LOCATION_CODE'
    try:
        weather_data_scraped = scrape_weather(url)
        print("Scraped Weather Data:")
        print(f"Location: {weather_data_scraped['location']}")
        print(f"Temperature: {weather_data_scraped['temperature']}")
        print(f"Condition: {weather_data_scraped['condition']}")
    except Exception as e:
        print(f"An error occurred while scraping: {e}")

    # API example
    api_key = 'YOUR_API_KEY'
    city = 'London'
    weather_data_api = get_weather(api_key, city)
    print("\nAPI Weather Data:")
    if "error" in weather_data_api:
        print(f"Error: {weather_data_api['error']}")
    else:
        print(f"Location: {weather_data_api['location']}")
        print(f"Temperature: {weather_data_api['temperature']}°C")
        print(f"Condition: {weather_data_api['condition']}")
