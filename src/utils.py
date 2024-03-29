config_path = "./data/config.json"
banlist_txt_path = "./data/banlist.txt"

import os
import json
from src.log import log
from functools import cached_property


def read_config() -> dict:
    try:
        with open(config_path, encoding='utf-8') as f:
            config = json.load(f)
    except FileNotFoundError:
        # copy example_config.json
        with open(f'{config_path}.example', encoding='utf-8') as f:
            config = json.load(f)
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=4)
        log(f'{config_path} not found, created a new one.', 'warning')
    finally:
        log(f'Read config from {config_path}:\n{config}')
        return config

class Config:
    def __init__(self):
        self.config = read_config()
    
    @cached_property
    def config(self) -> dict:
        return read_config()
    
    @cached_property
    def preference(self) -> dict:
        return read_preference()
    
    @cached_property
    def ban_list(self) -> list:
        return read_banlist()

config = Config()


def read_banlist() -> list:
    preference = config.preference
    if preference['read_banlist_mode'] == 'json':
        ban_list = config.config['ban_list']
        source = config_path
    elif preference['read_banlist_mode'] == 'txt':
        try:
            with open(banlist_txt_path, encoding='utf-8') as f:
                ban_list = [line.strip() for line in f.readlines()]
        except:
            with open(f'{banlist_txt_path}.example', encoding='utf-8') as df:
                with open(banlist_txt_path, 'w', encoding='utf-8') as f:
                    text = df.read()
                    f.write(text)
                    ban_list = [line.strip() for line in df.readlines()]
                log(f'{banlist_txt_path} not found, created a new one.', 'warning')
        finally:
            source = banlist_txt_path
            log(f'Read banlist from {source}:\n{ban_list}')
            return ban_list

def read_preference() -> dict:
    return config.config['preference']