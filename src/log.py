import logging
import datetime

def get_datetime() -> str:
    """
    Returns the current date and time
    """
    return datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

logging.basicConfig(level=logging.INFO,
                    filename=f'./data/logs/{get_datetime()}.log',
                    format="%(asctime)s - %(name)s %(levelname)-9s - %(filename)-8s : %(lineno)s line - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S"
                    )

def log(msg: str, level: str='info', is_exception: bool=False) -> None:
    """
    Logs a message
    """
    if is_exception:
        logging.exception(msg)
    else:
        if level == 'info':
            logging.info(msg)
        elif level == 'warning':
            logging.warning(msg)
        elif level == 'error':
            logging.error(msg)
        elif level == 'critical':
            logging.critical(msg)
        else:
            logging.info(msg)