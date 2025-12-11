#B1: Import thư viện trc.
#B2: dùng cú pháp with open
import json
with open("../BUOI 3/food.json", "r", encoding="utf-8") as f:
    try:
        cookingway = json.load(f)
        #print(cookingway)
        print("Name of food: ", cookingway["name"])
    except Exception as e:
        print('File Error: ', e)

