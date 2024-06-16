import json

def get_key():
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
        return config['master_password']
    except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
        print(f"Error reading the secret key: {e}")
        return None