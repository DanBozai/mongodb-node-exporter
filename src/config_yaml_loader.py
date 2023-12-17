import yaml

def load_yaml_file(file_path):
    config_file_data= None
    if file_path:
        try:
            with open(file_path,'r') as config_file:
                config_file_data =yaml.safe_load(config_file)
        except Exception as err:
            print(err)
            
    return config_file_data
        
