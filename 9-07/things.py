import yaml

with open("9-07/config.yaml","r") as file:
    data = yaml.safe_load(file)

for tag in data["tags"]:
    print(tag)
    
student_dict = {
    "name": "Kane",
    "age": 21,
    "grades": [100, 90, 80]
}

with open("9-07/config2.yaml", "w") as f:
    yaml.dump(student_dict, f, sort_keys=False)