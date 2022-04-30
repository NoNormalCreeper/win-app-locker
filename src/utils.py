config_path = "./data/config.json"

from doctest import Example
import json

def read_config() -> dict:
    try:
        with open(config_path, encoding='utf-8') as f:
            config = json.load(f)
    except FileNotFoundError:
        with open(config_path, 'w') as f:
            with open("./data/default_config.json", encoding='utf-8') as df:
                config = json.load(df)
                json.dump(config, f)
    return config

def read_banlist() -> list:
    config = read_config()
    return config['ban_list']

def read_preference() -> dict:
    config = read_config()
    return config['preference']