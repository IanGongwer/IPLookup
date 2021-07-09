import requests as r

api_key = "18b430b6f395c6f9fb8697cbaad61dbc"

ip = input("IP to track: ")

api_request = {"access_key" : api_key}
lookup = r.get("http://api.ipapi.com/" + ip, params=api_request)

response = lookup.json()
print("IP Type:", response["type"])
print("Country:", response["country_name"], "| Region:", response["region_name"], "| City:", response["city"])
print("Latitude:", response["latitude"], "| Longitude:", response["longitude"])
print("")

geolocation_ip = "latlong.net/c/?lat=" + str(response["latitude"]) + "&long=" + str(response["longitude"])

print(geolocation_ip)