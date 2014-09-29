import pygame


def load_image(imagePath):
    image = pygame.image.load(imagePath)
    image.set_colorkey((255,255,255,255))

    return image

def load_images(imagesPath):
        images = []
        imageNum = 1
        while True:
            try:
                image = load_image(imagesPath.format(imageNum))
            except:
                break
            images.append(image)

            imageNum += 1

        return images
