from enum import Enum


class ScreenSize(Enum):
    DESKTOP = [1980, 720]
    TABLE = [800, 600]


class Browser(Enum):
    CHROME = 'CHROME'
    FIREFOX = 'FIREFOX'
