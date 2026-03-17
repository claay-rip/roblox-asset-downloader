import logging
from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)

class CustomLogger(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def format(self, record):
        log_clrs = {
            'DEBUG': Fore.CYAN,
            'INFO': Fore.GREEN,
            'WARNING': Fore.YELLOW,
            'ERROR': Fore.RED,
            'CRITICAL': Fore.RED + Style.BRIGHT
        }

        clr = log_clrs.get(record.levelname, Fore.WHITE)
        timestamp = datetime.fromtimestamp(record.created).strftime('%H:%M:%S')

        return (f'{Fore.WHITE}[{timestamp}]{Style.RESET_ALL} '
                f'{clr}[{record.levelname}]{Style.RESET_ALL}: '
                f'{Fore.CYAN}{record.getMessage()}{Style.RESET_ALL}')


def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    cn_handler = logging.StreamHandler()
    cn_handler.setLevel(logging.INFO)
    cn_handler.setFormatter(CustomLogger('%(message)s'))
    logger.addHandler(cn_handler)

    log_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    f_handler = logging.FileHandler(f'logs/log-{log_time}.txt', encoding='utf-8')
    f_handler.setLevel(logging.DEBUG)

    f_formatter = logging.Formatter('[%(asctime)s] [%(levelname)s]: %(message)s', datefmt='%H:%M:%S')
    f_handler.setFormatter(f_formatter)
    logger.addHandler(f_handler)

    return logger