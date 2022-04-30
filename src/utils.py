config_path = "./data/config.json"

import json

def read_config() -> dict:
    with open(config_path, encoding='utf-8') as f:
        config = json.load(f)
    return config

def read_banlist() -> list:
    config = read_config()
    return config['banlist']

def read_preference() -> dict:
    config = read_config()
    return config['preference']