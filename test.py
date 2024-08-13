import httpx
import json
import pprint

# # Define the URL for the 15-day forecast
# fifteen_day_forecast_url = "http://xml.customweather.com/xml/v2?client=azurecloud&client_password=76N4gH38tm&product=15day_expanded_forecast&id=gn1273293&metric=false&format=json"

# # Fetch the 15-day forecast data
# response = httpx.get(fifteen_day_forecast_url)
# print(response)
# fifteen_day_forecast = response.json()

# # Save the forecast data to a file
# file_name = "forecast_on_" + fifteen_day_forecast["report"]["localtime"].split(" ")[1] + "_" + fifteen_day_forecast["report"]["localtime"].split(" ")[2] + "_" + fifteen_day_forecast["report"]["localtime"].split(" ")[3]
# with open(f'{file_name}.json', 'w') as f:
#     json.dump(fifteen_day_forecast, f)

# # Define the URL for historical data
# start_time = "2023-07-20"
# end_time = "2024-07-18"
# historical_url = "https://xml.customweather.com/xml/v2?client=sampleuser&client_password=samplepassword&product=daily_climate&id=gn1273293&start_time=" + start_time + "&end_time=" + end_time + "&format=json"
# print(historical_url)

# # Fetch the historical data
# response = httpx.get(historical_url, verify=False)
# historical_data = response.json()

# # Save the historical data to a file
# file_name = "historical_data_" + start_time + "_" + end_time
# with open(f'{file_name}.json', 'w') as f:
#     json.dump(historical_data, f)

# # Pretty print the historical data
# pprint.pprint(historical_data)


# import requests

import requests
import urllib3

# requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'

# Define the URL for historical data
start_time = "2023-07-20"
end_time = "2024-07-18"
historical_url = "https://xml.customweather.com/xml/v2?client=sampleuser&client_password=samplepassword&product=daily_climate&id=gn1273293&start_time=" + start_time + "&end_time=" + end_time + "&format=json"
page = requests.get(historical_url, verify=False)
# Fetch the historical data
response = httpx.get(historical_url, verify=False)
historical_data = response.json()

# Save the historical data to a file
file_name = "historical_data_" + start_time + "_" + end_time
with open(f'{file_name}.json', 'w') as f:
    json.dump(historical_data, f)

# Pretty print the historical data
pprint.pprint(historical_data)
# # Make the GET request with SSL verification disabled
# try:
#     response = requests.get(url, params=params, verify=False)
#     response.raise_for_status()  # Raise an error for bad status codes
    
#     # Check the response content and attempt to parse JSON
#     if response.content:
#         try:
#             data = response.json()
#             print(data)
#         except requests.exceptions.JSONDecodeError as e:
#             print("Error decoding JSON:", e)
#             print("Response content:", response.content.decode('utf-8'))
#     else:
#         print("Empty response received")
# except requests.exceptions.SSLError as e:
#     print(f"SSL error: {e}")
# except requests.exceptions.RequestException as e:
#     print(f"Request error: {e}")
