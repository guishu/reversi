from abc import ABC, abstractmethod


class Renderer(ABC):
    """
    Interface to be implemented by all renderers
    """

    @abstractmethod
    def render(self, surface):
        pass
