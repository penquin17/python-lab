import abc
import random
from typing import Any


class Extractor(abc.ABC):
    def extract(self):
        """Method to load
        """


class DiseaseExtractor(Extractor):
    def extract(self) -> Any:
        """Method to extract disease
        """
        return random.choices(["Diabetes", "Cancer", "Allergies", "Obesity"])[0]
