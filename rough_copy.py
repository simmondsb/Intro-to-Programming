import requests
#Menu
#def printGarageMenu(self):  
 # print("Welcome to WeatherMap")
 # print("[1] To enter zip code")
  #print("[2] To enter city ")
  ##print("[3] Quit ")
 # return int(input("Choose an option from the menu: "))
#Call API
  
key = "e62e816d5963e945771e6dd02cc07b61"
url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=e62e816d5963e945771e6dd02cc07b61'
querystring = {"zip": "76002", "APPID": "e62e816d5963e945771e6dd02cc07b61"}
headers = {'cashe-control': "no-cache"}
response = requests.request("GET", url, headers=headers,params=querystring)
response_dict=(response.json())

print(response_dict.keys())
#print(response_dict)
#print(response_dict['list'])
#new_tem=response_dict['list']
#print (new_tem)
#print(response_dictget.get['main'])
#print(list.keys())
type (['list'])