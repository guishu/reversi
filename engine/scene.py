from abc import ABC, abstractmethod


class Scene(ABC):
    """
    Interface to be implemented by all scenes
    """

    @abstractmethod
    def handle_events(self, event):
        pass

    @abstractmethod
    def render(self):
        pass
