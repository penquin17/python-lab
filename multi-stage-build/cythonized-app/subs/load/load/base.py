import abc
from typing import Any

from PIL import Image


class Loader(abc.ABC):
    def load(self):
        """Method to load
        """


class FileLoader(Loader):
    def load(self):
        """Method to load file
        """


class RasterLoader(FileLoader):
    def load(self, path: str) -> Any:
        image = Image.open(path).convert("RGB")
        return image
