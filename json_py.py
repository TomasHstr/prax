import json
json_file_path = "hello.json"

with open(json_file_path, "r") as file:
    json_data = json.load(file)
print(json_data["employees"][2])
#for i in json_data["employees"]:
    #print(i["name"])
    #print(i["department"])

#for i in json_data["employees"]:
    #if ["In Progress"] in ["projects"] :
        #print([i"name"])
    #print(i["department"])



for i in json_data["employees"]:
    for j in i["projects"]:
        if j["status"] == "In Progress":
            print(i["name"])
            break