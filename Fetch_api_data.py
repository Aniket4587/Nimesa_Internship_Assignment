import requests
from datetime import datetime

def get_weather_data():
    url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

def get_weather_by_date(weather_data, target_date):
    for data in weather_data["list"]:
        dt_txt = datetime.strptime(data["dt_txt"], "%Y-%m-%d %H:%M:%S")
        if dt_txt.date() == target_date.date():
            return data["main"]["temp"]
    return None

def get_wind_speed_by_date(weather_data, target_date):
    for data in weather_data["list"]:
        dt_txt = datetime.strptime(data["dt_txt"], "%Y-%m-%d %H:%M:%S")
        if dt_txt.date() == target_date.date():
            return data["wind"]["speed"]
    return None

def get_pressure_by_date(weather_data, target_date):
    for data in weather_data["list"]:
        dt_txt = datetime.strptime(data["dt_txt"], "%Y-%m-%d %H:%M:%S")
        if dt_txt.date() == target_date.date():
            return data["main"]["pressure"]
    return None

def main():
    weather_data = get_weather_data()
    if not weather_data:
        return

    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            date_str = input("Enter date (YYYY-MM-DD): ")
            target_date = datetime.strptime(date_str, "%Y-%m-%d")
            temperature = get_weather_by_date(weather_data, target_date)
            if temperature is not None:
                print(f"Temperature on {target_date.strftime('%Y-%m-%d')}: {temperature:.2f}°C")
            else:
                print("Weather data not found for the given date.")
        elif choice == 2:
            date_str = input("Enter date (YYYY-MM-DD): ")
            target_date = datetime.strptime(date_str, "%Y-%m-%d")
            wind_speed = get_wind_speed_by_date(weather_data, target_date)
            if wind_speed is not None:
                print(f"Wind Speed on {target_date.strftime('%Y-%m-%d')}: {wind_speed} m/s")
            else:
                print("Weather data not found for the given date.")
        elif choice == 3:
            date_str = input("Enter date (YYYY-MM-DD): ")
            target_date = datetime.strptime(date_str, "%Y-%m-%d")
            pressure = get_pressure_by_date(weather_data, target_date)
            if pressure is not None:
                print(f"Pressure on {target_date.strftime('%Y-%m-%d')}: {pressure} hPa")
            else:
                print("Weather data not found for the given date.")
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
