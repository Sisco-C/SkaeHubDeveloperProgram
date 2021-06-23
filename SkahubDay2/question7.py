import WebData
data = WebData.WebData("https://spoonacular.com/food-api/apps")
print("WebData Type:")
print(type(data.parseJson()))
print("\nWebData:")
print(data.parseJson())
