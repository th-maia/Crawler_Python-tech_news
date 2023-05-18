from abc import ABC, abstractmethod
from dataclasses import dataclass
import sys


@dataclass
class BaseOption(ABC):
    desc: str

    @classmethod
    def exec(cls):
        try:
            return cls._exec()
        except Exception as e:
            sys.stderr.write(e.__str__())

    @classmethod
    @abstractmethod
    def _exec(cls):
        raise "Not implemented yet"
