import json
json_file_path = "hello.json"

# Open the JSON file and load its contents
with open(json_file_path, "r") as file:
    json_data = json.load(file)
print(json_data["employees"][2])
for i in json_data["employees"]:
    print(i["name"])
    print(i["department"])
