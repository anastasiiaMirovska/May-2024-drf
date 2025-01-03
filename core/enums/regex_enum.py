from enum import Enum


class RegexEnum(Enum):
    NAME = (
        r'^[A-Z][a-z]{,19}$',
        'Only alpha characters are allowed. First character must be uppercase.'
    ) # NAME - це екземпляр класу RegexEnum
    
    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg
