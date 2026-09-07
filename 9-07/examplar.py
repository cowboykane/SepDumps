# uhhh

import yaml

with open("9-07/example.yml", "r") as f:
    data = yaml.safe_load(f)
    
print(data.get("pipeline_name"))

