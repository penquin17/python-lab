from src.processors import get_image_text, get_disease


def serve():
    image = '/data/cv-image.png'
    text = get_image_text(image)
    print(text)
    print(get_disease(5))


if __name__ == "__main__":
    serve()
