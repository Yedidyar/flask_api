import requests

BASE =" http://127.0.0.1:5000/"
data = [{"likes":10,"name":'jeo',"views":5003202},
        {"likes":100,"name":'hello',"views":5003402},
        {"likes":10,"name":'me',"views":500042}]
for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

# response = requests.delete(BASE + "video/2")
# print(response)
input()
response = requests.get(BASE + "video/1")
print(response.json())