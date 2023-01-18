import requests

url = "https://real-time-google-search.p.rapidapi.com/location"

querystring = {"location_name":"Italy","country_code":"IT"}

headers = {
	"X-RapidAPI-Host": "real-time-google-search.p.rapidapi.com",
	"X-RapidAPI-Key": "a5ac913853msha6d54736cd1b30dp1b62ffjsnf73d35d4c528"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)