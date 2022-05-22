import requests

api_key = "b1459c84875157ab387f3ba73e9b1e1a"

LAT = 5.008640
LONG = 19.447884

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)

data = response.json()

will_rain = False

for n in range(0, 12):
    if data["hourly"][n]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("Bring your umbrella")
