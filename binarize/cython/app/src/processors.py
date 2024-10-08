from extract.base import DiseaseExtractor
from load.base import RasterLoader
from PIL import Image
from pytesseract import image_to_string


def get_image_text(img: str) -> str:
    loader = RasterLoader()
    image = loader.load(img)
    text = image_to_string(image)
    return text


def get_disease(n: int) -> list[str]:
    extractor = DiseaseExtractor()
    return [extractor.extract() for i in range(n)]
