config_path = "./data/config.json"
banlist_txt_path = "./data/banlist.txt"

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
    preference = read_preference()
    if preference['read_banlist_mode'] == 'json':
        log(f'Read banlist from {config_path}')
        return config['ban_list']
    elif preference['read_banlist_mode'] == 'txt':
        try:
            with open(banlist_txt_path, encoding='utf-8') as f:
                result = [line.strip() for line in f.readlines()]
                log(f'Read banlist from {banlist_txt_path}')
        except:
            with open(banlist_txt_path+'.example', encoding='utf-8') as df:
                with open(banlist_txt_path, 'w', encoding='utf-8') as f:
                    text = df.read()
                    f.write(text)
                    result = [line.strip() for line in df.readlines()]
                log(f'{banlist_txt_path} not found, created a new one.', 'warning')
        finally:
            return result

def read_preference() -> dict:
    config = read_config()
    return config['preference']