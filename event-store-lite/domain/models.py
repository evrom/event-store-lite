from abc import ABCMeta, abstractmethod
from collections import namedtuple

Event = namedtuple('Event', ['path', 'content_type', 'body'])


class Store(metaclass=ABCMeta):
    @abstractmethod
    def save(self, event: Event) -> str:
        """save event to storage backend, return event id"""
        raise NotImplementedError


class Post(metaclass=ABCMeta):
    @abstractmethod
    def post_to_subscribers(self) -> None:
        """send event to subscribers"""
        raise NotImplementedError
