from abc import ABC, abstractmethod


class Scene(ABC):
    """
    Interface to be implemented by all scenes
    """

    def __init__(self, surface):
        self.surface = surface

    @abstractmethod
    def handle_events(self, event):
        pass

    @abstractmethod
    def render(self):
        pass
