# weather_power_dashboard.py

import requests
import csv
import datetime
import os
import matplotlib.pyplot as plt

# ========== CONFIGURATION ========== #
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
CITY = "Oklahoma City"
UNITS = "imperial"  # Use 'metric' for Celsius
LOG_FILE = "weather_log.csv"
GRAPH_FILE = "weather_trend.png"

# ========== FUNCTIONS ========== #
def fetch_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        raise Exception(f"API error: {data.get('message', 'Unknown error')}")

    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    return temp, desc

def generate_recommendation(temp):
    if temp > 85:
        return "Recommend increased AC usage"
    elif temp < 60:
        return "Recommend heating"
    else:
        return "Moderate temperature – normal power usage"

def log_data(temp, desc, recommendation):
    now = datetime.datetime.now()
    file_exists = os.path.isfile(LOG_FILE)
    
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Temperature", "Description", "Recommendation"])
        writer.writerow([now.strftime("%Y-%m-%d %H:%M:%S"), temp, desc, recommendation])

def plot_data():
    timestamps = []
    temps = []

    with open(LOG_FILE, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            timestamps.append(row['Timestamp'])
            temps.append(float(row['Temperature']))

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, temps, marker='o', linestyle='-', color='teal')
    plt.xticks(rotation=45)
    plt.title('Temperature Trends Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel(f'Temperature ({"F" if UNITS == "imperial" else "C"})')
    plt.tight_layout()
    plt.savefig(GRAPH_FILE)
    plt.close()

# ========== MAIN ========== #
def main():
    try:
        temp, desc = fetch_weather()
        recommendation = generate_recommendation(temp)
        log_data(temp, desc, recommendation)
        plot_data()
        print("Weather data logged and graph updated.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
