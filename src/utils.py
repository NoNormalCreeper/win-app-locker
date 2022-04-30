config_path = "./data/config.json"

import os
import json
from src.log import log

def read_config() -> dict:
    try:
        with open(config_path, encoding='utf-8') as f:
            config = json.load(f)
    except FileNotFoundError:
        # copy example_config.json
        with open(config_path+'.example', encoding='utf-8')as f:
            config = json.load(f)
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=4)
        log(f'{config_path} not found, created a new one.', 'warning')
    finally:
        log(f'Read config from {config_path}:\n{config}')
        return config
            
def read_banlist() -> list:
    config = read_config()
    return config['ban_list']

def read_preference() -> dict:
    config = read_config()
    return config['preference']