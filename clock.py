import requests

clock = "https://api.ipgeolocation.io/timezone?apiKey=&tz=America/Los_Angeles"
response = requests.request("GET", clock)
#Time
time = response.json()["time_12"]
#Date
month = response.json()["month"]
day = response.json()["year_abbr"]
year = response.json()["year"]
all = (f"At {time}, on {month}/{day}/{year}")
print(all)
