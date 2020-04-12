"""



"""

import abc
from itertools import chain


class BaseTool(metaclass=abc.ABCMeta):

    @classmethod
    def get_subclasses(cls):
        """
        Collect all BaseTool subclasses
        :return:
        """
        direct = cls.__subclasses__()
        recursive = chain.from_iterable(
            sub.get_subclasses() for sub in direct
        )
        return chain(direct, recursive)

    @abc.abstractmethod
    def __str__(self):
        """
        A tool's string representation
        :return:
        """

    @abc.abstractmethod
    def available(self) -> bool:
        """
        Check whether a tool is available
        :return:
        """
        pass


if __name__ == '__main__':
    raise RuntimeError
