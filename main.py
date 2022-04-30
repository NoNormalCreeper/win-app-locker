import imp
from src.utils import read_preference, read_banlist
from src.locker import kill_all_app
from time import sleep

frequency = read_preference()['frequency']
ban_list = read_banlist()

while True:
    kill_all_app(ban_list)
    sleep(frequency)
