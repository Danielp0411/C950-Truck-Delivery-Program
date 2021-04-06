from datetime import timedelta
from typing import Any


class ANSICodes:
    CLEAR = '\033[0m'
    GREEN = '\u001b[32;1m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    YELLOW = '\u001b[33;1m'

    @staticmethod
    def green(line: Any) -> str:
        return f'{ANSICodes.GREEN}{line}{ANSICodes.CLEAR}'

    @staticmethod
    def blue(line: Any) -> str:
        return f'{ANSICodes.BLUE}{line}{ANSICodes.CLEAR}'

    @staticmethod
    def cyan(line: Any) -> str:
        return f'{ANSICodes.CYAN}{line}{ANSICodes.CLEAR}'

    @staticmethod
    def yellow(line: Any) -> str:
        return f'{ANSICodes.YELLOW}{line}{ANSICodes.CLEAR}'


#  calculates the time it takes to reach an address by the miles travelled
def time_calculator(miles):
    time = miles / 18
    return timedelta(hours=time)
