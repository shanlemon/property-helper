import requests
import csv

url = "https://www.affordablehousing.com/v4/AjaxHandler?message=GetRentEstimate"

# properties = [["425000", "2320 Gracy Farms Ln, Austin, TX 78758", "3"],
#              ["480990", "2408 Sisterdale Lane, AUSTIN, TX 78754", "4"]]

responses = []

# get property data from csv using semi-colon as delimiter
with open('data.csv', newline='') as csvfile:
  properties = list(csv.reader(csvfile, delimiter=';'))
  print(properties)
  for property in properties:
    payload = {
        "address": property[1],
        "bedCount": property[2]
    }

    response = requests.post(url, json=payload)
    json_data = response.json()
    # add address and bedCount to response
    json_data['address'] = property[1]
    json_data['bedCount'] = property[2]
    json_data['price'] = property[0]
    json_data['costToRentRatio'] = int(property[0]) / json_data['values'][3]
    responses.append(json_data)

  print(responses)
  # sort responses by rent
  responses.sort(key=lambda x: x['costToRentRatio'], reverse=True)
  
  # print responses
  print("--------------------")
  for response in responses:
    address = response['address']
    bedCount = response['bedCount']
    price = response['price']
    rent = response['values'][3]
    costToRentRatio = response['costToRentRatio']

    print(address)
    print("Price $" + price)
    print("Rent Estimate $" + str(rent))
    print("Cost to Rent Ratio $" + str(costToRentRatio))
    print("--------------------")
    
