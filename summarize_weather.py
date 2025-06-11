import os
import sys
import json
import requests

API_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(zip_code, api_key):
    params = {"zip": zip_code, "units": "imperial", "appid": api_key}
    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def main():
    if len(sys.argv) < 2:
        print("Usage: python summarize_weather.py <ZIPCODE>")
        sys.exit(1)

    zip_code = sys.argv[1]
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        print("Environment variable OPENWEATHERMAP_API_KEY is not set.")
        sys.exit(1)

    try:
        data = fetch_weather(zip_code, api_key)
    except requests.RequestException as exc:
        print(f"Failed to fetch weather: {exc}")
        sys.exit(1)

    with open("weather.json", "w") as f:
        json.dump(data, f, indent=2)

    main_temp = data.get("main", {})
    temp = main_temp.get("temp")
    temp_min = main_temp.get("temp_min")
    temp_max = main_temp.get("temp_max")

    print(f"Current temperature: {temp}°F (High: {temp_max}°F, Low: {temp_min}°F)")


if __name__ == "__main__":
    main()
