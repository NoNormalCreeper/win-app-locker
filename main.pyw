try:
    from src.log import log
    from src.utils import read_preference, read_banlist
    from src.locker import kill_all_app
    from time import sleep
    import asyncio

    frequency = read_preference()['frequency']
    ban_list = read_banlist()

    while True:
        try:
            asyncio.get_event_loop().run_until_complete(kill_all_app(ban_list))
            sleep(frequency)
        except Exception as e:
            log(str(e), is_exception=True)

except Exception as e:
    log(str(e), is_exception=True)