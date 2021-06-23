import requests
 # To execute get request
response = requests.get('https://www.delish.com/cooking/menus/')
print("Response text of https://www.delish.com/cooking/menus/")
# To print response bytes 
print(response.text)
print("\n========================================================")
print("\nContent :")
 # To print unicode response string 
print(response.content)
print("\n=======================================================")
print("\nRaw data :")
re = requests.get('https://api.github.com/events', stream = True)
print(re.raw)
print(re.raw.read(15))
