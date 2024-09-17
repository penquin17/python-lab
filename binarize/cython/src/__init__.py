from .processors import get_image_text

def serve():
    image = '/data/cv-image.png'
    text = get_image_text(image)
    print(text)