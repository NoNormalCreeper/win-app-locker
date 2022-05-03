try:
    from src.log import log
    import asyncio
    from src.utils import config
    from src.locker import show_error_box, kill_all_app
    from time import sleep

    frequency = config.preference['frequency']
    mode = config.preference['mode']
    ban_list = config.ban_list
    
    flag = 1
    while True:
        try:
            if flag:
                log('====Started locker.====')
                flag = 0
            if mode == 'kill':
                asyncio.get_event_loop().run_until_complete(kill_all_app(ban_list))
            elif mode == 'lock':
                # TODO: Implement lock mode
                pass
            # elif mode == ...
            # ......
            else:
                log(f'Mode "{mode}" is not supported.', 'error')
            sleep(frequency)
        except Exception as e:
            log(str(e), is_exception=True)

except Exception as e:
    log(str(e), is_exception=True)
    asyncio.get_event_loop().run_until_complete(show_error_box(message=f'An Exception occured:\n{str(e)}',title="Error"))