from abc import ABC, abstractmethod


class Indicator(ABC):
    """
        Abstract Base Class for Indicator
    """

    @abstractmethod
    def _get_data(self):
        """
        """
        raise NotImplementedError

    @abstractmethod
    def calculate(self):
        """
        """
        raise NotImplementedError

