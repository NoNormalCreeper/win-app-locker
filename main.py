try:
    from src.log import log
    from src.utils import read_preference, read_banlist
    from src.locker import kill_all_app
    from time import sleep

    frequency = read_preference()['frequency']
    ban_list = read_banlist()

    while True:
        try:
            resp = kill_all_app(ban_list)
            if resp:
                log(f'Successfully killed {resp}')
            sleep(frequency)
        except Exception as e:
            log(str(e), is_exception=True)

except Exception as e:
    log(str(e), is_exception=True)