import logging
import datetime

def get_datetime() -> str:
    """
    Returns the current date and time
    """
    return datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

logging.basicConfig(level=logging.INFO #设置日志输出格式
                    ,filename=f'./data/{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}.log' #log日志输出的文件位置和文件名
                    ,format="%(asctime)s - %(name)s %(levelname)-9s - %(filename)-8s : %(lineno)s line - %(message)s" #日志输出的格式
                    # -8表示占位符，让输出左对齐，输出长度都为8位
                    ,datefmt="%Y-%m-%d %H:%M:%S" #时间输出的格式
                    )

def log(msg: str, level: str) -> None:
    """
    Logs a message
    """
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