import yaml
from datetime import datetime

def create_yaml_with_datetime(filename):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {"date_and_time": current_datetime}

    with open(filename, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

    print(f"Date and time written to {filename}")

filename = 'datetime.yaml'
create_yaml_with_datetime(filename)


